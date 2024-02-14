var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

let N = Number(lines.shift());

for (let i = 0; i < N; i++) {
  let linha = lines.shift().replace('\r', '').split(' '),
      string1 = linha[0], 
      string2 = linha[1];

  let sen = "";
  for (let j = 0; j < string1.length + string2.length; j++) {
    sen += string1[j] + string2[j];
  }
  // solução porca, mas é uma das possibilidades rs
  console.log(sen.replace(/undefined/g, '').replace(/NaN/g, ''));
}