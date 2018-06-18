#!/usr/bin/node
const a = process.argv.slice(2);
const fs = require('fs');
fs.readFile(args[0], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
    process.exit(1);
  }


  const d1 = data;
  fs.readFile(args[1], 'utf8', function (err, data) {
    if (err) {
      console.log(err);
      process.exit(1);
    }


    const d2 = data;
    fs.writeFile(args[2], d1 + d2, function (err) {
      if (err) {
        console.log(err);
        process.exit(1);
      }
    });
  });
});
