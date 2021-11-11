### `:root`
  - CSS `:root` 의사 클래스는 문서 트리의 루트 요소를 선택합니다 HTML의 루트 요소는 `<html>` 요소이므로, 
  - `:root`의 명시도가 더 낮다는 점을 제외하면 html 선택자와 똑같습니다. 
  - :root는 전역 CSS 변수 선언에 유용하게 사용할 수 있습니다.

### --white-color: #f9f9f9;
  - color를 미리 지정해줍니다. 
  - 크롬의 확장프로그램으로 색상을 따올수 있습니다. 
  - color picker

### css를 할때는 컬러나 사이즈 폰트사이즈를 미리해주면 좋다.
- header { } 를 하여 선택자를 header로 만들고 
- 그 안에 display: flex를 넣어 flex박스로 만든다. 
- 헤더야 너는 이제 플렉스박스야
- flex CSS 속성은 하나의 플렉스 아이템이 자신의 컨테이너가 차지하는 공간에 맞추기 위해 크기를 키우거나 줄이는 방법을 설정하는 속성입니다. 
- flex는 flex-grow, flex-shrink, flex-basis의 단축 속성입니다.

### header

```css
header {
  display: flex;
  justify-content: space-between;
  padding: var(--padding);
  background-color: var(--black-color);
  color: var(--white-color)
}
```

- 이렇게 넣을때 위에 썼던 `--padding`을 사용하므로써 일관성을 유지한다.
- 패딩과 백그라운드컬러, 컬러를 쓸때도 위에서의 설정값을 넣어 일관성과 유지보수를 쉽게한다.

### header 클래스 선택자
- `header .logo`를 하면 헤더내의 클래스네임 logo 만 바꿀수 있다.
- `header .logo i`를 하면 헤더안에 로고 안에 i 클래스만 바꿀 수 있다.
- 항상 오타를 조심하자.

### vscode에서 라이브서버
- 하려면 view에서 command pallete 에서 live server : open with live server를 클릭하면된다.

### 정리
- `.`이 붙으면 class=다음에 나오는 거고(클래스네임) 안 붙으면 태그이다.

### video
- `text-align: center;`를 하면 video도 가운데에 올 수 있게 한다.
- `position: sticky;` 와 `top: 0;`을 하면 유튜브 처럼 위에 고정할 수 있다.
