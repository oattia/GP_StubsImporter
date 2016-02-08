import xml.etree.ElementTree as xml
import pymysql
import sql_tuple
import time
import weakref

def insert(records):
    sql = 'INSERT INTO `en_articles` (`pid`, `ns`, `title`) VALUES (%s, %s, %s);'
    for rec in records: 
        with connection.cursor() as cursor:
            cursor.execute(sql, (rec.id, rec.ns, rec.title))
    connection.commit()
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='(Abo)^93',
                             db='enwiki_stub_articles',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
print("XML Loaded...")
i = 0
j = 0
context = xml.iterparse(open("enwiki-20151201-stub-articles.xml"), events=("start", "end"))

context = iter(context)

event, root = next(context)
start = int(round(time.time()))
records = []
for event, elem in context:
    if event == "end" and elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}page":
        title = elem.find("{http://www.mediawiki.org/xml/export-0.10/}title").text
        ns    = int(elem.find("{http://www.mediawiki.org/xml/export-0.10/}ns").text)
        pid   = int(elem.find("{http://www.mediawiki.org/xml/export-0.10/}id").text)
        record = sql_tuple.sql_tuple(pid, ns, title)
        records.append(record)
        i = i+1
        if i%1000 == 0:
            print(i, " Pages have been processed.")
            insert(records)
            end = int(round(time.time()))
            if(end - start) > 900:
                start = end
                print("\tLast Id inserted: ", pid)
            records = []
    del elem
    root.clear()

insert(records)
connection.close()
print("Done...")
print("I:   ", i)
print((i + len(records)), " Records Inserted.")