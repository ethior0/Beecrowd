var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split(" ");

let A = parseFloat(valores.shift());
let B = parseFloat(valores.shift());
let C = parseFloat(valores.shift());

let d = Math.pow(B, 2) -4 * A * C;
let r1 = (-B + Math.sqrt(d))/ (2 * A);
let r2 =  (-B - Math.sqrt(d))/ (2 * A);

if (A == 0 || d < 0) {
  console.log("Impossivel calcular");
} else {
  console.log("R1 = " + r1.toFixed(5));
  console.log("R2 = " + r2.toFixed(5));
}



