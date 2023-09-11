var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split("\n");

var valor1 = parseFloat(valores.shift());
var valor2 = parseFloat(valores.shift());

var MEDIA = ((valor1*3.5) + (valor2*7.5))/11

console.log("MEDIA = " + MEDIA.toFixed(5))