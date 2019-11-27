# _PostgreSQL_ OMG Microservice

> Interact with a Postgres database.

[![Open Microservice Specification Version](https://img.shields.io/badge/Open%20Microservice-1.0-477bf3.svg)](https://openmicroservices.org)
[![Open Microservices Spectrum Chat](https://withspectrum.github.io/badge/badge.svg)](https://spectrum.chat/open-microservices)
[![Open Microservices Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](https://github.com/oms-services/.github/blob/master/CODE_OF_CONDUCT.md)
[![Open Microservices Commitzen](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Direct usage in [Storyscript](https://storyscript.io/):

### Create table

A table can be created with `createTable`:

```coffee
psql createTable table: "books" columns: {
  "id": "serial primary key",
  "title": "varchar(100)"
}
```

### Insert an entry

```coffee
psql insert table: "books" values: {"title": "Ulysses"}
# result: {"id": 1, "title": "Ulysses"}
```

### Insert multiple entries

```coffee
psql insert table: "books" values: [{"title": "Moby Dick"}, {"title": "War and Peace"}]
# result: [{"id": 2, "title": "Ulysses"}, {"id": 3, "title": "War and Peace"}]
```

### Select entries

- `$and` and `$or` can be used to combine queries
- `$lt`, `$lte`, `$gt`, `$gte` and `$eq` can be used as comparison operators
- if no comparison operators is provided, the query will match on equality
- `columns` can be used to filter the selected fields

```coffee
psql select table: "books" where: {"title": "Moby Dick"}
# result: [{"id": 2, "title": "Moby Dick"}]
```

```coffee
psql select table: "books" where: {"$or": {title: "Moby Dick", "id": {"$lt": 2}}}
# result: [{"id": 1, "title": "Ulysses"}, {"id": 2, "title": "Moby Dick"}]
```

```coffee
psql select table: "books" columns: ["title"] where: {"title": "Moby Dick"}
# result: [{"title": "Moby Dick"}]
```

### Update entries

```coffee
psql update table: "books" values: {"title": "UPDATED"} where: {"id": {"$gt": 2}}
# result: [{"id": 3, "title": "UPDATED"}]
```

The where query is optional, but without it _all_ columns will be updated:

```coffee
psql update table: "books" values: {"title": "UPDATED"}
# result: [
#     {"id": 1, "title": "Ulysses"},
#     {"id": 2, "title": "Ulysses"},
#     {"id": 3, "title": "War and Peace"}
# ]
```

### Delete entries

`delete` uses a `where` select query and will return the deleted columns:

```coffee
psql delete table: "books" where: {"title": "Moby Dick"}
# result: [{"id": 2, "title": "Moby Dick"}]
```

The where query is optional, but without it _all_ rows will be deleted.

### Drop table

An entire table can be dropped with `dropTable`:

```coffee
psql dropTable table: "books"
```

### Execute

```storyscript
# Storyscript
result = psql exec query: "select * from my_table where name=%(username)s" data: {"username": "jill"}
# result is an array, with records as JSON objects inside it.
```

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMS CLI](https://www.npmjs.com/package/@microservices/oms)

##### Create Table

```shell
oms run createTable -a table=<TABLE_NAME> -a columns=<COLUMNS_DATA> -e POSTGRES_DSN=<POSTGRES_DSN>
```

##### Drop Table

```shell
oms run dropTable -a table=<TABLE_NAME> -e POSTGRES_DSN=<POSTGRES_DSN>
```

##### Insert

```shell
oms run insert -a table=<TABLE_NAME> -a values=<MAP/LIST_OF_MAP_VALUES> -e POSTGRES_DSN=<POSTGRES_DSN>
```

##### Select

```shell
oms run select -a table=<TABLE_NAME> -a where=<WHERE_CONDITION> -e POSTGRES_DSN=<POSTGRES_DSN>
```

##### Update

```shell
oms run update -a table=<TABLE_NAME> -a values=<MAP/LIST_OF_MAP_VALUES> -a where=<WHERE_CONDITION> -e POSTGRES_DSN=<POSTGRES_DSN>
```

##### Delete

```shell
oms run delete -a table=<TABLE_NAME> -a where=<WHERE_CONDITION> -e POSTGRES_DSN=<POSTGRES_DSN>
```

##### Execute

```shell
oms run exec -a query=<QUERY> -a data=<DATA_FOR_QUERY_FIELDS> -e POSTGRES_DSN=<POSTGRES_DSN>
```

## License

[MIT License](https://github.com/oms-services/psql/blob/master/LICENSE).
