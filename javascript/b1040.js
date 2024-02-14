var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split(/[\s\n]+/);

let n1 = parseFloat(valores.shift());
let n2 = parseFloat(valores.shift());
let n3 = parseFloat(valores.shift());
let n4 = parseFloat(valores.shift());

let media = (n1*2 + n2*3 + n3*4 + n4*1)/ 10;
console.log("Media: " + media.toFixed(1));

if (media >= 7) {
  console.log("Aluno aprovado.");
} else if (media < 5) {
  console.log("Aluno reprovado.");
} else {
  console.log("Aluno em exame.");

  let ex = parseFloat(valores.shift());
  console.log("Nota do exame: " + ex.toFixed(1));

  media = (media + ex)/ 2;

  if (media >= 5) {
    console.log("Aluno aprovado.");
  } else {
    console.log("Aluno reprovado.");
  }
  console.log("Media final: " + media.toFixed(1));
}
