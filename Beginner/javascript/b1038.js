var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split(" ");

var code = parseInt(valores.shift());
var qtd = parseInt(valores.shift());
let preco;

switch(code) {
  case 1:
    preco = qtd * 4.00;
    break;
  case 2:
    preco = qtd * 4.50;
    break;
  case 3:
    preco = qtd * 5;
    break;
  case 4:
    preco = qtd * 2
    break;
  case 5:
    preco = qtd * 1.5
    break;
}

console.log("Total: R$ " + preco.toFixed(2));