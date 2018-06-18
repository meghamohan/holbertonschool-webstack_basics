#!/usr/bin/node
const a = process.argv.slice(2);
if (a.length <= 1) {
  console.log(0);
} else {
  a.sort();
  console.log(a[a.length - 2]);
}
