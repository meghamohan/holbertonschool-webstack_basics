#!/usr/bin/node
const lst1 = require('./100-data.js').list;
let lst2 = [];
let n = 0;
console.log(lst1);
lst1.map(elem => {
  lst2.push(elem * n);
  n++;
});
console.log(lst2);
