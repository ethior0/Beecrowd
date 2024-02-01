var input = require("fs").readFileSync("stdin", "utf8");

var values  = input.split("\n");

var number = parseInt(values.shift());
var hour = parseInt(values.shift());
var perHour = parseFloat(values.shift());

var salary = hour * perHour;

console.log("NUMBER = " + number);
console.log("SALARY = U$ " + salary.toFixed(2))