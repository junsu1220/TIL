# 글의 목적

면접 대비해서 대답할 수 있도록 정리함

# 레퍼런스

[📚 require vs import 문법 비교 (CommonJS vs ES6)](https://inpa.tistory.com/entry/NODE-📚-require-⚔️-import-CommonJs와-ES6-차이-1)

[모듈 소개](https://ko.javascript.info/modules-intro)

# 본문

require는 NodeJS에서 사용하고 있는 CommonJS키워드이고 import는 ES6에서 새롭게 도입된 키워드이다.

즉 require는 서버에서 사용하는 모듈시스템에서의 모듈을 불러오는 문법이고 import는 브라우저에서 사용하는 모듈시스템에서의 모듈을 불러오는 문법이다.

require는 프로그램의 어느 지점에서나 호출 할 수 있지만 import는 파일의 시작 부분에서만 실행할 수 있다.

일반적으로 import는 사용자가 필요한 모듈 부분 만 선택하고 로드 할 수 있기 때문에 더 선호된다. 또한 require보다 성능이 우수하며 메모리를 절약한다.

개발하는 애플리케이션의 크기가 커지면 언젠간 파일을 여러 개로 분리해야 하는 시점이 온다. 

이때 분리된 파일 각각을 '모듈(module)'이라고 부르는데, 모듈은 대개 클래스 하나 혹은 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성된다.

모듈은 단지 파일 하나에 불과하다.

스크립트 하나는 모듈 하나이다.

모듈에 특수한 지시자 `export`와 `import`를 적용하면 다른 모듈을 불러와 불러온 모듈에 있는 함수를 호출하는 것과 같은 기능 공유가 가능하다.
