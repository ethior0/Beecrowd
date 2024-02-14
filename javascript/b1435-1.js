var input = require("fs").readFileSync("stdin", "utf8");

var valor = input.split("\n");

let t = valor.length;
let x;
let linha = "";

for (let cc = 0; cc < t; cc++) {
  for (let i = 1; i <= valor[cc]; i++) {
    for (let j = 1; j<= valor[cc]; j++) {
      x = i;
  
      if (j < x) {
        x = j;
      }
      if (valor[cc] - i + 1 < x) {
        x = valor[cc] - i + 1;
      }
      if (valor[cc] - j + 1 < x) {
        x = valor[cc] - j + 1;
      }
      linha += "  " + x;
      if (j < valor[cc]) {
        linha += " ";
      } else {
        console.log(linha)
        linha = "";
      }
    }
  }
  if (cc != t-1) {
    console.log("");
  } 
}
