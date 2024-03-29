# 글의 목적

면접 대비 정리

# 레퍼런스

[🔍 [단골질문] - 01. 브라우저 저장소에 대해서 설명해보세요.](https://velog.io/@cjh951114/단골질문-01)

# 본문

로컬스토리지와 세션스토리지는 간단한 key와 value를 저장할 수 있는 저장소이다.

이 저장소들은 브라우저에 저장하기 떄문에 새로고침을 해도 데이터가 휘발되지 않는다는 특징이 있는 데 

이를 이용해 프론트엔드에서는 로그인시 access token을 로컬스토리지에 저장하고 로그인을 유지하는데 사용할 수 있다.

또한 redux-persist를 사용하면 클라이언트 자체에서 새로고침이나 창을 닫았을 시에도 휘발되지 않게 유저의 정보를 저장할 수 있다.

세션스토리지의 경우는 로컬과는 조금 차이가 있는게 윈도우나 창을 닫으면 그 정보가 사라진다.

그리고 이 로컬과 세션 스토리지 전에 있던 것이 쿠키인데 쿠키는 만료기간이 있는 저장소라고 생각하면 좋다.

따라서 이 각각의 저장소는 목적에 따라 쓰여지는데 정리하자면 다음과 같다.

- 자동 로그인 -> 로컬스토리지
- 입력 폼 정보 -> 세션스토리지
- 비로그인 장바구니 -> 세션스토리지
- 다시 보지 않음 팝업 창 -> 쿠키
