var input = require("fs").readFileSync("stdin", "utf8");

var raio = parseFloat(input);
var PI = 3.14159;

var area = Math.pow(raio, 2) * PI;

console.log("A=" + area.toFixed(4));