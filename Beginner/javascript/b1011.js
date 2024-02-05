var input = require("fs").readFileSync("stdin", "utf8");

var raio = parseFloat(input);

var PI =  3.14159;
var volume = (4/3) * PI * Math.pow(raio, 3);

console.log("VOLUME = " + volume.toFixed(3));