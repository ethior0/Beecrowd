var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split(" ");

let A = parseFloat(valores.shift());
let B = parseFloat(valores.shift());
let C = parseFloat(valores.shift());

let maior = Math.max(A, B);
maior = Math.max(maior, C);
if (maior == C) {
  C = A;
  A = maior;
} else if (maior == B) {
  B = A;
  A = maior;
}

let Aq = Math.pow(A, 2);
let BC = B + C;
let BCq = Math.pow(B, 2) + Math.pow(C, 2);


if (A >= BC) {
  console.log("NAO FORMA TRIANGULO");
} else {
  if (Aq == BCq) {
    console.log("TRIANGULO RETANGULO");
  } else if (Aq > BCq) {
    console.log("TRIANGULO OBTUSANGULO");
  } else if (Aq < BCq) {
    console.log("TRIANGULO ACUTANGULO");
  }
    if (A == B && B == C) {
    console.log("TRIANGULO EQUILATERO");
  } else if (A == B ^ B == C ^ C == A) {
    console.log("TRIANGULO ISOSCELES")
  }
}


