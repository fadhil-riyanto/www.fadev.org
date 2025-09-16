# Postgresql II SQL language docs summary

this is incomplete documentation summary of postgresql (SQL section), see complete docs [here](https://www.postgresql.org/docs/current/sql.html)

## 5. Data Definition
### 5.2. Default values

When a new row is created and no values are specified for some of the columns, those columns will be filled with their respective default values. A data manipulation command can also request explicitly that a column be set to its default value, without having to know what that value is

example

```sql
CREATE TABLE state (
	uid				integer,
	enable			bool DEFAULT false
)
```

### 5.3. Identity column