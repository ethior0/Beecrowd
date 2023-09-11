var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split("\n");

var valor1 = parseInt(valores.shift());
var valor2 = parseInt(valores.shift());

var SOMA = valor1 + valor2;

console.log("SOMA = " + SOMA);