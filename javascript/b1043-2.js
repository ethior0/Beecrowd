var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split(" ");

let A = parseFloat(valores.shift());
let B = parseFloat(valores.shift());
let C = parseFloat(valores.shift());

let p = A + B + C;
let a = (A + B) * C / 2;

if (A<(B+C) && B<(A+C) && C<(A+B)) {
  console.log("Perimetro = " + p.toFixed(1));
} else {
  console.log("Area = " + a.toFixed(1));
}