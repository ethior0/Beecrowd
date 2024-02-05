var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split(" ");

let A = parseInt(valores.shift());
let B = parseInt(valores.shift());

if (A % B == 0 || B % A == 0 ) {
  console.log("Sao Multiplos");
} else {
  console.log("Nao sao Multiplos");
}