---
created: 2024-05-06 20:31:11-07:00
title: node-csv
updated: 2024-05-06 20:35:35-07:00
---

## Summary

Suite of [CSV](CSV.md) processing libraries for [Node.js](Node.js.md)

## Components

### `csv-generate`

 > 
 > a flexible generator of CSV string and JavaScript objects

### `csv-parse`

[CSV Parse - Usage](https://csv.js.org/parse/)

 > 
 > a parser converting CSV text into arrays or objects

Multiple APIs:

* Stream API
* Callback API
* Stream + callback API
* Sync API
* Async iterator API

#### Interesting Constructor Options

````javascript
on_record: (record, context): Record? => {}
````

for row transformation and filtering

````javascript
info: boolean
````

if true, `parse()` produces an object with `record` and `info` properties. Sounds like that means it parses the whole thing rather than parts in async.

### `csv-stringify`

[CSV Stringify - Usage](https://csv.js.org/stringify/)

`columns: array | object`

````javascript
import { stringify } from 'csv-stringify';
import assert from 'assert';

stringify([
  { a: '1', b: '2' }
], {
  columns: [ { key: 'a' }, { key: 'b' } ]
}, function(err, data){
  assert.equal(data, '1,2\n');
});
````

### `string-transform`

 > 
 > a transformation framework

[CSV Transform - Usage](https://csv.js.org/transform/)