# 글의 목적

면접에서 질문으로 나왔을 때를 대비하여 글로 정리한다.

# 레퍼런스

[[React] useRef - 필요성,  필요한 상황, 사용법](https://velog.io/@fejigu/React-useRef-필요성-필요한-상황-사용법)

[useRef는 처음이라 :: 개념부터 활용 예시까지 - Deeming](https://mnxmnz.github.io/react/what-is-use-ref/)

# 본문

react에서는 DOM을 건드리지 않고 거의 대부분의 요구사항을 구현할 수 있지만 특정 상황에 경우는 DOM을 건드려야 하는 경우가 있다. 

또 부모의 props나 자신의 state가 변하면 리렌더링이 일어나는데 이 리렌더링을 일어나지 않게 하기 위해서도 쓰는 경우가 있다.

DOM을 건드리는 경우는 회원가입폼의 input에서 포커스를 시키고 싶을 때가 있다.

이때 input요소의 ref에 useRef로 만든 변수를 할당해주고 이 값과 input의 event.target을 비교해준 이후 그 포커스해야하는 특정 input창이 맞다면 (useRef값).current.focus()로 포커싱을 해줄 수 있다.

```jsx
import React, { useRef } from "react";
const Focus = () => {
  const firstRef = useRef(null);
  const secondRef = useRef(null);
  const thirdRef = useRef(null);
  const handleInput = (event) => {
    console.log(event.key, event);
    if (event.key === "Enter") {
      if (event.target === firstRef.current) {
        secondRef.current.focus();
        event.target.value = "";
      } else if (event.target === secondRef.current) {
        thirdRef.current.focus();
        event.target.value = "";
      } else if (event.target === thirdRef.current) {
        firstRef.current.focus();
        event.target.value = "";
      } else {
        return;
      }
    }
  };
return (
    <div>
      <h1>타자연습</h1>
      <h3>각 단어를 바르게 입력하고 엔터를 누르세요.</h3>
      <div>
        <label>hello </label>
        <input ref={firstRef} onKeyUp={handleInput} />
      </div>
      <div>
        <label>world </label>
        <input ref={secondRef} onKeyUp={handleInput} />
      </div>
      <div>
        <label>codestates </label>
        <input ref={thirdRef} onKeyUp={handleInput} />
      </div>
    </div>
  );
};
export default Focus;
```

useRef 로 관리하는 변수는 값이 바뀐다고 해서 컴포넌트가 리렌더링되지 않는다. 

리액트 컴포넌트에서의 상태는 상태를 바꾸는 함수를 호출하고 나서 그다음 렌더링 이후로 업데이트된 상태를 조회할 수 있지만, **useRef 로 관리하는 변수는 설정 후 바로 조회**할 수 있다.

useRef() 를 사용할 때 파라미터를 넣어주면, 이 값이 `.current`값의 기본값이 된다. 

그리고 이 값을 수정할 때는 `.current`값을 수정하면 되고 조회할 때는 `.current`를 조회하면 된다.
