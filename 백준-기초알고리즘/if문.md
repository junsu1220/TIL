## 1330 두 수 비교하기
- 출처 : https://www.acmicpc.net/problem/1330
- 코드 : 
```javascript
const fs = require("fs")
const inputData = fs.readFileSync("/dev/stdin").toString().split(" ").map(val=>+val)
const [a,b] = inputData

if (a > b){
    console.log(">")
}
else if (a < b){
    console.log("<")
}
else {
    console.log("==")
}
```
- 참고 : https://silverlibrary.tistory.com/231

## 9498 시험성적
- 출처 : https://www.acmicpc.net/problem/9498
- 코드 : 
```javascript
const fs = require('fs')
const inputData = fs.readFileSync("/dev/stdin")
const a = inputData;
if(a>=90 && a<=100){
    console.log('A');
}
else if(a>=80 && a<=89){
    console.log('B');
}
else if(a>=70 && a<=79){
    console.log('C');
}
else if(a>=60 && a<=69){
    console.log('D');
}
else{
    console.log('F');
}
```

## 2753 윤년
- 출처 : https://www.acmicpc.net/problem/2753
- 코드 :

```javascript
const fs = require("fs")
const inputData = fs.readFileSync("/dev/stdin").toString().split(" ").map(val=>+val)

const a = inputData;
if(a%4===0 && (a%100!==0 || a%400===0)){
    console.log(1)
}
else{
    console.log(0)
}
```

## 14681 사분면 고르기
- 출처 : https://www.acmicpc.net/problem/14681
- 코드 : 
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];

rl.on("line", function (line) {
  input.push(parseInt(line));
}).on("close", function () {
  ///////////////////////////////
  const a = input[0];
  const b = input[1];
  ///////////////////////////////
if(a > 0 && b > 0){
    console.log("1");
}
else if(a < 0 && b > 0){
    console.log("2");
}
else if(a < 0 && b < 0){
    console.log("3");
}
else if(a > 0 && b < 0){
    console.log("4");
}
//////////////////////////////
    process.exit();
});

## 2884 알람시계
- 출처 : https://www.acmicpc.net/problem/2884
- 코드 : 

```javascript
let input = require('fs').readFileSync('dev/stdin').toString().split(' ');

let Hour = Number(input[0]);  // Hour
let Minute = Number(input[1]);  // Minute

Minute -= 45;

if (Minute < 0) {
    Minute += 60;
    Hour--;

    if (Hour === -1) {
        Hour = 23;
    }
}

console.log(Hour + ' ' + Minute);
```

- 참고 : https://gurtn.tistory.com/20
