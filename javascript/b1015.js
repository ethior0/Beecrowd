var input = require("fs").readFileSync("stdin", "utf8");

var values = input.split(/[\s\n]+/)

var x1 = parseFloat(values.shift());
var y1 = parseFloat(values.shift());
var x2 = parseFloat(values.shift());
var y2 = parseFloat(values.shift());

var sub1 = x2 - x1;
var sub2 = y2 - y1;

var pow1 = Math.pow(sub1, 2);
var pow2 = Math.pow(sub2, 2);
var distance = Math.sqrt(pow1 + pow2);

console.log(distance.toFixed(4));
