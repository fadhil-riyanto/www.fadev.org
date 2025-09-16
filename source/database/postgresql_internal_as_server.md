# Postgresql internal (server) 

this thing explain the internal of pgsql system (not the source code I mean)

## difference between catalog vs schema

key point:
- schema is folder like, grouping table together, can be created using 
	```sql
	CREATE SCHEMA my_catalog;
	CREATE TABLE my_catalog.metadata_table (...);
	```
- catalog is system schema, can't be created manually, part of internal pgsql system
- view is a resulted table from XYZ queries, example
	```sql
	CREATE VIEW active_users AS 
		SELECT id, name, 
		FROM
			users 
		WHERE
			active = true;
	```

	then query it

	```sql
	SELECT * FROM active_users;
	```

## pg_catalog inside

this is some stuff inside of pg catalog, you can do that using `\dt pg_catalog.*`

* pg\_aggregate: Stores information about aggregate functions (like `SUM`, `AVG`, etc.).
* pg\_am: Lists access methods for indexes (e.g., `btree`, `hash`).
* pg\_amop: Defines operators used in access methods.
* pg\_amproc: Defines support functions used in access methods.
* pg\_attrdef: Stores default values for columns.
* pg\_attribute: Contains column definitions for all tables.
* pg\_auth\_members: Shows role memberships (who is a member of what).
* pg\_authid: Stores user/role definitions (superuser access required).
* pg\_cast: Contains rules for casting between data types.
* pg\_class: Contains all table-like objects (tables, views, indexes, sequences, etc.).
* pg\_collation: Defines collations (rules for string comparison).
* pg\_constraint: Stores constraints like PRIMARY KEY, UNIQUE, CHECK, and FOREIGN KEY.
* pg\_conversion: Defines character set conversions.
* pg\_database: Stores information about each database in the cluster.
* pg\_db\_role\_setting: Stores per-user/per-database configuration settings (GUCs).
* pg\_default\_acl: Defines default privileges for newly created objects.
* pg\_depend: Stores dependency relationships between database objects.
* pg\_description: Stores comments/descriptions on database objects.
* pg\_enum: Stores values for `ENUM` data types.
* pg\_event\_trigger: Stores event trigger definitions (triggers on DDL commands).
* pg\_extension: Tracks installed extensions (like `uuid-ossp`, `pgcrypto`, etc.).
* pg\_foreign\_data\_wrapper: Stores definitions of foreign data wrappers (FDW).
* pg\_foreign\_server: Stores foreign servers used by FDWs.
* pg\_foreign\_table: Stores metadata for foreign tables.
* pg\_index: Contains metadata about indexes (e.g., indexed columns).
* pg\_inherits: Stores table inheritance relationships.
* pg\_init\_privs: Records original privileges on built-in objects.
* pg\_language: Stores information about supported procedural languages.
* pg\_largeobject: Stores the actual data of large objects (blobs).
* pg\_largeobject\_metadata: Stores metadata about large objects.
* pg\_namespace: Lists all schemas in the database (IMPORTANT)
* pg\_opclass: Stores index operator classes (how a datatype is indexed).
* pg\_operator: Stores SQL operators (like `=`, `<`, `+`, etc.).
* pg\_opfamily: Groups related operator classes.
* pg\_parameter\_acl: Stores access control for configuration parameters (PostgreSQL 16+).
* pg\_partitioned\_table: Stores metadata for partitioned tables.
* pg\_policy: Stores row-level security policies.
* pg\_proc: Contains all function and procedure definitions.
* pg\_publication: Stores logical replication publications.
* pg\_publication\_namespace: Links publications to schemas.
* pg\_publication\_rel: Links publications to individual tables.
* pg\_range: Stores definitions of range types (e.g., `int4range`).
* pg\_replication\_origin: Tracks origins for logical replication.
* pg\_rewrite: Stores query rewrite rules (used in views, rules).
* pg\_seclabel: Stores security labels for database objects.
* pg\_sequence: Contains metadata for sequence generators.
* pg\_shdepend: Tracks dependencies involving shared objects (like roles, databases).
* pg\_shdescription: Stores comments on shared objects.
* pg\_shseclabel: Stores security labels on shared objects.
* pg\_statistic: Stores planner statistics for columns.
* pg\_statistic\_ext: Stores extended planner statistics (multi-column, NDV, etc.).
* pg\_statistic\_ext\_data: Contains actual values for extended statistics.
* pg\_subscription: Defines logical replication subscriptions.
* pg\_subscription\_rel: Lists tables included in subscriptions.
* pg\_tablespace: Lists all tablespaces (disk locations for data).
* pg\_transform: Stores type transformation functions for procedural languages.
* pg\_trigger: Stores triggers on tables.
* pg\_ts\_config: Stores full-text search configurations.
* pg\_ts\_config\_map: Maps text search config tokens to dictionaries.
* pg\_ts\_dict: Stores text search dictionaries.
* pg\_ts\_parser: Defines tokenizers for full-text search.
* pg\_ts\_template: Defines templates for building text search dictionaries.
* pg\_type: Stores all data types (built-in, custom, enum, composite). (IMPORTANT)
* pg\_user\_mapping: Maps users to foreign servers.

### pg_catalog.pg_database details
this docs can be found in [https://www.postgresql.org/docs/16/catalog-pg-database.html](https://www.postgresql.org/docs/16/catalog-pg-database.html)

| Column Name          | Type        | Description                                                                                                   |
| -------------------- | ----------- | ------------------------------------------------------------------------------------------------------------- |
| **`datname`**        | `name`      | The name of the database.                                                                                     |
| **`datdba`**         | `oid`       | The OID of the role (user) that owns the database. Use `pg_get_userbyid(datdba)` to resolve it.               |
| **`encoding`**       | `int`       | The character encoding of the database (e.g., UTF8 = 6). Use `pg_encoding_to_char(encoding)` to get the name. |
| **`datlocprovider`** | `char`      | Locale provider used (`c` = libc, `i` = ICU).                                                                 |
| **`datistemplate`**  | `bool`      | If `true`, the database can be used as a template for `CREATE DATABASE ... TEMPLATE`.                         |
| **`datallowconn`**   | `bool`      | If `false`, connections to this database are not allowed (except by superusers).                              |
| **`datconnlimit`**   | `int`       | The maximum number of concurrent connections allowed (-1 = no limit).                                         |
| **`datlastsysoid`**  | `oid`       | The last system OID used in this database at creation (mainly historical).                                    |
| **`datfrozenxid`**   | `xid`       | The transaction ID at which all tuples are known to be frozen (related to VACUUM).                            |
| **`datminmxid`**     | `xid`       | The minimum multixact ID that is still considered potentially unfrozen.                                       |
| **`dattablespace`**  | `oid`       | OID of the default tablespace for the database. Use `pg_tablespace` to resolve.                               |
| **`datcollate`**     | `name`      | LC\_COLLATE setting (how strings are sorted).                                                                 |
| **`datctype`**       | `name`      | LC\_CTYPE setting (how character classification works).                                                       |
| **`daticulocale`**   | `text`      | ICU locale (used if `datlocprovider = 'i'`).                                                                  |
| **`datcollversion`** | `text`      | Version of the collation used (important for collation versioning with ICU).                                  |
| **`datacl`**         | `aclitem[]` | Access privileges (GRANTs), stored as an array of ACL items.                                                  |


## management script collection

#### - show all databases (in current user)
```sql
SELECT * FROM pg_catalog.pg_database;`:
```
#### - show `pg_catalog.pg_tables` definition

go back on top in order to see what actually view is
```sql
SELECT pg_get_viewdef('pg_catalog.pg_tables', true);`: 
```

#### - show all available pgsql datatype
```sql
SELECT 
	*
FROM
	pg_catalog.pg_type;
```

#### - lists all schema
```sql
SELECT
    *
FROM
    pg_catalog.pg_namespace;
```

#### - show all dbs with owner

```sql
SELECT 
        x.oid as object_id,
        x.datname as db_name,
        CASE 
                WHEN pg_catalog.pg_get_userbyid(x.datdba) LIKE 'unknown (OID=%)' THEN 'UNKNOWN'
                ELSE pg_catalog.pg_get_userbyid(x.datdba)
        END as owner
FROM pg_catalog.pg_database as x;
```

cond: [https://www.postgresql.org/docs/current/functions-conditional.html#FUNCTIONS-CASE](https://www.postgresql.org/docs/current/functions-conditional.html#FUNCTIONS-CASE)

#### - RENAME db (as postgres user)
```sql
ALTER DATABASE xyz RENAME TO abc;
```