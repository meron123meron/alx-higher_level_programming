#!/usr/bin/node
const l = process.argv.length;
if (l <= 3) {
  console.log(0);
} else {
  const a = process.argv.map(Number)
    .slice(2, l)
    .sort((a, b) => a - b);
  console.log(a[a.length - 2]);
}
