#!/usr/bin/node
const n = Number(process.argv[2]);
if (isNaN(n)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < n; i++) {
  console.log('C is fun');
}
