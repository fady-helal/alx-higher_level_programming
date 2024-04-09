#!/usr/bin/node
function secondbigest (arr) {
    let max = -Infinity;
    let result = -Infinity;
    for (const value of arr) {
      const nr = Number(value);
  
      if (nr > max) {
        [result, max] = [max, nr]; // save previous max
      } else if (nr < max && nr > result) {
        result = nr; // new second biggest
      }
    }
  
    console.log(result);
  }
if (process.argv.length <= 3) {
  console.log(0);
}
else{
const args = [];
for (let i = 0; i < (Number(process.argv.length)); i++) {
  args[i] = Number(process.argv[i]);
}secondbigest(args);
}
