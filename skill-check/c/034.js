process.stdin.resume();
process.stdin.setEncoding('utf8');
// 自分の得意な言語で
// Let's チャレンジ！！

var lines = [];
var reader = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
reader.on('line', (line) => {
  lines.push(line.split(' '));
});
reader.on('close', () => {
    const a = lines[0][0];
    const op = lines[0][1];
    const b = lines[0][2];
    const c = lines[0][4];
    
    let x = 0;
    
    if (op === "+") {
        if (a === "x") {
            x = Number(c) - Number(b);
        } else if (b === "x") {
            x = Number(c) - Number(a);
        } else {
            x = Number(a) + Number(b);
        }

    } else if (op === "-") {
        if (a === "x") {
            x = Number(b) + Number(c);
        } else if (b === "x") {
            x = Number(a) - Number(c);
        } else {
            x = Number(a) - Number(b);
        }
        
    }
    console.log(x);
});