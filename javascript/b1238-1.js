var input = require("fs").readFileSync("stdin", "utf8");
var lines = input.split('\n');

let N = Number(lines.shift());

for (let i = 0; i < N; i++) {
  let string = lines.shift().replace('\r', '').split(' '),
      string1 = string[0], 
      string2 = string[1],
      maiorString = string1.length > string2.length ? string1 : string2,
      menorString = string2.length < string1.length ? string2 : string1;

  let sen = "";
  for (let j = 0; j < maiorString.length; j++) {
    if (j >= menorString.length) { 
      sen += maiorString[j];
    } else { 
      sen += string1[j] + string2[j];
    }
  }
  console.log(sen);
}