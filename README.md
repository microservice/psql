# Asyncy Postgres

This container should be used for raw psql access.
The output is always returned in JSON format.

#### Example

```storyscript
# Storyscript
result = psql exec query: 'select * from my_table where name=%(username)s' data: {'username': 'jill'}
# result is an array, with records as JSON objects inside it.
```
