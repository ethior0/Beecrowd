var input = require("fs").readFileSync("stdin", "utf8");

var values = input.split(" ");

var A = parseFloat(values.shift());
var B = parseFloat(values.shift());
var C = parseFloat(values.shift());

var PI = 3.14159;

var triangle = A * C / 2;
var circle = Math.pow(C, 2) * PI;
var trapezium = (A + B) * C / 2;
var square = B * B;
var rectangle = A * B;

console.log("TRIANGULO: " + triangle.toFixed(3));
console.log("CIRCULO: " + circle.toFixed(3));
console.log("TRAPEZIO: " + trapezium.toFixed(3));
console.log("QUADRADO: " + square.toFixed(3));
console.log("RETANGULO: " + rectangle.toFixed(3));