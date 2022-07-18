```jsx
function solution(x, n) {
        let answer = [];
        let add = 0;
        for (let i = 0; i < n; i++) {
          add += x;
          answer.push(add);
          console.log(answer);
        }
        return answer;
      }
      // for문을 이용해 배열에 주어진 숫자를 push하고
      // 그 수를 더해서 다시 넣는다.
      // n번 반복한다.
      console.log(solution(2, 5));
      // function solution(x, n) {
      //   var answer = [];
      //   for (let i = 1; i <= n; i++) {
      //     answer.push(x * i);
      //   }
      //   return answer;
      // }
```
