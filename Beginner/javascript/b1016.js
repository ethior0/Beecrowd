var input = require("fs").readFileSync("stdin", "utf8");

var value = input;

var km = parseInt(input);
var minutes = km * 2;

console.log(minutes + " minutos");