### css 적용법
- html 파일내에 head안에 `<link rel="stylesheet" href="style.css">`를 넣어준다.

### font 적용법
- google font 가서 맘에 드는거 링크를 복사 한 후 그대로 html파일 내에 `<head>`안에 넣는다.
- 이후 css파일에서 body 내에 `font-family: Roboto;`를 넣어주면 된다.

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

### SASS & LESS
- sass 와 less 라이브러리를 쓰면 css 작성 코드를 줄일 수 있다.
- 헤더와 헤더내의 로고 그리고 i class를 바꿀때 일일이 헤더라고 쓰면 귀찮기 때문에 모아서 쓰는것이 sass와 less이다.

### 팁
- 이번에 해쉬태그를 고칠때처럼 무언가 고칠때는 클래스네임들을 다 적어서 확실하게 해두자
- ex) .info .metadata .hashtags
- CSS Background-color 투명 or 배경 없애기 background-color:transparent;
- 항상 안전하게 상위 태그나 상위 클래스네임을 꼭 적어서 확실하게 하자
- `>` 자식노드 셀렉터를 이용하면 밑에 다른 중복되는 클래스네임이 있어도 바로 따라오는 클래스네임만 적용시킨다.

### javascript
- `<script src="main.js" defer></script>`코드를 head태그 내에 넣는다.
- 이후 main.js를 만들어 사용자와의 상호작용 코드를 넣어주면 여러가지를 구현할 수 있다.
- 다음에 자바스크립트를 배우면 실전으로 써보자.


## 코드
```css
:root {
  /* Color */
  --white-color: #f9f9f9;
  --black-color: #121212;
  --blue-color: #065fd4;
  --red-color: #f00;
  --grey-dark-color: #909090;
  --grey-light-color: #e0e0e0;

  /* Size */
  --padding: 12px;
  --avatar-size: 36px;

  /* Font Size */
  --font-large: 18px;
  --font-medium: 14px;
  --font-small: 12px;
  --font-micro: 10px;
}

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

body {
  font-family: Roboto;
}

ul { 
  list-style: none;
}

button,
button:focus {
  border: none;
  cursor: pointer;
  outline: none;
  background-color:transparent;
}

/* Header */
header {
  display: flex;
  justify-content: space-between;
  padding: var(--padding);
  background-color: var(--black-color);
  color: var(--white-color)
}

header .logo {
  font-size: var(--font-large);
}

header .logo i{
  color: var(--red-color);
}

header .icons .fa-search {
  margin-right: var(--padding)
}

/* Video Player */
.player{
  position: sticky;
  top: 0;
  text-align: center;
  background-color: var(--black-color);
}
.player video {
  width: 100%;
  height: 100%;
  max-width: 1000px;
}

.info {
  padding: var(--padding);
}

.info .metadata .hashtags {
  display: flex;
  font-size: var(--font-small);
  color: var(--blue-color);
}

.info .metadata .hashtags li {
  margin-right: var(--padding);
}

.info .metadata .titleAndButton {
  display: flex;
}

.info .metadata .titleAndButton .title {
  font-size: var(--font-medium);
  margin-right: var(--padding);
}

.info .metadata .titleAndButton .title.clamp{
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
}

.info .metadata .titleAndButton .moreBtn {
  height: 100%;
  transition: transform 300ms ease-in-out;
}

.info .metadata .titleAndButton .moreBtn.clicked {
  transform: rotate(180deg);
}

.info .views {
  font-size: var(--font-small);
  color: var(--grey-dark-color);
}

/* Action Buttons */
.info .actions {
  display: flex;
  justify-content: space-around;
  margin: var(--padding) 0;
}

.info .actions button {
  display: flex;
  flex-direction: column;
  font-size: var(--font-small);
  color: var(--grey-dark-color)
}

.info .actions button i {
  margin: 0 auto;
  margin-bottom: calc(var(--padding)/2);
  font-size: 16px;
}

.info .actions button i.active {
  color: var(--blue-color);
}

/* Channel Description */
.channel {
  display: flex;
  justify-content: space-between;
  border-top: 1px solid var(--grey-light-color);
  border-bottom: 1px solid var(--grey-light-color);
}

.channel .metadata {
  display: flex;
  align-items: center;
}

.channel .metadata .info {
  display: flex;
  flex-direction: column;
}
.channel .metadata img {
  width: var(--avatar-size);
  height: var(--avatar-size);
  border-radius: 50%;
}

.channel .metadata .info .name {
  font-size: var(--font-medium);
}

.channel .metadata .info .subscribers {
  font-size: var(--font-small);
  color: var(--grey-dark-color);
}

.channel .subscribe {
  text-transform: uppercase;
  color: var(--red-color);
  font-size: var(--font-medium);
}

/* Up Next */
.upNext {
  padding: 0 var(--padding);
}

.upNext > .title {
  font-size: var(--font-medium);
  color: var(--grey-dark-color);
  margin-bottom: calc(var(--padding) / 2);
}

.upNext .item {
  display: flex;
  margin-top: var(--padding);
}

.upNext .item .img {
  flex: 1 1 35%;
  margin-right: var(--padding);
}

.upNext .item .img img{
  width: 100%;
}

.upNext .item .info {
  flex: 1 1 60%;
}

.upNext .item .moreBtn {
  height: 100%;
  flex: 1 1 5%;
}

.upNext .item .info {
  display: flex;
  flex-direction: column;
}

.upNext .item .info .title {
  font-size: var(--font-small);
}

.upNext .item .info .name, 
.upNext .item .info .views {
  font-size: var(--font-micro);
  color: var(--grey-dark-color);
}

.infoAndUpNext {
  display: flex;
  flex-direction: column;
}

@media screen and (min-width: 768px){
  .infoAndUpNext {
    flex-direction: row;
    margin: var(--padding) 0;
  }
}
```

```javascript
const moreBtn = document.querySelector('.info .metadata .moreBtn');
const title = document.querySelector('.info .metadata .title');

moreBtn.addEventListener('click', () => {
  moreBtn.classList.toggle('clicked');
  title.classList.toggle('clamp');
});
```
