var input = require("fs").readFileSync("stdin", "utf8");

var valor = parseInt(input);

var seg = parseInt (valor % 60);
var min = valor / 60;
var mins = parseInt (min % 60);
var hora = parseInt(valor / 3600);

console.log(hora+":"+mins+":"+seg);


