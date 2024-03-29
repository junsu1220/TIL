### 상태관리를 왜 할까요? 그리고 평소 state 관리는 어떻게 하시나요?

- 단순 정보전달의 정적인 웹 사이트 부터 상호작용으로 구성되는 동적 웹 페이지로 변화하는 과정 속에서 데이터 관리의 필요성이 나타났습니다.
- 한가지 예로 DB로부터 받아온 데이터가 공통적으로 재사용 되는 일이 늘어남에 따라 API 호출 횟수에 직접적으로 연관되는 DB의 의존도를 줄일 필요가 있었습니다.
- 데이터가 필요할 때 마다 서버를 호출 하는 것은 비효율적 이므로 DB로부터 분리된 상태 저장소의 필요성이 나타나게 되었습니다.
- 정확하고 효율적인 상태 관리는 DB와의 접촉 횟수를 줄여주며 안정적이고 지속적인 서비스 제공을 가능하게 합니다.
- 현재 상태관리 라이브러리 중 하나인 Redux-toolkit를 사용하여 전역적으로 상태를 관리해 단방향 데이터 흐름을 지키기위해 노력하고 있습니다.
- 상태관리를 하는 이유는 유저와의 상호작용으로부터 데이터를 갱신시켜줘야 하기 때문으로 알고 있습니다.
- 저는 상태관리를 어떠한 동작에 의해 UI,UX 내의 변화가 필요할 때
    - 그 데이터가 단독으로 관리 가능하다면 useState를 이용해서 지역적으로 관리하고
    - 비동기통신의 결과로 로딩여부가 필요하거나 다른 컴포넌트들에서 그 데이터를 사용한다면 redux를 사용해 전역적으로 관리합니다.

### Redux가 무엇인가요, 왜 Redux를 사용하시나요?

- 리덕스란 전역 상태 저장소입니다.
- 저장된 데이터를 App 이 가져다 쓰고, 자식들도 가져다 쓰는 것입니다.
- 부모의 state를 간섭하는 것이 아니라서 유용하게 쓰입니다.
- 아래로 전달해주기 위해 쓸데없는 데이터를 가지고 있게 되는 props driling을 해결해주기 위해 리덕스를 사용한다.

### Redux 말고 다른 전역 상태관리 아는 것 하나와 차이점을 말해주세요

- Redux는 store라는 관리 공간 속에서 여러 reducer들을 이용해 **각각의 reducer에서 쓰이는 state를 관리하는 방식으로 운영**된다.
- 반면, Recoil은 atom이라는 즉, **원자라고 불리는 상태 저장소를 통해 state를 관리**한다.
- 이 atom은 **store와 같은 하나의 전역 관리 객체 속에서 관리되는 방식이 아닌 말그대로 각각의 atom에 관리되고 있다.**
- Redux의 핵심은 reducer를 통해서 state를 관리하는 것인데 이때 **state를 저장, 변경, 삭제 등을 하기 위해 dispatch라는 메소드를 이용해 관리**한다.
- dispatch를 이용할 때는 두 가지 값이 필요한데, 하나는 **우리가 현재 가지고 있는 state**이며 다른 하나는 이 state를 이용해서 **어떠한 행위와 갱신할 값의 정보를 들고 있는 action이 필요**하다.
- 반면 **Recoil은** dispatch의 방식이 아닌 우리가 React에서 익숙하게 쓰고 있는 **useState의 형식을 그대로 따라간다.**
- useRecoilState를 이용해서 atom에 있는 값들을 변화하여 상태관리를 할 수 있는데 이 Recoil에는 useState에서 쓰이는 기존 값을 불러오는 읽기 전용, 기존 값을 덮어씌우는 쓰기 전용으로도 **함수를 따로 분리해 쓸 수 있도록 했다는 점이 특징**이다.

### 버츄얼 돔과 리얼 돔의 차이를 설명해주세요

- DOM은 웹 브라우저가 html 파일, 문서를 접근하기 위한 혹은 인식하기 위한 모델, 방식, 인터페이스입니다.
- JavaScript는 이러한 웹 페이지들의 태그를 인식해 추가, 수정, 삭제, 변화 등 다양한 작업을 처리할 수 있습니다.
- 기존의 DOM 요소에서 데이터를 저장하거나 변경하는 사항이 생기면 DOM을 전부 갱신하여 새로 불러와줘야 한다는 제약이 있습니다.
- React에서는 이 과정이 반복되는 것이 비효율적이라고 생각하였고, DOM을 본 뜬 가상 DOM을 이용하면 데이터의 변화가 생길 때 가상 DOM과 DOM을 비교해 달라진 부분만을 변경하여 갱신해줌으로서 불필요하게 DOM을 전부 불러오는 문제를 방지할 수 있었습니다.

### useRef에 대해 설명해보세요
- **useRef**란 어떠한 **특정 DOM**을 선택할 수 있게 해줍니다.
- 코딩을 하다보면 DOM을 직접 선택해서 포커스를 주거나 특정 엘리먼트의 크기나 색상을 변경하는 경우가 있는데 그때 사용하는 것입니다.
- 특정 DOM을 선택하는 용도 이외에도 **Component 안에서 조회 및 수정이 가능한 변수를 관리하는 용도**로도 사용된다.
- 하지만 **useRef** 이용해서 변수를 업데이트 하게 되면 해당 Component가 리렌더링 되지 않기 때문에 용도에 맞게 사용해야 합니다.

### useEffect의 실행 순서에 대해 설명해주세요

- 우선 **최초로 사이트를 띄울 시, useEffect의 내용이 반드시 실행**되도록 되어있습니다.
- 이 과정 속에서 dependency array, **의존성 배열**의 존재가 중요하게 됩니다.
    - 의존성 배열 자체가 없다면 **useEffect는 렌더링이 일어날 때마다 계속 실행됩니다**.
    - **의존성 배열이 있고, 내부에 요소가 없다면 useEffect는 최초로 사이트를 띄운 이후부터는 실행되지 않습니다.**
    - **의존성 배열이 있고, 내부에 요소가 있다면 해당 요소의 데이터가 변경되거나 갱신될 때마다 useEffect의 내용이 실행**되도록 되어있습니다.
- useEffect에서는 갱신 시 실행되는 업데이트 내용 외에도, **useEffect를 적용한 컴포넌트가 제거될 시 리소스를 정리해야 합니다.**
이 과정을 React에서는 Clean-up이라고 부르며, **업데이트 내용 뒤에 return을 붙여 cleanup을 적용하도록 합니다.**

### useEffect의 실행 순서에 대해 설명해주세요

- 우선 **최초로 사이트를 띄울 시, useEffect의 내용이 반드시 실행**되도록 되어있습니다.
- 이 과정 속에서 dependency array, **의존성 배열**의 존재가 중요하게 됩니다.
    - 의존성 배열 자체가 없다면 **useEffect는 렌더링이 일어날 때마다 계속 실행됩니다**.
    - **의존성 배열이 있고, 내부에 요소가 없다면 useEffect는 최초로 사이트를 띄운 이후부터는 실행되지 않습니다.**
    - **의존성 배열이 있고, 내부에 요소가 있다면 해당 요소의 데이터가 변경되거나 갱신될 때마다 useEffect의 내용이 실행**되도록 되어있습니다.
- useEffect에서는 갱신 시 실행되는 업데이트 내용 외에도, **useEffect를 적용한 컴포넌트가 제거될 시 리소스를 정리해야 합니다.**
이 과정을 React에서는 Clean-up이라고 부르며, **업데이트 내용 뒤에 return을 붙여 cleanup을 적용하도록 합니다.**

### var, let, const의 차이에 대해 알려주세요.

- const로 선언한 변수명은 절대적이므로 변경되지 않으며 초기화를 통해 변수에 할당한 값도 절대적으로 변경되지 않습니다.
- let은 const와 같은 점으로서 선언한 변수명 자체는 절대적이므로 재선언이 불가능하나 변수 속 값은 재할당할 수 있다는 차이가 있습니다.
- var의 경우, 재선언에다 재할당도 가능한데 거기에 중복 선언까지 가능하다는 이슈가 있습니다.
- var의 이런 자유로운 점은 변수를 이용할 시 예기치 못한 문제를 발생할 수 있으므로 되도록 const와 let을 활용해 변수를 관리하는 것이 좋습니다.

### Async/Await와 Promise의 차이

- promise는 자바스크립트에서 비동기 처리에 사용되는 객체입니다.
- **내용은 실행 되었지만 결과를 아직 반환하지 않은 객체**라고 이해해도 좋습니다.
- 값이 참이면 resolve 를 호출하고, 아닐시에는 reject 를 호출한다.
- resolve 한 반환 값에 대해서는 then() 을 통해 결과 값을 반환 받을 수 있고 reject 의 반환 값에 대해서는 catch() 를 통해 반환 받는다.
- 함수에 `async` 키워드를 적고, 비동기 대상에 `await`를 추가해주면 된다.
- 비동기 대상 함수에 `await`를 추가하면, *'이 함수의 처리를 기다려!'* 라는 의미가 되기에
- `await` 함수 아래에 해당 함수의 응답값을 사용하는 구문을 추가해주면 된다.
- `async await`를 사용하게 되면 하나의 `catch`만 해주면된다!
- 해당 `catch`문에서는 `try` 내부에서 발생하는 모든 에러를 접근할 수 있다.

### 데이터 10,000개를 가지고 무한 스크롤 구현시에 가장 중요하게 고려해야 할점은?

- 무한스크롤은 트위터나 페이스북 같은 단발성 메시지가 주가 되는 SNS에서는, 최근 글에만 신경쓰게 할 수 있지만, 그렇지 않은 사이트들은 가령 열 페이지 뒤쪽의 게시물을 보기 위해서 페이지 로딩을 열 번을 해야 되는 번거로움이 고려해야 할 점입니다.
- 즉 과거 데이터를 보고 싶은 사람들이 많은 사이트라면, 무한스크롤 구현을 하기에 적합하지 않다는 것을 고려해야 합니다.

### CloudFront를 사용해본적이 있나요? 사용해봤다면, CloudFront로 배포하는 이유를 설명해주세요

- S3 버킷은 선택한 리전 내에만 생성되기 때문에 해당 리전에서 멀어질수록 접속 속도가 느려지게 되는데요.
- 또한, 동시 접속수가 많아질수록 느려지기도 하고요. 그렇기 때문에 이 문제를 해결하기 위해 CloudFront 라는 서비스를 S3와 함께 사용하게 됩니다.
- CloudFront란 전 세계의 정적/동적 웹 콘텐츠, 비디오 스트림 및 API를 안전하게 대규모로 전송할 수 있는 콘텐츠 전송 네트워크 서비스라고 할 수 있어요.
- CloudFront는 전 세계에 분포된 엣지 로케이션이라고 하는 데이터 센터의 엣지 서버를 사용해 콘텐츠를 캐싱하고, 사용자가 위치한 곳에서 가장 가까운 엣지 로케이션에서 콘텐츠를 제공받을 수 있도록 해주는 역할을 합니다(CDN).
- 또 호스팅을 HTTPS로 하게 할 수도 있는 점에서 보안을 향상 시킬수 있어서 CloudFront로 배포를 합니다.

### useEffect와 useLayoutEffect 차이에 대해 설명해주세요

- useEffect 는 컴포넌트들이 render 와 paint 된 후 실행됩니다. **비동기적(asynchronous)**으로 실행됩니다.
- paint 된 후 실행되기 때문에, useEffect 내부에 dom 에 영향을 주는 코드가 있을 경우 사용자 입장에서는 **화면의 깜빡임을 보게됩니다**
- useLayoutEffect 는 컴포넌트들이 render 된 후 실행되며, 그 이후에 paint 가 됩니다. 이 작업은 **동기적(synchronous)**으로 실행됩니다.
- paint 가 되기전에 실행되기 때문에 dom 을 조작하는 코드가 존재하더라도 사용자는 **깜빡임을 경험하지 않습니다**
- 화면이 깜빡거리는 상황일 때, 예를들어 state가 존재하며, 해당 state가 조건에 따라 첫 painting 시 다르게 렌더링 되어야 할 때는 useLayoutEffect사용

### Closure란?

- **“자신이 선언될 당시의 환경을 기억하는 함수”**
- 흔히말해 함수 내에서 함수를 선언하고 사용하면 클로저라고 한다.
- 여기서 바깥쪽 함수는 **외부함수**, 그 안에서 선언한 함수는 **내부함수**
라고 부른다.

```jsx
function hello(name) {
  let _name = name;
  console.log('Hello, '+_name);
}

hello('백산'); // [출력] : Hello, 백산
hello('신우'); // [출력] : Hello, 신우
```

```jsx
function hello(name) {
  let _name = name;
  return function() {
    console.log('Hello, '+_name);
  }
}

let hello1 = hello('백산');
let hello2 = hello('신우');
hello1(); // [출력] : Hello, 백산
hello2(); // [출력] : Hello, 신우
```

- 일반함수에서는 hello('백산')를 정의한 시점에서 _name은 '백산'이라는 string으로 결정된다.
- 출력이 끝난 후에는 해당 함수는 소멸(해당 함수의 전역변수가 초기화됨)되어 다시 같은 함수를 사용하기 위해서는 또다시 백산이라는 string을 받는 함수를 선언해야만 한다.
- 그에 비해 내부함수의 경우 hello('백산')으로 정의된 함수가 소멸하지 않고 내부의 클로저가 외부함수의 전역변수 값을 기억하고 있다.
- 따라서 hello1()을 사용하기만 해도 **클로저가 외부함수의 전역변수값을 가져와 출력**한다.
- 이점이 일반함수와 내부함수가 다른점이다.
- 일반함수는 **선언할때마다 내부의 전역변수가 초기화**되지만 내부함수는 **선언했을때의 환경을 기억**하고 있다가 여러번 실행할 수 있다.
- 클로저는 일반함수와 달리 함수 **내부에 선언되는 함수로 함수가 실행될때 외부변수에 접근하기 위한 객체**이다.

### Javascript 호이스팅에 대해 설명해주세요.

- 함수 안에 있는 선언들을 모두 끌어올려서 해당 함수 유효 범위의 최상단에 선언하는 것을 말한다.
    - 자바스크립트 Parser가 함수 실행 전 해당 함수를 한 번 훑는다.
    - 함수 안에 존재하는 변수/함수선언에 대한 정보를 기억하고 있다가 실행시킨다.
    - 유효 범위: 함수 블록 {} 안에서 유효
- var 변수 선언과 함수선언문에서만 호이스팅이 일어난다.
    - var 변수/함수의 선언만 위로 끌어 올려지며, 할당은 끌어 올려지지 않는다.
    - let/const 변수 선언과 함수표현식에서는 호이스팅이 발생하지 않는다.

### 프로세스 생성 과정에 대해 설명해보세요

- 프로세스는 간단히 말하자면 실행 중인 프로그램을 의미합니다. 아마 여러분들은 컴퓨터를 하면서 아주 빈번하게 듣는 용어이기도 합니다.
- 컴퓨터에서 말하는 실행 중인 프로그램이라는 건 저장공간에 있는 실행 파일이 메모리를 할당받아 명령어를 수행한다는 것을 의미합니다.
- 프로세스 제어 블록(PCB)가 생성되며 OS가 실행한 프로그램의 코드를 읽어들여 프로세스에 할당된 메모리의 Text segment에 저장한다.
- 초기화된 전역 변수 및 static 변수를 data segment에 할당.
- HEAP과 Stack은 초기 메모리 주소만 초기화됨.
- PCB에 여러 정보가 기록되면 Ready Queue에서 CPU를 할당받기까지 대기한다.

### HTTPS란

- HTTP란 HyperText Transfer Protocol의 약자로써, 풀어서 설명하면 **하이퍼텍스트(HyperText)를 전송(Transfer)하기 위해 사용되는 통신 규약(Protocol)**
이다.
- 즉, 인터넷에서 HTML과 같은 문서를 사용자 컴퓨터에 설치된 웹 브라우저가 웹 서버에 요청할 때의 규칙이라고 할 수 있다.
- HTTPS는 HTTP에서 데이터를 주고 받는 과정에 ‘보안’ 요소가 추가되었다는 것이 가장 큰 차이점이다.
- HTTPS를 사용하면 **서버와 클라이언트 사이의 모든 통신 내용이 암호화**된다.

### TCP란 무엇인가

- TCP는 말 그대로 **전송 제어를 위한 작업을 해주는 역할**
- TCP는 두가지 역할을 한다.
    - **받을 대상 노드(호스트)가 서비스 가능(연결 가능) 상태인지 확인 및 연결을 수립하는 역할**
    - **전송을 제어해주는 정보를 패킷에 추가해주는 역할**
- 받을 대상 노드(호스트)가 서비스 가능 상태인지 확인하기 위해서는 해당 노드가 활성 상태인지 확인하기 위해 통신을 해야 한다.
- TCP에서는 3 Way Handshake라는 방식으로 해당 노드와 통신을 수행하게 된다.
- **SYN 단계**
    - 어플리케이션이 서버에 통신을 위한 연결을 요청하는 단계
- **SYN-ACK 단계**
    - 서버가 어플리케이션에 자신이 활성 상태임을 알리고 어플리케이션에서도 포트를 열어 연결을 활성화하라는 요청 메세지를 전송
- **ACK 단계**
    - 어플리케이션이 서버의 요청 메세지를 수락하여 연결이 수립
- 전송을 제어해주는 규약(Protocol)에 대한 정보를 패킷에 추가한다. 대표적으로 Port 정보, 순서 정보가 있다.
- **Port 정보는 패킷이 어떤 프로세스에 전달되어야 할지에 대한 정보**
로, 프로세스간 통신을 위해 사용되는 정보이다.
- **전송 제어 정보 중 하나인 순서 정보는 전달해야 하는 패킷이 여러개로 나뉘어져 있을 경우 각 패킷이 어떤 순서로 처리되어야 하는지에 대한 정보**이다.

### TCP와 UDP의 차이점은?

- 연결형 서비스를 지원하는 전송 계층 프로토콜로써, 인터넷 환경에서 기본으로 사용합니다.
- 호스트간 신뢰성 있는 데이터 전달과 흐름제어를 합니다. 즉, 인터넷상에서 데이터를 메시지의 형태로 보내기 위해 IP와 함께 사용하는 프로토콜입니다.
- 일반적으로 TCP와 IP를 함께 사용하는데, IP가 데이터의 배달을 처리한다면 TCP는 패킷을 추적 및 관리하게 됩니다.
- 데이터의 전송 순서를 보장한다.
- 비연결형 서비스를 지원하는 전송계층 프로토콜로써, 인터넷상에서 서로 정보를 주고받을 때 정보를 보낸다는 신호나 받는다는 신호 절차를 거치지 않고, 보내는 쪽에서 일방적으로 데이터를 전달하는 통신 프로토콜입니다.
- 데이터를 데이터그램 단위로 처리하는 프로토콜입니다.
- TCP는 연속성보다 신뢰성있는 전송이 중요할 때에 사용하는 프로토콜이며, UDP는 TCP보다 속도가 빠르며 네트워크 부하가 적다는 장점이 있지만, 신뢰성있는 데이터 전송을 보장하지는 않습니다.
- 그렇기 때문에 신뢰성보다는 연속성이 중요한 서비스의 예를 들면 실시간 서비스(streaming)에 자주 사용됩니다.

### 브라우저에서 주소창에 url 입력시 어떤일이 일어나는가

1. **브라우저 주소창**에 maps.google.com을 입력한다.
2. 브라우저가 maps.google.com의 **IP 주소**를 찾기 위해 **캐시**에서 **DNS 기록**을 확인한다.
3. 만약 요청한 URL(maps.google.com)이 캐시에 없다면, **ISP의 DNS 서버**가 **DNS 쿼리로** maps.google.com을 **호스팅**하는 서버의 IP 주소를 찾는다.
4. 브라우저가 해당 서버와 **TCP 연결**을 시작한다.
5. 브라우저가 웹서버에 **HTTP 요청**을 보낸다.
6. 서버가 요청을 처리하고 **응답**을 보낸다.
7. 서버가 **HTTP 응답**을 보낸다.
8. 브라우저가 **HTML** 컨텐츠를 보여준다.

### JavaScript Event Loop

- 브라우저는 Web APIs, Event Table, Callback Queue, Event Loop 등으로 구성됩니다.

- **Heap**: 메모리 할당이 발생하는 곳
- **Call Stack** : 실행된 코드의 환경을 저장하는 자료구조, 함수 호출 시 Call Stack에 push 됩니다. (Call Stack에 대한 자세한 설명은 **[여기](https://medium.com/sjk5766/call-stack%EA%B3%BC-execution-context-%EB%A5%BC-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90-3c877072db79)**)
- **Web APIs**: DOM, AJAX, setTimeout 등 브라우저가 제공하는 API
- **Callback Queue,** **Event Loop, Event Table**(그림엔 없음) 은 아래에서 설명하겠습니다.

```jsx
setTimeout(function exec() {
  console.log('second')
}, 1000);
```

- **Web APIs**: setTimeout이 Call Stack에 들어와 실행되면 Browser API인 timer를 호출합니다.
- **Event Table**: 특정 event(timeout, click, mouse move 등등)가 발생했을 때 **`어떤 callback 함수가 호출되야 하는지`**를 알고 있는 자료구조입니다. 위 코드에서 호출된 timer가 종료되면 event가 발생하게 되는데 이때 **exec callback 함수가 실행되어야 한다는 것**을 **`Event Table`**이 알고 있습니다.
- **Callback Queue**: ****이벤트 발생 시 실행해야 할 callback 함수가 **`Callback Queue`**에 추가됩니다.
- **Event Loop**: ****Event Loop의 역할은 간단합니다.1. **`Call Stack`**과 **`Callback Queue`**를 감시합니다.2. Call Stack이 **`비어있을 경우`**, Callback queue에서 함수를 꺼내 Call Stack에 추가 합니다.

[JavaScript 비동기 핵심 Event Loop 정리](https://medium.com/sjk5766/javascript-%EB%B9%84%EB%8F%99%EA%B8%B0-%ED%95%B5%EC%8B%AC-event-loop-%EC%A0%95%EB%A6%AC-422eb29231a8)

### RESTFul API란

- HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미한다.
- 즉, REST는 자원 기반의 구조(ROA, Resource Oriented Architecture) 설계의 중심에 Resource가 있고 HTTP Method를 통해 Resource를 처리하도록 설계된 아키텍쳐를 의미한다.
- 웹 사이트의 이미지, 텍스트, DB 내용 등의 모든 자원에 고유한 ID인 HTTP URI를 부여한다.
CRUD Operation
Create : 생성(POST)
Read : 조회(GET)
Update : 수정(PUT)
Delete : 삭제(DELETE)
HEAD: header 정보 조회(HEAD)

### GET, POST 방식의 차이점

- **사용목적** : GET은 서버의 리소스에서 데이터를 요청할 때, POST는 서버의 리소스를 새로 생성하거나 업데이트할 때 사용한다.
- DB로 따지면 GET은 SELECT 에 가깝고, POST는 Create 에 가깝다고 보면 된다.
- **요청에 body 유무** : GET 은 URL 파라미터에 요청하는 데이터를 담아 보내기 때문에 HTTP 메시지에 body가 없다. POST 는 body 에 데이터를 담아 보내기 때문에 당연히 HTTP 메시지에 body가 존재한다.

### Webpack 써보신 적 있나요

- Webpack = 모듈 번들링이라고 한다.
- html 파일에 들어가는 자바스크립트 파일들을 하나의 자바스크립트 파일로 만들어주는 방식을 모듈 번들링이라고 한다.
- 쉽게 말하면, 필요한 다수의 자바스크립트 파일을 하나의 자바 스크립트 파일로 만들어 주는 것을 Webpack 이라고 한다.
- 파일을 컴파일 할 때, 여러 모듈들의 파일을 읽어오는데 시간이 오래 걸린다. 그 부분을 해결하기 위해 여러 파일을 하나의 파일로 번들링 해준다.
- 하나의 자바스크립트 파일로 만들어서 웹페이지 성능 최적화 해준다.

### 동기와 비동기의 차이

- 동기는 데이터의 요청과 결과가 한 자리에서 동시에 일어나는것을 말합니다.
- **요청을 하면 시간이 얼마나 걸리던지 요청한 자리에서 결과가 주어져야 합니다.**
- *사용자가 데이터를 서버에게 요청한다면 그 서버가 데이터 요청에 따른 응답을 사용자에게 다시 리턴해주기 전까지 사용자는 다른 활동을 할 수 없으며 기다려야만합니다.*
- 비동기는 동시에 일어나지 않는다는 의미입니다.
- **요청한 결과는 동시에 일어나지 않을거라는 약속입니다.**
- *서버에게 데이터를 요청한 후 요청에 따른 응답을 계속 기다리지 않아도되며 다른 외부 활동을 수행하여도되고 서버에게 다른 요청사항을 보내도 상관없습니다*

### Array vs LinkedList8

- element들을 index를 통해 직접적으로 접근할 수 있습니다.
- ex) arr[0], arr[1] 따라서, 특정 element에 접근하는 시간 복잡도는 **O(1)**으로 빠르게 찾을 수 있습니다.
- LinkedList는 **Sequential Access**를 지원합니다.
- 어떤 element/node를 접근할 때 처음 부터 찾는 element에 도달할 때까지 순차적으로 검색하면서 찾아야 합니다.
- 특정 element에 접근할 때의 시간 복잡도는 **O(n)**이 됩니다.

### 서버 사이드 렌더링이란?

- 렌더링이란? → 서버로부터 요청해서 받은 내용을 브라우저 화면에 표시해주는 것입니다.
- SSR은 서버에서 사용자에게 보여줄 페이지를 모두 구성해 보여주는 방식입니다.
- 서버를 이용해 페이지를 구성하기 때문에 클라이언트 사이드 렌더링(CSR)보다 페이지 구성 속도는 느리지만
- 전체적으로 사용자에게 보여주는 컨텐츠 구성이 완료되는 시점은 빨라진다는 장점이 있습니다.
- 또한 SEO도 쉽게 구성할 수 있습니다.

### MVC 패턴이란 무엇인가?

- MVC패턴은 디자인패턴 중 하나입니다.
- 사용자 인터페이스로부터 비즈니스 로직을 분리하여 애플리케이션의 시각적 요소나 그 이면에서 실행되는 비즈니스 로직을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있습니다.
- MVC에서 모델은 애플리케이션의 정보(데이터)를 나타내며, 뷰는 텍스트, 체크박스 항목 등과 같은 사용자 인터페이스 요소를 나타내고, 컨트롤러는 데이터와 비즈니스 로직 사이의 상호동작을 관리한다.

### 아토믹 디자인 패턴에 대해 아는가?

- 대형 프로젝트에서는 최적화된 코드 재사용이 필수입니다.
- 아토민 디자인 패턴은 이를 위한 생긴 코드 디자인 패턴 중 하나입니다.
- 컴포넌트를 사용하는 라이브러리와 프레임워크에 모두 사용 가능합니다.
- **Atoms(원자) → 레이블(Label), 텍스트(Text), 컨테이너(Container), 버튼(Button), 아이콘(Icon) 등**
- **Molecules(분자) → 입력 폼(Input forms), 네비게이션(Navigation), 카드(Card) 등**
- **Organisms(유기체) → 입력 폼과 함께 헤더를 감싸거나, 여러 카드를 관리하는 그리드**
- **Templates(템플릿) → 여러 유기체가 모여있지만, 페이지보다는 낮은 단위**

### 웹 스토리지의 차이점

- 쿠키
    - Response Header에 Set-Cookie 속성을 사용하면 클라이언트에 쿠키를 만들 수 있다.
    - 쿠키는 사용자가 따로 요청하지 않아도 브라우저가 Request 시에 Request Header를 넣어서 **자동으로 서버에 전송**한다.
- 세션
    - 사용자 정보를 파일 브라우저에 저장하는 쿠키와 달리 세션은 **서버 측에서 관리**한다.
    - 서버에서 클라이언트를 구분하기 위해 세션 ID를 부여하며, 웹 브라우저가 서버에 접속해서 브라우저를 종료할 때까지 인증상태를 유지한다.
- 로컬 스토리지
    - 사용자가 데이터를 지우지 않는 이상, 브라우저나 OS를 종료해도 계속 브라우저에 남아있음 (**영구성**)
    - 지속적으로 필요한 데이터 저장(자동 로그인 등)
- 세션 스토리지
    - 데이터가 오리진 뿐만 아니라 **브라우저 탭에도 종속**되기 때문에, 윈도우나 브라우저 탭을 닫을 경우 제거
    - 일시적으로 필요한 데이터 저장(일회성 로그인 정보, 입력폼 저장 등)

### http vs https 차이점에 대해 설명해주세요

- HTTP는 암호화가 추가되지 않았기 때문에 보안에 취약한 반면, HTTPS는 안전하게 데이터를 주고받을 수 있다.
- 하지만 HTTPS를 이용하면 암호화/복호화의 과정이 필요하기 때문에 HTTP보다 속도가 느리다.
- (물론 오늘날에는 거의 차이를 못느낄 정도이다.) 또한 HTTPS는 인증서를 발급하고 유지하기 위한 추가 비용이 발생하다.
- https는 http프로토콜에 보안 기능을 추가한 것이라고 할 수 있다.

### 웹 프로토콜이란?

- HTTP(Hypertext Transfer Protocol) 프로토콜이란 상호 간에 정의한 규칙을 의미하며 특정 기기 간에 데이터를 주고받기 위해 정의다.
- 통신 프로토콜을 쉽게 풀어보면 "내가 이렇게 보낼게 너는 이렇게 받아" 라고 이해하면 되겠다.
- 웹에서는 브라우저와 서버 간에 데이터를 주고받기 위한 방식으로 HTTP 프로토콜을 사용하고 있습니다.

### AJAX란 무엇인가

- **자바스크립트를 통해서 서버에 데이터를 비동기 방식으로 요청하는 것**
- AJAX는 HTML 페이지 전체가 아닌 일부분만 갱신할 수 있도록 XMLHttpRequest객체를 통해 서버에 request한다.
- 이 경우, **JSON이나 XML형태로 필요한 데이터만 받아 갱신하기 때문에 그만큼의 자원과 시간을 아낄 수 있다.**

### Promise와 Callback의 차이점은

- callback을 사용하면 비동기 로직의 결과값을 처리하기 위해서는 callback안에서만 처리를 해야하고, 콜백 밖에서는 비동기에서 온 값을 알 수가 없습니다.
- 하지만 promise를 사용하면 비동기에에서 온 값이 promise 객체에 저장되기 때문에 코드 작성이 용이해집니다.

### 자바스크립트와 타언어의 차이점

**JavaScript**

- 웹 프로그래밍을 위한 객체지향 스크립트 언어
- 실행환경 : 추가적인 환경 설정 필요 X(브라우저 동작에 따라감)
- 변수 & 컴파일 : 변수 자료형을 미리 선언하지 않아도 브라우저가 자동으로 파악한다. 또한, 텍스트로 쓰인 코드로 실행될 수 있는 스크립트 언어이다.
- 사용범위 : 다양한 웹 브라우저에서 이용되며, 자바스크립트가 실행되려면 HTML, CSS에 의존해야 한다

**Java**

- 객체지향 프로그래밍 언어
- 실행환경 : 추가적이 환경 설정 필요 O(JRE, JDK)
- 변수 & 컴파일 : 변수 자료형이 반드시 선언되어야 하며, 프로그래밍 언어이기 때문에 컴퓨터가 이해할 수 있도록 컴파일되어야 한다.
- 사용범위 : 거의 모든 환경에서 활용되며 다양한 운영체제에서 실행될 수 있는 독립적인 언어이다.

### ES6의 호환성 해결방법은?

- Javascript의 호환성에 따른 충돌이나 부작용을 줄이기 위한 방법으로는 Babel이라는 도구를 사용하면 됩니다.
- 바벨은 주로 ES5 이상 버전의 코드를 현재 및 과거의 브라우저와 같은 환경에서 호환되는 버전으로 변환하는데 사용되는 도구로,
- IE나 다른 브라우저에서 동일한 기능을 제공하고 side-effect를 최소한으로 줄일수 있습니다.

### babel은 컴파일러 인가? 트랜스파일러인가?

- Babel은 빌드 단계에서 Javascript를 다른 언어로 변환하는 것이 아닌 어플리케이션에서 설정된 환경에 맞게 또는 현재 사용하고 있는 대중적인 브라우저 스펙 또는 호환성에 맞는 하위 버전의 Javascript로 변환한다는 의미에서 Babel은 트랜스파일러라고 할 수 있습니다.
- 컴파일러와 트랜스파일러에 대해 설명하자면,
    - **컴파일러** 의 경우에는 한 언어도 작성된 코드를 다른 언어로 변환하는 것으로 C 코드로 개발된 코드를 Assembly 코드로 변환하는 것과 같고
    - **트랜스파일러** 란 한 언어로 작성된 소스 코드를 비슷한 수준의 추상화를 가진 언어로 변환하는 것을 의미합니다.

### ES6에 추가된 것은 무엇인가?

- **String Literal**
    - ES6의 String Literal을 활용하면 문자열을 좀 더 직관적으로 결합할 수 있다.
- **객체 비구조화 ( Object Destructuring )**
    - 객체에 들어있는 값들 각각을 꺼내 쓸 수 있다.
- **객체 리터럴 ( Object Literal )**
    - ES6에선 객체 프로퍼티 이름이 로컬 변수 이름과 같으면 콜론과 값 없이 작성해도 된다.
    - 값을 직접 명시해주는 경우와 함께 사용할 수도 있다
- **for .. of**
    - for.. of는 이런 아쉬움을 덜어내 줄 수 있도록 ES6에 추가된 효율적인 반복문이다
- **Spread Operator**
    - 배열이나 객체, 문자열을 ...과 함께 사용하면 배열, 객체, 문자열을 결합하기가 매우 수월해졌습니다.
- **Rest Parameter**
    - ... 을 함수의 인자에 사용하면 인자를 배열로 받을 수 있다
- **Arrow Function**
    - Arrow Function을 활용하면 함수 표현을 기존의 function 표현보다 짧은 구문으로 표현할 수 있다.
- **Default Params**
    - es6에선 함수의 기본 파라미터를 세팅해줄 수 있다.
- **includes**
    - es5에서 배열에 특정 값이 있는지 알고싶으면 indexOf를 활용해 -1 값이 있는지를 봐야했다.
    - es6에선 includes를 활용하면 배열에 특정값이 있는지를 깔끔하게 확인할 수 있다.
- **let & const**
    - es5에선 변수를 var로만 선언할 수 있었다. 그러나 es6에서 let과 const가 추가되었다.
    - let과 const를 활용하면 예상하지 못한 오류가 발생하는 걸 막을 수 있다. 이를 사용하길 권장한다.
- **import & export**
    - import와 export를 활용하면 다른 파일에서 사용한 원시값, 객체, 배열, 함수 등을 가져와서 쓸 수 있다.
- **Classes**
    - es5에서 어떤 함수를 Class처럼 쓰려면 함수를 Class처럼 만들고 prototype을 활용해야 했지만
    - es6부터는 객체지향형 프로그래밍 언어들이 지원하던 Class를 javascript에서도 사용할 수 있게 되었다.
- **Trailing Commas**
    - es6부터는 trailing comma를 지원하기 때문에 객체나 배열의 마지막 값 뒤에 ,을 붙여도 된다
    - ( trailing comma는 데이터가 늘어날 경우를 대비해서 사용한다 )
- **Map & Set**
    - es6부터는 javascript에서도 Map과 Set을 지원한다
- **Async & Await**
    - es6에선 Async와 Await를 활용해서, promise then을 쓸 때 보다 좀 더 세련되게 callback 지옥을 벗어날 수 있다.

### Context API란?

- Context API는 리액트에 내장된 기능으로 **Props**를 사용하지 않아도 특정 값이 필요한 컴포넌트끼리 쉽게 값을 공유할 수 있게 해 준다.
- 주로 프로젝트에서 전역 상태를 관리할 때 많이 사용한다.
- 리덕스에서의 강력한 미들웨어 기능은 없다.

### 라이프사이클 메소드에 대해 설명

- 크게 세가지 유형으로 나눌 수 있는데 생성 될때, 업데이트 할 때, 제거할 때이다.
- 이를 리액트에서는 마운트, 업데이트, 언마운트라고 하며
- 여기서 마운트는 DOM이 생성되고 웹 브라우저 상에서 나타나는 것을 뜻하고, 반대로 언마운트는 DOM에서 제거되는 것을 뜻한다.
- 주의하여 볼 것은 업데이트 부분인데, 업데이트는 다음과 같은 4가지 상황에서 발생한다.
    1. props가 바뀔 때
    2. state가 바뀔 때
    3. 부모 컴포넌트가 리렌더링 될 때
    4. this.forceUpdate로 강제로 렌더링을 트리거할 때
### react 클래스형과 함수형의 차이

### 클래스형 :

- state, lifeCycle 관련 기능사용 가능하다.
- 메모리 자원을 함수형 컴포넌트보다 조금 더 사용한다.
- 임의 메서드를 정의할 수 있다.

### 함수형 :

- state, lifeCycle 관련 기능사용 불가능 *[Hook을 통해 해결 됨]*
- 메모리 자원을 함수형 컴포넌트보다 덜 사용한다.
- 컴포넌트 선언이 편하다.

### 타입스크립트란?

- 타입스크립트는 자바스크립트에 타입을 부여한 언어입니다.
- 타입을 지켜야 하기 때문에 의도하지 않은 코드의 동작을 예방할 수 있습니다.
- 타입스크립트의 또 다른 장점은 코드를 작성할 때 개발 툴의 기능을 최대로 활용할 수 있다는 것입니다.
- 요즘에 프런트엔드 개발을 할 때 가장 많이 사용되는 Visual Studio Code는 툴의 내부가 타입스크립트로 작성되어 있어 타입스크립트 개발에 최적화 되어 있습니다.

### Angular와 React의 차이점

- Angular와 React의 가장 큰 차이점은 Angular는 프레임워크(Framework)이고 React는 UI 구성요소 라이브러리라고 할 수 있습니다.
- 쉽게 표현하자면 React는 자체적으로 개발에 필요한 모든 요소들을 제공하지 않으며 제대로 활용하기 위해선 추가적인 구성이 필요하기 때문에 엄격히 말해 프레임워크라고 표현하지 않는다.

### SEO란?

- 검색엔진에서 더 찾기 쉽도록 사이트를 개선하는 프로세스
- **모바일 친화적인 페이지**
- **적절한 `<meta>`태그 사용**
- **유효한 HTML (Semantic Markup)을 사용**
- **이미지, 동영상, 구조화된 데이터에 관한 권장사항을 준수**
- **`<title>`, `<alt>` 속성이 구체적이고 정확한지 확인**

### 이벤트 위임이란?

- 이벤트 위임이란 하위 요소마다 이벤트를 붙이지 않고 상위 요소에서 하위 요소의 이벤트들을 제어하는 방식을 말한다.

### 메모이제이션이란?

- 메모이제이션 (Memoization) 이란 이름대로 메모 를 하는 것이 특징인데,
- 프로그래밍에서 반복되는 결과를 메모리에 저장 해놓고 다음에 같은 결과가 나올 때 다시 계산할 필요없이 빨리 실행 하는 기법이다.
- 마치 캐싱 과 같은 기능이라고 할 수 있다.

### 이벤트 버블링이란

- 이벤트 버블링은 특정 화면 요소에서 이벤트가 발생했을 때 해당 이벤트가 더 상위의 화면 요소들로 전달되어 가는 특성을 의미합니다.
- HTML요소는 트리 형식이죠? 그렇다면 그 랜딩페이지에서 <Body />가 최상위 요소가 됩니다. 그 밑으로 자식 요소들이 있죠.
- 브라우저는 이벤트를 하위 컴포넌트에서 상위 컴포넌트로 전파시키는 방식을 가집니다. 이 것을 ' 이벤트 버블링' 이라고 합니다.

### 부모에서 자식으로 이벤트상속방법

- 이벤트 캡처링으로 부모에서 자식으로 이벤트를 상속할 수 있습니다.
- 이벤트 캡처링은 이벤트 버블링과 반대로 상위 요소에서 **하위 요소로 탐색하며 이벤트를 전파**하는 방식입니다.
- 캡쳐링 단계에서 이벤트를 캐치하려면 ***addEventListener***의 세번째 파라미터를 정의할 수 있다.
- 기본적으로 ***default***는 ***false***인데, 이때 핸들러는 버블링 단계로 설정된다. 이벤트 캡쳐링은 흔히 사용 되지는 않지만 옵션을 `true`로 설정하면 이벤트 버블링과 반대 방향으로 탐색한다.

### 이벤트버블링을 막는 방법

- 이벤트를 멈추기 위해서는 최초로 이벤트가 발생되는 엘리먼트의 이벤트 핸들러에 event.stopPropagation()  라는 API 를 추가해주면 된다.
- 만약 하나의 이벤트에 여러 핸들러가 붙어 있는 경우event.stopPropagation() API를 추가 해도 다른 이벤트는 버블링 될 것이다.
- 모든 이벤트 버블링을 멈추고 싶은 경우에는 event.stopImmediatePropagation() API를 사용하도록 하자

### 이벤트버블링 활용 방법

- 정해진 액션에 따라서 다른 동작을 하는 여러 버튼에 대한 이벤트는 어떻게 처리해야할까 ? 모든 버튼에 대해서 이벤트 리스너를 등록하면 매우 비효율 적일 것이다.
- 해결 방법은 이벤트 위임 방식을 이용하여 공통 부모에 이벤트를 등록하고, 정해진 `data-action`에 따라서 다른 함수를 실행하는 것이다.

### React, 왜 사용하시나요?

- **Component 단위 작성**
    - **컴포넌트는 UI를 구성하는 개별적인 뷰 단위**로서, UI를 개발을 레고라고 한다면, 컴포넌트는 블록 역할을 하게 됩니다.
    - 이러한 특징은 **생산성과 유지 보수를 용이하게 합니다.**
    - 하나의 요소의 변화가 다른 요소들의 변화에 영향을 미치는 복잡한 로직을 업데이트하는 까다로운 작업에 경우, 컴포넌트의 재사용 기능으로서 보완할 수 있게 됩니다.
- **JSX**
    - JSX(Javascript + xml)는 자바스크립트에 대한 확장 구문으로서, 리액트에서 element(요소)를 제공해 줍니다.
    - 단순히 개발자가 마크업 코드에 익숙하다면, 그것만으로도 JSX를 통해 컴포넌트를 구성하는 데 쉽게 적응할 수 있다는 장점이 있습니다.
- **Virtual DOM**
    - 유저 인터랙션에 의해 View에 변화가 발생하여 10개의 노드를 수정해 주어야 한다면, 10번의 레이아웃 재계산, 10번의 리랜더링이 필요하다는 것입니다.
    - Virtual DOM은 변화가 발생하면, 실제 DOM에 적용되기 전에 Virtual DOM에 우선 적용을 시켜봅니다. 실제 DOM에 바로 적용하나, Virtual DOM에 적용하나 같은 연산 비용이 필요할 거라 생각하실 수 있지만, Vitual DOM은 랜더링 과정이 필요 없기 때문에 연산 비용이 실제 DOM보다 적습니다.
    - Virtual DOM에서 이러한 연산이 끝나고 나면, 최종적인 변화를 실제 DOM에 전달해줍니다. 즉, 10번의 작업을 하나로 묶어 딱 한 번 전달해 줍니다. 물론, 레이아웃 계산과 리랜더링하는 과정의 규모는 커지겠지만, 횟수를 줄이는 것으로 충분히 연산 비용을 적게 만들어 줍니다.
    - 또한, Virtual DOM은 어떤 게 바뀌었는지, 어떤 게 바뀌지 않았는지 자동으로 파악하여 필요한 DOM 트리만 업데이트할 수 있게 해줍니다.
