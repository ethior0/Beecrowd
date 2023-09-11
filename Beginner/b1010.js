var input = require("fs").readFileSync("stdin", "utf8");

var values = input.split(/[\s\n]+/);

var code1 = parseInt(values.shift());
var unit1 = parseInt(values.shift());
var uPrice1 = parseFloat(values.shift());

var code2 = parseInt(values.shift());
var unit2 = parseInt(values.shift());
var uPrice2 = parseFloat(values.shift());

var price = (unit1*uPrice1) + (unit2*uPrice2);

console.log("VALOR A PAGAR: R$ " + price.toFixed(2));
