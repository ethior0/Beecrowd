var input = require("fs").readFileSync("stdin", "utf8");

var values = input.split("\n");

var time = parseInt(values.shift());
var speed = parseInt(values.shift());

var distance = time * speed;
var fuel = distance / 12;

console.log(fuel.toFixed(3));