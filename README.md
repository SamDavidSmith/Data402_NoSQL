# NoSQL Introduction
## by Samuel Smith

### NoSQL is an approach to designing a database in order to store and retrieve data differently to traditional relational databases.

NoSQL databases stores data inside a single structure, rather than within multiple related tables. This dynamic schema (which is a blueprint of how data is connected to other data) would mean having rapid **scalability** when managing such a database, which is usually very large and **unstructured**.
<br> It stands for '*Not Only SQL*', which means SQL can still be used to query the data structure, just that other languages also appear alongside it.
<br>
### There are differences between SQL and NoSQL around scalability, languages used and the data schema.
![differences.png](sql_vs_nosql.jpg)
</n> We'll go through the main differences.

1. **Type of Database**:<br> Relational (SQL) Databases store structured data in rows and columns. <br>Non-relational (NoSQL) databases store data in various ways, such as key-value pairs, graph stores, and document-based. MongoDB is a very popular document-based server.
2. **Programming Languages**: <br> Relational Databases use SQL to manipulate data, which is a very powerful language when it comes to forming complex queries.<br> Non-relational databases use different languages to query their data. For example, MongoDB uses a language which has many similarities to JSON script. Cassandra uses its own querying language, CQL.
3. **Schema** (*the rules that define how data is arranged in your database, including the column data types and foreign key arrangements*): <br> SQL databases require their schemas to be pre-defined with rules before data can be inserted and queried. This also means changing the schema after insertion is complex work. <br> NoSQL databases use schemas that are flexible, as NoSQL databases store data in different forms in one structure. This means data can be created without needing a schema.
4. **Scalability**: SQL databases are mostly vertically scalable, which means you will be stacking the databases on a single server. However, enhancing the server's load would mean you would have to change RAM, CPU and storage capacities. <br> NoSQL databases are horizontally scalable, which means you can add or share across servers to handle more traffic. This enhances NoSQL size and capabilities and makes this the preferred choice for large and constantly-changing datasets.

