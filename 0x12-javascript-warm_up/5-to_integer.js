#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
if (typeof num === 'number') {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
