# Asyncy Postgres

This container should be used for raw psql access.
The output is not parsed into json format.

#### Example

```storyscript
# Storyscript
result = psql -c "select true"
```

The result is the raw output from Postgres.
