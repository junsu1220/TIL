# 글의 목적

면접 대비로 대답을 정리해놓는다.

# 레퍼런스

[this 가 동작하는 원리와 용법](https://suzzeong.tistory.com/127)

# 본문

자바스크립트에서는 함수 호출의 방식에 따라 this에 어떤 객체를 바인딩할 지 동적으로 바뀌게 된다.

this는 클래스나 함수에서 동적으로 값을 할당하기 위해서 쓰는 기능이다.

함수의 호출하는 방식에는 크게 함수 호출, 메소드 호출, 생성자 함수 호출, apply/call/bind가 있는데 

함수 호출시에는 기본적으로 전역 객체에 바인딩 된다.

즉, 그냥 console.log(this === window) 를 하면 true가 나오게 된다.

(node.js가 아니라 브라우저에서 사용할 경우의 기준이다. node.js에서는 global객체를 의미한다.)

메소드 호출의 경우 함수가 객체의 프로퍼티 값이면 메소드로서 호출된다.

이 말을 풀어쓰자면 메소드는 객체의 함수인데 이 함수 내부에서 this를 사용할 경우 this는 그 해당 메소드를 호출한 객체를 의미 한다는 말이다. 

백문이 불여일견 코드로 써보자면

```jsx
const myObject = {
  name: 'sujeong',
  greet() {
    console.log(`Hello, my name is ${this.name}`);
  }
};

myObject.greet(); // "Hello, my name is sujeong"
```

생성자 함수 호출의 경우

생성자 함수는 class와 연관이 있는데 객체를 생성하는 역할을 한다.

왜 나오게 되었냐면 개발자들은 초기에는 그냥 단순한 객체들만을 사용하다가 시간이 지날 수록 특정객체의 형태를 계속 써야 됐고 이 중복을 피하기 위해 붕어빵 틀처럼 하나의 틀이 있으면 좋겠다 생각해 나오게 되었다. 

이렇게 생성자함수를 쓸때 this는 그 틀에서의 변수를 지칭하는 데 유용하게 쓰인다.

이 틀은 앞으로 어떻게 쓰일지 미리 예측할 수 없다. 

따라서 받아들이는 인자값을 생성자 함수내에서 다시 정의해두는 느낌이다.

이번에도 코드로 볼 건데 여기서는 sujeong이라는 객체를 Person이라는 생성자함수로 만들었고 이 틀을 사용했기 때문에 자동으로 name과 age라는 값을 갖게 되며 이때 this를 이용해서 이 객체에 동적으로 값을 정의할 수 있는 것이다.

```jsx
function Person(name, age) {
  this.name = name;
  this.age = age;
}

const sujeong = new Person('sujeong', 26);
console.log(sujeong.name); // "sujeong"
console.log(sujeong.age); // 26
```

this를 명시적으로 바인딩할 수 있는 방법이 있는데, 바로 apply, call, bind 메소드를 사용하는 것이다.

이 메소드들은 모든 함수 객체의 프로토타입 객체인 Function.prototype 객체의 메소드이다.

**apply()메서드**는 주어진 this값과 배열 (또는 유사 배열 객체) 로 제공되는 arguments로 함수를 호출한다.

**call()메소드**는 주어진 this값 및 각각 전달된 인수와 함께 함수를 호출한다.

**bind()메소드**가 호출되면 새로운 함수를 생성한다. 받게되는 첫 인자의 value로는 this  키워드를 설정하고, 이어지는 인자들은 바인드된 함수의 인수에 제공된다.

apply, call, bind에서 첫 번째 인자로 다른 것을 넣어주는 게 this를 바꾸는 방법 중 하나다.

```jsx
func.apply(thisArg, [argsArray])
func.call(thisArg[, arg1[, arg2[, ...]]])
func.bind(thisArg[, arg1[, arg2[, ...]]])
// call 예시
function myFunction() {
  console.log(`Hello, my name is ${this.name}`);
}

const myObject = { name: 'sujeong' };

myFunction.call(myObject); // "Hello, my name is sujeong"
// bind 예시
const myObject = { name: 'sujeong' };

function myFunction() {
  console.log(`Hello, my name is ${this.name}`);
}

const myBoundFunction = myFunction.bind(myObject);
myBoundFunction(); // "Hello, my name is sujeong"
```
