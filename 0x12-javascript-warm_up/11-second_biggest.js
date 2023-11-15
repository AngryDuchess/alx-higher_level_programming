#!/usr/bin/node

const args = process.argv.slice(2);
const toNumber = args.map(Number);
if (args.length <= 1) {
  console.log('0');
} else {
  /* const toNumber = args.map(Number); */
  const sortedNum = toNumber.sort((a, b) => b - a);
  console.log(sortedNum[1]);
}
