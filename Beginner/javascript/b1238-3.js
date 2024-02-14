var input = require("fs").readFileSync("stdin", "utf8");
var lines = input.split('\n');

let N = Number(lines.shift());

for (let i = 0; i < N; i++) {
  let string = lines.shift().replace('\r', '').split(' '),
      string1 = string[0], 
      string2 = string[1],
      maxLength = Math.max(string1.length, string2.length);

  let sen = "";
  for (let j = 0; j < maxLength; j++) {
    if (string1[j]) sen += string1[j];
    if (string2[j]) sen += string2[j];
  }
  console.log(sen);
}