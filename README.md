# Asyncy Postgres

Interact with a Postgres database.

Examples
-------

### Create table

A table can be created with `create_table`:

```coffee
# Storyscript
psql create_table table: 'books' columns: {
  'id': 'serial primary key',
  'title': 'varchar(100)'
}
```

### Insert an entry

```coffee
# Storyscript
psql insert table: 'books' values: {'title': 'Ulysses'}
# result: {'id': 1, 'title': 'Ulysses'}
```

### Insert multiple entries

```coffee
# Storyscript
psql insert table: 'books' values: [{'title': 'Moby Dick'}, {'title': 'War and Peace'}]
# result: [{'id': 2, 'title': 'Ulysses'}, {'id': 3, 'title': 'War and Peace'}]
```

### Select entries

- `$and` and `$or` can be used to combine queries
- `$lt`, `$lte`, `$gt`, `$gte` and `$eq` can be used as comparison operators
- if no comparison operators is provided, the query will match on equality

```coffee
# Storyscript
psql select table: 'books' where: {'title': 'Moby Dick'}
# result: [{'id': 2, title: 'Moby Dick'}]
```

```coffee
# Storyscript
psql select table: 'books' where: {'$or': {title: 'Moby Dick', 'id: {'$lt': 2}}}
# result: [{'id': 1, 'title': 'Ulysses'}, {'id': 2, title: 'Moby Dick'}]
```

### Update entries

```coffee
# Storyscript
psql update table: 'books' values: {'title': 'UPDATED'} where: {'id': {'$gt': 2}}
# result: [{'id': 3, title: 'UPDATED'}]
```

The where query is optional, but without it _all_ columns will be updated:

```coffee
# Storyscript
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
# Storyscript
psql delete table: 'books' where: {'title': 'Moby Dick'}
# result: [{'id': 2, title: 'Moby Dick'}]
```

The where query is optional, but without it _all_ columns will be deleted.

### Drop table

An entire table can be dropped with `drop_table`:

```coffee
# Storyscript
psql drop_table table: 'books'
```

### Execute

```storyscript
# Storyscript
result = psql exec query: 'select * from my_table where name=%(username)s' data: {'username': 'jill'}
# result is an array, with records as JSON objects inside it.
```
