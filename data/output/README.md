# GML BI Community Edition (Open Source)

## About Database

There are many database management systems (DBMS) out there. But there is no
one-size-fits all database system. All take different trade-offs to better adjust to
specific use cases. DuckDB is no different. Here, we try to explain what goals DuckDB
has and why and how we try to achieve those goals through technical means. To start
with, DuckDB is a relational (table-oriented) DBMS that supports the Structured Query
Language (SQL).

### Fast Analytical Queries

DuckDB is designed to support analytical query workloads, also known as Online
analytical processing (OLAP). These workloads are characterized by complex, relatively
long-running queries that process significant portions of the stored dataset, for
example aggregations over entire tables or joins between several large tables. Changes
to the data are expected to be rather large-scale as well, with several rows being
appended, or large portions of tables being changed or added at the same time.

To efficiently support this workload, it is critical to reduce the amount of CPU cycles
that are expended per individual value. The state of the art in data management to
achieve this are either vectorized or just-in-time query execution engines. DuckDB
contains a columnar-vectorized query execution engine, where queries are still
interpreted, but a large batch of values (a “vector”) are processed in one operation.
This greatly reduces overhead present in traditional systems such as PostgreSQL, MySQL
or SQLite which process each row sequentially. Vectorized query execution leads to far
better performance in OLAP queries.

### Simple Operation

SQLite is the world’s most widely deployed DBMS. Simplicity in installation, and
embedded in-process operation are central to its success. DuckDB adopts these ideas of
simplicity and embedded operation.

DuckDB has no external dependencies, neither for compilation nor during run-time. For
releases, the entire source tree of DuckDB is compiled into two files, a header and an
implementation file, a so-called “amalgamation”. This greatly simplifies deployment and
integration in other build processes. For building, all that is required to build DuckDB
is a working C++11 compiler.

For DuckDB, there is no DBMS server software to install, update and maintain. DuckDB
does not run as a separate process, but completely embedded within a host process. For
the analytical use cases that DuckDB targets, this has the additional advantage of
high-speed data transfer to and from the database. In some cases, DuckDB can process
foreign data without copying. For example, the DuckDB Python package can run queries
directly on Pandas data without ever importing or copying any data.

### Feature-Rich

DuckDB provides serious data management features. There is extensive support for complex
queries in SQL with a large function library, window functions etc. DuckDB provides
transactional guarantees (ACID properties) through our custom, bulk-optimized
Multi-Version Concurrency Control (MVCC). Data can be stored in persistent, single-file
databases. DuckDB supports secondary indexes to speed up queries trying to find a single
table entry.

DuckDB is deeply integrated into Python and R for efficient interactive data analysis.
DuckDB provides APIs for Java, C, C++, and others.

### Thorough Testing

While DuckDB is created by a research group, it is not intended to be a research
prototype. DuckDB is intended to be a stable and mature database system.

To facilitate this stability, DuckDB is intensively tested using Continuous Integration.
DuckDB’s test suite currently contains millions of queries, and includes queries adapted
from the test suites of SQLite, PostgreSQL and MonetDB. Tests are repeated on a wide
variety of platforms and compilers. Every pull request is checked against the full test
setup and only merged if it passes.

In addition to this test suite, we run various tests that stress DuckDB under heavy
loads. We run the TPC-H and TPC-DS benchmarks, and run various tests where DuckDB is
used by many clients in parallel.

### Free & Open Source License

DuckDB’s development started while the main developers were public servants in The
Netherlands. We see it as our responsibility and duty to society to make the results of
our work freely available to anyone in The Netherlands or elsewhere. This is why DuckDB
is released under the very permissive MIT License. DuckDB is Open Source, the entire
source code is freely available on GitHub. We invite contributions from anyone provided
they adhere to our Code of Conduct.
