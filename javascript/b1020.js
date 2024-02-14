var input = require("fs").readFileSync("stdin", "utf8");

var dias = parseInt(input);

var ano = parseInt(dias / 365);
var resto = dias % 365;
var mes = parseInt(resto / 30);
var dia = parseInt (resto % 30);

console.log(ano + " ano(s)");
console.log(mes + " mes(es)");
console.log(dia + " dia(s)");