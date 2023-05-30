# 글의 목적

- 면접에서 질문받았을 때를 대비하여 대답할 것을 정리한다.

# 레퍼런스

[[10분 테코톡] 헌치, 써머의 HTTP](https://www.youtube.com/watch?v=IjxkKQvn8Bc)

[HTTP 프로토콜이란?](https://shlee0882.tistory.com/107)

# 본문

http란 하이퍼텍스트 트랜스퍼 프로토콜의 약자로 인터넷상에서 데이터를 주고 받기 위한 통신 규약입니다.

즉 클라이언트와 서버사이에서 요청과 응답을 주고받는 과정인데요 이름의 유래는 하이퍼텍스트기반으로 데이터를 전송하겠다라른 뜻입니다.

작동은 클라이언트가 프로토콜, 위치, 자원명으로 서버의 자원에 접근하는 것인데 이는 우리가 브라우저의 주소창에 찾고자 하는 웹사이트의 주소를 적는것과 같습니다.

즉, 우리는 알게 모르게 이미 httpf를 통해서 서버와 통신을 주고받고 있던것입니다.

예를 들어 https://www.naver.com/index.html이라면 https라는 프로토콜로, naver라는 위치에 있는 곳에 index.html이라는 자원을 요청하는 것입니다.

이런 http프로토콜 방식에는 메시지를 전달하는 것이 있는데 메시지의 구성에는

메서드, 요청의 종류를 알려주는 것

프로토콜의 버전, 그리고 헤더가 있습니다. 

더 나아가 헤더에는 클라이언트가 어떤 브라우저를 쓰고 있는지, 언어는 무엇인지 같은 다양한 정보들이 담겨 있습니다.