#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
  process.exit();
}

const numbers = args.map(Number);
numbers.sort((a, b) => b - a);

console.log(numbers[1]);
