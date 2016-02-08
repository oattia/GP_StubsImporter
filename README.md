# GP_StubsImporter

Python script. The code is not very poratble, check it before running on your machine.

Before running it, you must have:
1- enwiki-20151201-stub-articles.xml or arwiki-20151201-stub-articles.xml in the same path.
2- Database named enwiki_stub_articles, with a table named en_articles.

It fills the en_articles table with tuples of: (`pid`, `ns`, `title`)
pid: page id, the real Wikipedia article ID.
ns: article namespace.
title: article title.

