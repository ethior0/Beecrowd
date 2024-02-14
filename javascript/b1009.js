var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split("\n");

var nome = valores.shift();
var salario = parseFloat(valores.shift());
var produtos = parseFloat(valores.shift());

var salarioFinal = salario + (0.15 * produtos);

console.log("TOTAL = R$ " + salarioFinal.toFixed(2))