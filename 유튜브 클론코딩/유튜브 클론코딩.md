## html
- fontawesome
  - `<script src="https://kit.fontawesome.com/3dd9792e1f.js" crossorigin="anonymous"></script>`
  - head 태그안에 title 태그 다음에 넣어준다.
- title
  - `<title>`: 문서 제목 요소
  - HTML `<title>` 요소는 브라우저의 제목 표시줄이나 페이지 탭에 보이는 문서 제목을 정의합니다. 
  - 텍스트만 포함할 수 있으며 태그를 포함하더라도 무시합니다.
- header
  - HTML `<header>` 요소는 소개 및 탐색에 도움을 주는 콘텐츠를 나타냅니다. 
  - 제목, 로고, 검색 폼, 작성자 이름 등의 요소도 포함할 수 있습니다.
- section
  - `<section>`: 일반 구획 요소
  - HTML `<section>` 요소는 HTML 문서의 독립적인 구획을 나타내며, 더 적합한 의미를 가진 요소가 없을 때 사용합니다. 
  - 보통 `<section>`은 제목을 포함하지만, 항상 그런 것은 아닙니다.
- div
  - `.name1+.name2` 이런식으로 치고 엔터하면 div로 태그가 만들어집니다.
  - `<div>`: 콘텐츠 분할 요소
  - HTML `<div>` 요소는 플로우 콘텐츠를 위한 통용 컨테이너입니다. 
  - CSS로 꾸미기 전에는 콘텐츠나 레이아웃에 어떤 영향도 주지 않습니다.
  - `<div>` 요소는 "순수" 컨테이너로서 아무것도 표현하지 않습니다. 
  - 대신 다른 요소 여럿을 묶어 class나 id 속성으로 꾸미기 쉽도록 돕거나, 
  - 문서의 특정 구역이 다른 언어임을 표시(lang 속성 사용)하는 등의 용도로 사용할 수 있습니다.
- i
  - HTML `<i>` 요소는 텍스트에서 어떤 이유로 주위와 구분해야 하는 부분을 나타냅니다. 
  - 기술 용어, 외국어 구절, 등장인물의 생각 등을 예시로 들 수 있습니다. 
  - 보통 기울임꼴로 표시합니다.
- span
  - HTML `<span>` 요소는 구문 콘텐츠를 위한 통용 인라인 컨테이너로, 본질적으로는 아무것도 나타내지 않습니다. 
  - 스타일을 적용하기 위해서, 또는 lang 등 어떤 특성의 값을 서로 공유하는 요소를 묶을 때 사용할 수 있습니다. 
  - 적절한 의미를 가진 다른 요소가 없을 때에만 사용해야 합니다. 
  - `<span>`은 `<div>`와 매우 유사하지만, `<div>`는 블록 레벨 요소인 반면 `<span>`은 인라인 요소입니다.
- video
  - `<video>`: 비디오 삽입 요소
  - HTML `<video>` 요소는 비디오 플레이백을 지원하는 미디어 플레이어를 문서에 삽입합니다. 
  - 오디오 콘텐츠에도 사용할 수 있으나, `<audio>` 요소가 사용자 경험에 좀 더 적합합니다.
  - `<video>` 또한 `<img>` 요소와 비슷하게, 표시하고자 하는 `미디어로의 경로를 src 특성에 제공합니다.`
  - 또한 비디오의 너비와 높이, 자동재생과 반복 여부, 브라우저 기본 컨트롤 노출 여부 등 다른 정보도 특성을 통해 지정할 수 있습니다.
  - `<video></video>` 태그 안의 콘텐츠는 브라우저가 `<video>` 요소를 지원하지 않을 때 보여집니다.
- ul
  - HTML `<ul>` 요소는 정렬되지 않은 목록을 나타냅니다. 
  - 보통 불릿으로 표현합니다.
- li 
  - HTML `<li>` 요소는 목록의 항목을 나타냅니다. 
  - 반드시 정렬 목록(`<ol>`), 비정렬 목록(`<ul>`, 혹은 메뉴(`<menu>`) 안에 위치해야 합니다. 
  - 메뉴와 비정렬 목록에서는 보통 불릿으로 항목을 나타내고, 정렬 목록에서는 숫자나 문자를 사용한 오름차순 카운터로 나타냅니다.
- button
  - `<button>`: 버튼 요소
  - HTML `<button>` 요소는 클릭 가능한 버튼을 나타냅니다. 
  - 버튼은 양식 내부는 물론 간단한 표준 버튼 기능이 필요한 곳이라면 문서 어디에나 배치할 수 있습니다. 
  - 기본값의 HTML 버튼은 사용자 에이전트의 호스트 플랫폼과 비슷한 디자인을 따라가지만, 외형은 CSS로 변경할 수 있습니다.
- vscode skill `>`
  - `(li>button)*5`를 하면 `<li><button></button></li>`가 5개 만들어진다.
- vscode skill
  - 실제로 코딩할때 코드들을 숨기기해서 큰그림을 보며 코딩하도록 하자
- img
  - `<img>`: 이미지 삽입 요소
  - HTML `<img>` 요소는 문서에 이미지를 넣습니다.
  - src 특성은 필수이며, 포함하고자 하는 이미지로의 경로를 지정합니다.
  - alt 특성은 이미지의 텍스트 설명이며 필수는 아니지만, 스크린 리더가 alt의 값을 읽어 사용자에게 이미지를 설명하므로, 접근성 차원에서 매우 유용합니다. 
  - 또한 네트워크 오류, 콘텐츠 차단, 죽은 링크 등 이미지를 표시할 수 없는 경우에도 이 속성의 값을 대신 보여줍니다.



## 2:41 ~ 4:00
- 레이아웃 구조를 잘 잡아두자
- 변경사항을 최소한으로 줄이자
- 따라하고 싶은 사이트를 먼저 잘 박스별로 구분하자
- `<header>` HTML `<header>` 요소는 소개 및 탐색에 도움을 주는 콘텐츠를 나타냅니다. 제목, 로고, 검색 폼, 작성자 이름 등의 요소도 포함할 수 있습니다.

## 4:00 ~ 6:00
- 유튜브를 클론코딩하고 있으니 정보를 보여주는 공간이 몇개로 나뉘는지 확인해보자
- wireframe을 해보자
  - 미리 스케치북이나 종이에 설계도같이 어떤기능과 아이콘이 어디에 들어갈지 전반적인 구조를 잡는 것

## 6:00 ~ 8:00
- 그 다음 wireframe을 보고 레이블링하자
  - 각각의 큰 박스를 어떻게 부를건지, 각각의 아이템들을 어떻게 이름을 붙일건지
- HTML 빠르게 마크업하자, 준비물사이트 4가지

  - https://developer.mozilla.org/ko/docs/Web/HTML/Element

  - https://fontawesome.com/
 
  - https://material.io/resources/color/#!/?view.left=0&view.right=0

  - https://fonts.google.com/

- 먼저 youtube_mobile이라고 폴더를 만들고 index.html을 만든다.
- vscode에서 `!`치고 엔터하면 기본양식이 나온다.
- title은 원하는걸로 한다.
- 세멘틱을 최대한 쓰는 것이 좋다
  - body 태그 내에서 `header+section.player+section.info+section.upNext`하고 엔터하면 
  - 4개의 상자가 나누어진다.

## 8:00 ~ 10:00
- 우리가 처음 와이어프레임했을때 로고박스와 아이콘박스가 있었으므로 박스들을 나누어보자
- 헤더태그에서 `.logo+.icon`을 하고 엔터하면 2개의 박스로 나누어진다.
- 이제 로고 안에는 우리가 준비물사이트에서 찾은 `<i class="fab fa-youtube"></i>` 를 넣고
- `<span class="title">youtube</span>' 라고 넣어준다.
- 또한 icons에도 `<i class="fas fa-search"></i>` 와 `<i class="fab fa-ellipsis-v"></i>`를 넣어준다.
- 이제 지금까지 한내용을 구분하여 보기 쉽게 body태그 바로밑에 `<!-- Header -->` 를 넣어 주석처리해준다.
- 비디오기능을 사용하려면 준비물 사이트의 MDN에 들어가서 ctrl+f video를 하면 `<video>`를 들어갈 수 있다.
- 이 사이트에서 보면 다양한 기능들을 알 수 있고 설명들을 본다.
- 끝부분에서 제일 중요한 다양한 브라우저에서 사용가능한지 확인해본다.
- 넣고 싶은 아이콘을 font awesome에서 찾아 잘 넣어보자.

## 10:00 ~ 12:00
- 웹에 있는 링크를 넣어도 되지만 로컬에 있는 링크를 넣어보자.
- video폴더를 만들고 가지고있는 video를 넣어준다.
- 이제 우리가 앞에서 나누었던 section 박스안에다 `<video controls src="video/video.mp4"></video>`를 하면 된다.
- 자바스크립트를 배운다면 controls를 직접 만들어보는것도 좋다.
- 이제 비디오의 인포메이션을 넣을차례이다.
- 처음 나누었던 section class info에서 총 3개의 박스를 나눌것이다.
- `.metadata+.actions+.channel`로 유튜브를 보면 알 수 있지만 
- 영상정보, 좋아요싫어요액션기능, 채널정보 이렇게 3개로 나눈 것이다.



## 코드
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Youtube Mobile</title>
    <script 
        src="https://kit.fontawesome.com/3dd9792e1f.js" 
        crossorigin="anonymous">
    </script>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="logo">
            <i class="fab fa-youtube"></i>
            <span class="title">Youtube</span>
        </div>
        <div class="icons">
            <i class="fas fa-search"></i>
            <i class="fas fa-ellipsis-v"></i>
        </div>
    </header>

    <!-- Video Player-->
    <section class="player">
        <video controls src="video/video.mp4"></video>
    </section>

    <!-- Video info-->
    <section class="info">
        <!-- Metadata -->
        <div class="metadata">
            <ul class="hashtags">
                <li>#DreamCoding</li>
                <li>#DreamCoders</li>
                <li>#Ellie</li>
            </ul>
            <div class="titleAndButton">
                <span class="title">
                    클론코딩 유튜브 사이트 따라 만들기(HTML+CSS 연습편, 웹 포트폴리오) 
                    | 프론트엔드 개발자 입문편: HTML, CSS, Javascript
                </span>
                <button class="moreBtn">
                    <i class="fas fa-caret-down"></i>
                </button>
            </div>
            <div class="views">
                <span class="views">1M views 1 month ago</span>
            </div>
        </div>
        <!-- Actions -->
        <ul class="actions">
            <li>
                <button><i class="fas fa-thumbs-up"></i><span>1K</span></button>
            </li>
            <li>
                <button><i class="fas fa-thumbs-down"></i><span>0</span></button>
            </li>
            <li>
                <button><i class="fas fa-share"></i><span>Share</span></button>
            </li>
            <li>
                <button><i class="fas fa-plus"></i><span>Save</span></button>
            </li>
            <li>
                <button>
                    <i class="fab fa-font-awesome-flag"></i><span>Report</span>
                </button>
            </li>
        </ul>
        <!-- Channel Description -->
        <div class="channel">
            <div class="metadata">
                <img src="image/avatar.png" alt="">
                <div class="info">
                    <span class="name">드림코딩 by js</span>
                    <span class="subscribers">1M subscribers</span>
                </div>
            </div>
            <button class="subscribe">subscribe</button>
        </div>
    </section>
    <section class="upNext">
        <span class="title">Up next</span>
        <ul>
            <li class="item">
                <img src="image/kt.png" alt="">
                <div class="info">
                    <span class="title">kt 사이트를 반응형으로 만들어 볼꺼예요. 
                        순수 HTML, CSS를 이용해서 (Javascript 약간) 만들어 보고, 
                        다음에 Javascript를 배우면 동적으로 서버에서 데이터를 가져오는 
                        연습을 더 해보도록 할께요. (↙ 자세한 내용)</span>
                    <span class="name">드림코딩 by js</span>
                    <span class="views">82K views</span>
                </div>
                <button class="moreBtn"><i class="fas fa-ellipsis-v"></i></button>
            </li>
            <li class="item">
                <img src="image/sk.png" alt="">
                <div class="info">
                    <span class="title">sk 사이트를 반응형으로 만들어 볼꺼예요. 
                        순수 HTML, CSS를 이용해서 (Javascript 약간) 만들어 보고, 
                        다음에 Javascript를 배우면 동적으로 서버에서 데이터를 가져오는 
                        연습을 더 해보도록 할께요. (↙ 자세한 내용)</span>
                    <span class="name">드림코딩 by js</span>
                    <span class="views">82K views</span>
                </div>
                <button class="moreBtn"><i class="fas fa-ellipsis-v"></i></button>
            </li>
            <li class="item">
                <img src="image/lg.png" alt="">
                <div class="info">
                    <span class="title">lg 사이트를 반응형으로 만들어 볼꺼예요. 
                        순수 HTML, CSS를 이용해서 (Javascript 약간) 만들어 보고, 
                        다음에 Javascript를 배우면 동적으로 서버에서 데이터를 가져오는 
                        연습을 더 해보도록 할께요. (↙ 자세한 내용)</span>
                    <span class="name">드림코딩 by js</span>
                    <span class="views">82K views</span>
                </div>
                <button class="moreBtn"><i class="fas fa-ellipsis-v"></i></button>
            </li>
        </ul>
    </section>
    

</body>
</html>
```







