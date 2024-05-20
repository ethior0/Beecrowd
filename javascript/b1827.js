var input = require("fs").readFileSync("stdin", "utf8");
var lines = input.trim().split('\n');

while (lines.length) {
  const size = parseInt(lines.shift());
  let aux1 = 0, aux2 = size - 1;

  for (let i = 0; i < size; i++) {
    let input = "";
    for (let j = 0; j < size; j++) {
      const sqr = Math.trunc(size / 3);
      if (i >= sqr && i < size - sqr && j >= sqr && j < size - sqr) {
        if (i === (size - 1) / 2 && j === (size - 1) / 2) input += "4";
        else input += "1";
      } else {
        if (j === aux1) input += "2";
        else if (j === aux2) input += "3";
        else input += "0";
      }
    }
    aux1++, aux2--;
    console.log(input);
  }
  console.log();
}
