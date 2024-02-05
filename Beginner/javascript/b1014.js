var input = require("fs").readFileSync("stdin", "utf8");

var values = input.split("\n");

var distance = parseInt(values.shift());
var fue = parseFloat(values.shift());

var consumption = distance / fue;

console.log(consumption.toFixed(3) + " km/l");