#!/usr/bin/node
const fs = require('fs');
const myFile = process.argv[2];
const txt = process.argv[3];
fs.appendFile(myFile, txt, {encoding: 'utf8'}, function (err, data) {
  if (err) {
    console.log(err);
  }
});
