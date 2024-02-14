var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split(" ");

let A = parseInt(valores.shift());
let B = parseInt(valores.shift());
let C = parseInt(valores.shift());
let D = parseInt(valores.shift());

let CD = C + D;
let AB = A + B;

if (B > C && D > A && CD > AB && C>0 && D>0 && A%2 == 0) {
  console.log("Valores aceitos");
} else {
  console.log("Valores nao aceitos");
}