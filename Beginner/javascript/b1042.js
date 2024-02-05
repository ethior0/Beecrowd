var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split(" ");

let A = parseInt(valores.shift());
let B = parseInt(valores.shift());
let C = parseInt(valores.shift());

let min1, min2 = 0, min3 = 0;

min1 = Math.min(A, Math.min(B, C));

if (min1 == A) {
  min2 = Math.min(B, C);
  min3 = Math.max(B, C);
}
if (min1 == B) {
  min2 = Math.min(A, C);
  min3 = Math.max(A, C);
}
if (min1 == C) {
  min2 = Math.min(A, B);
  min3 = Math.max(A, B);
}
console.log(min1);
console.log(min2);
console.log(min3);
console.log();
console.log(A);
console.log(B);
console.log(C);