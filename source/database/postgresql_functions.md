# pgsql functions()

### `pg_get_viewdef`
see sql script for particular view, I call this as view reverser

example: 
```sql
SELECT
        *
FROM
        pg_get_viewdef('pg_catalog.pg_sequences', true)
```

ref:
- [https://pgpedia.info/p/pg_get_viewdef.html](https://pgpedia.info/p/pg_get_viewdef.html)
- [https://www.postgresql.org/docs/current/functions-info.html](https://www.postgresql.org/docs/current/functions-info.html)

### akan ada kelanjutan disini.