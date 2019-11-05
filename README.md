# _PostgreSQL_ OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)

Interact with a Postgres database.

## Direct usage in [Storyscript](https://storyscript.io/):

### Create table

A table can be created with `createTable`:

```coffee
psql createTable table: 'books' columns: {
  'id': 'serial primary key',
  'title': 'varchar(100)'
}
```

### Insert an entry

```coffee
psql insert table: 'books' values: {'title': 'Ulysses'}
# result: {'id': 1, 'title': 'Ulysses'}
```

### Insert multiple entries

```coffee
psql insert table: 'books' values: [{'title': 'Moby Dick'}, {'title': 'War and Peace'}]
# result: [{'id': 2, 'title': 'Ulysses'}, {'id': 3, 'title': 'War and Peace'}]
```

### Select entries

- `$and` and `$or` can be used to combine queries
- `$lt`, `$lte`, `$gt`, `$gte` and `$eq` can be used as comparison operators
- if no comparison operators is provided, the query will match on equality
- `columns` can be used to filter the selected fields

```coffee
psql select table: 'books' where: {'title': 'Moby Dick'}
# result: [{'id': 2, 'title': 'Moby Dick'}]
```

```coffee
psql select table: 'books' where: {'$or': {title: 'Moby Dick', 'id': {'$lt': 2}}}
# result: [{'id': 1, 'title': 'Ulysses'}, {'id': 2, 'title': 'Moby Dick'}]
```

```coffee
psql select table: 'books' columns: ['title'] where: {'title': 'Moby Dick'}
# result: [{'title': 'Moby Dick'}]
```

### Update entries

```coffee
psql update table: 'books' values: {'title': 'UPDATED'} where: {'id': {'$gt': 2}}
# result: [{'id': 3, 'title': 'UPDATED'}]
```

The where query is optional, but without it _all_ columns will be updated:

```coffee
psql update table: 'books' values: {'title': 'UPDATED'}
# result: [
#     {'id': 1, 'title': 'Ulysses'},
#     {'id': 2, 'title': 'Ulysses'},
#     {'id': 3, 'title': 'War and Peace'}
# ]
```

### Delete entries

`delete` uses a `where` select query and will return the deleted columns:

```coffee
psql delete table: 'books' where: {'title': 'Moby Dick'}
# result: [{'id': 2, 'title': 'Moby Dick'}]
```

The where query is optional, but without it _all_ rows will be deleted.

### Drop table

An entire table can be dropped with `dropTable`:

```coffee
psql dropTable table: 'books'
```

### Execute

```storyscript
# Storyscript
result = psql exec query: 'select * from my_table where name=%(username)s' data: {'username': 'jill'}
# result is an array, with records as JSON objects inside it.
```

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### Create Table
```shell
$ omg run createTable -a table=<TABLE_NAME> -a columns=<COLUMNS_DATA> -e POSTGRES_DSN=<POSTGRES_DSN>
```
##### Drop Table
```shell
$ omg run dropTable -a table=<TABLE_NAME> -e POSTGRES_DSN=<POSTGRES_DSN>
```

##### Insert
```shell
$ omg run insert -a table=<TABLE_NAME> -a values=<MAP/LIST_OF_MAP_VALUES> -e POSTGRES_DSN=<POSTGRES_DSN>
```

##### Select
```shell
$ omg run select -a table=<TABLE_NAME> -a where=<WHERE_CONDITION> -e POSTGRES_DSN=<POSTGRES_DSN>
```

##### Update
```shell
$ omg run update -a table=<TABLE_NAME> -a values=<MAP/LIST_OF_MAP_VALUES> -a where=<WHERE_CONDITION> -e POSTGRES_DSN=<POSTGRES_DSN>
```

##### Delete
```shell
$ omg run delete -a table=<TABLE_NAME> -a where=<WHERE_CONDITION> -e POSTGRES_DSN=<POSTGRES_DSN>
```

##### Execute
```shell
$ omg run exec -a query=<QUERY> -a data=<DATA_FOR_QUERY_FIELDS> -e POSTGRES_DSN=<POSTGRES_DSN>
```


**Note**: the OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/psql/blob/master/LICENSE).
