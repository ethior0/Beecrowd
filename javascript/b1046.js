var input = require("fs").readFileSync("stdin", "utf8");

var values = input.split(" ");

let start = parseInt(values.shift());
let end = parseInt(values.shift());

let hour;

if (start == end) {
  console.log("O JOGO DUROU 24 HORA(S)");
} else if (start < end) {
  hour = end - start;
  console.log("O JOGO DUROU " + hour + " HORA(S)");
} else if (start > end) {
  hour = (end + 24) - start;
  console.log("O JOGO DUROU " + hour + " HORA(S)");
}
