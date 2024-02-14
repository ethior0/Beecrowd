var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split(" ");

let A = parseFloat(valores.shift());
let B = parseFloat(valores.shift());
let C = parseFloat(valores.shift());

let maior = Math.max(A, B)
    maior = Math.max(maior, C);
let menor1 = 0;
let menor2 = 0;

if (maior == A) {
  menor1 = B;
  menor2 = C;
} else if (maior == B) {
  menor1 = A;
  menor2 = C;
} else {
  menor1 = A;
  menor2 = B;
}

if (maior > Math.abs(menor1 - menor2) && maior < (menor1 + menor2)) {
  let perimetro = A + B + C;
  console.log("Perimetro = " + perimetro.toFixed(1));
} else {
  let trapezio = (A + B) * C / 2;
  console.log("Area = " + trapezio.toFixed(1))
}