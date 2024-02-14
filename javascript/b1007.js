var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split("\n");

var A = parseInt(valores.shift());
var B = parseInt(valores.shift());
var C = parseInt(valores.shift());
var D = parseInt(valores.shift());

var PROD1 = A * B;
var PROD2 = C * D;
var DIF = PROD1 - PROD2;

console.log("DIFERENCA = " + DIF);