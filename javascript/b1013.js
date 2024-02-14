var input = require("fs").readFileSync("stdin", "utf8");

var values = input.split(" ");

var a = parseInt(values.shift());
var b = parseInt(values.shift());
var c = parseInt(values.shift());

var maiorAB = ((a + b + Math.abs(a - b))/2);
var maiorABC = ((maiorAB + c + Math.abs(maiorAB - c))/2);

console.log(maiorABC + " eh o maior");