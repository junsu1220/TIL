React의 state와 props에 대해서 설명해주세요.

# 글의 목적

면접을 대비해서 대답을 정리한다.

# 레퍼런스

[React의 state와 props에 대해서 설명해주세요.](https://codingpracticenote.tistory.com/181)

[React props와 state 알아보기](https://freestrokes.tistory.com/156)

[기술 면접 part 2.](https://velog.io/@starrypro/Part-6.-JS-기술-면접)

[React의 state와 props에 대해서 설명](https://velog.io/@young0_0/React의-state와-props에-대해서-설명)

# 본문

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/11394b96-c18e-4b4f-aefe-c186e9c88754/Untitled.png)

리액트의 stste는 컴포넌트 내에서 지속적으로 변경이 일어나는 값을 관리하기 위해 사용합니다. useState훅을 사용하여 state를 만들고, setState를 사용하여 값을 변경합니다. 

props는 부모 컴포넌트에서 자식 컴포넌트로 넘겨주는 것들을 의미합니다. 

props로 넘겨준 값들은 불변하며, readOnly속성을 가지고있습니다. 

따라서 자식 컴포넌트에서의 직접적인 props 변경은 불가하며, 내려받은 setState나 함수를 이용하여 props를 바꾸도록 부모 컴포넌트에게 요청할 수 있습니다.

왜 변수가 아닌 state에 데이터를 저장하나?

변수로 저장해도 됩니다. 

하지만 변수값이 바뀌었을 때 일반 변수는 리렌더링이 되지 못하지만, state에 저장된 데이터는 리렌더링이 되기 때문입니다. 

리액트에서는 분리된 컴포넌트 별로 리렌더링을 하게하여 성능을 높일 수 있으므로, state를 주로 사용한다고 생각합니다.

React에서 state는 변할 수 있는 데이터를 의미합니다. 

애플리케이션의 작동 구조를 봤을때, 변할 수 있는 값이면 React의 상태로 적절합니다. 

예를 들어서, input의 value는 사용자가 값을 입력하면 변경될 수 있는 값이기 때문에 state로 적절합니다. 

또한 Social media에서 게시글 역시 다른 유저가 추가로 게시글을 작성하고 난 뒤에는 게시글의 수가 변할 수 있기 때문에 게시글 배열로 state로 적절합니다.

다만, input의 value는 하나의 컴포넌트에만 영향을 주고 게시글의 배열은 여러 컴포넌트에 영향을 줄 수 있는 차이점이 있습니다. 

다른 컴포넌트에 영향을 미치는 정도에 따라 전역 상태와 지역 상태로 구분할 수 있습니다.

props는 외부에서 전달받아 컴포넌트 내에서는 변할 수 없는 값입니다. 

그래서 React에서는 props를 중간에 변경하는 것을 권장하지 않고, lifting state up(상태 끌어올리기)를 통해 상태를 변경시키고 변경된 상태값을 props로 내려주어 side effect를 최소화시킵니다.

> props는 함수에 전달하는 매개변수, state는 함수 내부에 선언된 변수 라고 볼수 있다.
> 

## props

함수 컴포넌트나 클래스 컴포넌트 모두 컴포넌트의 자체 props를 수정해서는 안된다.

이런 함수들은 순수 함수 라 호칭한다. 

입력값을 바꾸려 하지 않고 항상 동일한 입력값에 대해 동일한 결과를 봔환하기 때문이다.

> 모든 react 컴포넌트는 자신의 props를 다룰 때 반드시 순수 함수처럼 동작해야한다.
> 

## state

state로 정의한 값이나 함수는 변경이 가능하다.

setState란 React의 불변성을 지키며 state의 값을 변경하기 위한 리액트 함수 이다.

리액트에서는 모든 상태 값들을 불변성을 유지하며 관리하게되는데,이렇게 불변성을 유지 하는 것은 virtual-dom이 real dom과 차이를 알아내기 위함 이라는 이유가 있다.

> 불변성 메모리 영역에서 값이 변하지 않는다.
> 

만약 객체가 직접적으로 값이 변경되게 된다면 변경된 객체를 찾기 위해 실제 돔과 가상 돔 전체 트리를 비교하며 변경사항을 감지해야한다. 

하지만 불변 객체가 이전 객체와 다른지를 얕은 평가만으로 확인 할수 있기 때문이다.
