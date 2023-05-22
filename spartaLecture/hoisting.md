# 글의 목적

- 면접하듯이 외워서 대답해야할 수 있게 정리한다.

# 레퍼런스

[[JavaScript] 호이스팅(Hoisting)과 시간상 사각지대(Temporal Dead Zone, TDZ)](https://any-ting.tistory.com/135)

[자바스크립트를 배우는데 아직도 let과 var의 차이를 모른다고? : 호이스팅](https://www.youtube.com/watch?v=fETYLCU2YYc)

[모던 JavaScript 튜토리얼](https://ko.javascript.info/?map)

[오래된 var](https://ko.javascript.info/var)

[[10분 테코톡] 💙 하루의 실행 컨텍스트](https://www.youtube.com/watch?v=EWfujNzSUmw)

# 본문

hoisiting이란 자바스크립트엔진이 script를 해석하는 초기 시점에 모든 변수와 함수를 미리 할당하는 것을 의미합니다.

여기서 var로 선언한 변수의 경우 자바스크립트 엔진은 호이스팅시 undefined로 변수를 바로 초기화하기 때문에 스크립트내에서 선언전에 변수를 사용해도 에러를 내지 않아 선언 라인 이전에는 변수를 참조할 수 없다는 일반적인 프로그래밍 방식에 어긋나는 문제가 생깁니다.

tdz란 일시적 사각지대라는 뜻으로 es6 에서 나온 let과 const라는 변수 선언 방법에서 나온 현상입니다.

let과 const 또한 호이스팅으로 인해 변수를 최상단으로 끌어올려 먼저 선언하지만 var와는 다르게 바로 초기화를 하지는 않고 실제 코드에 도달했을 때 발생하기 때문에 만약 변수의 선언문 이전에 변수를 참조하려고 하면 reference error가 발생하게 됩니다.

이렇게 let과 const로 선언했을 때 선언 이전에 변수를 참조할 수 없는 구역을 TDZ, 일시적 사각지대라고 합니다.
