```jsx
function solution(s) {
        let answer = true;
        let p_cnt = 0;
        let y_cnt = 0;
        s = s.toLowerCase();
        for (let x of s) {
          if (x === "p") p_cnt++;
          else if (x === "y") y_cnt++;
        }
        if (p_cnt !== y_cnt) answer = false;
        return answer;
      }
      // 변수 p_cnt와 y_cnt를 만든다.
      // 반복문을 이용해 하나씩 toLowerCase()로 봐서 p이면 p_cnt
      // y이면 y_cnt를 ++해주고 반복이 끝나면 둘을비교해
      // 다르다면 answer를 false로 바꿔준다.
      console.log(solution("pPoooyY"));
```
