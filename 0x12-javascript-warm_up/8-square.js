#!/usr/bin/node
const n = Math.floor(Number(process.argv[2]));
if (isNaN(n)) {
  console.log('Missing size');
}
for (let i = 0; i < n; i++) {
  let r = '';
  for (let j = 0; j < n; j++) {
    r = r + 'x';
  }
  console.log(r);
}
