- "직접 DOM에 접근하는 것은 지양해야 한다.”는 말이 있습니다.
- 과연 DOM이 무엇이길래 이런 말이 있을까요?
- MDN에서는
    - *"DOM은 HTML, XML document와 상호작용하고 표현하는 API이다.*
    - *DOM은 browser에서 로드되며, Node(이하 노드) 트리(각 노드는 document의 부분을 나타낸다)로 표현하는 document 모델이다. (ex. element, 문자열, 혹은 코멘트)"*
- 라고 나와 있습니다.
- 위의 설명으로, Document는 HTML, XML을, Object는 노드 트리라 유추해볼 수 있습니다.
- 그렇다면 노드 트리는 무엇일까요?

![image](https://user-images.githubusercontent.com/87622597/197388169-5d59af5b-08f7-4885-93ef-891342160d40.png)
- 위의 그림에서 볼 수 있듯이 노드란 웹을 만들어본 사람이라면 다 알고 있는 HTML 태그들입니다.
- 가장 일반적인 노드 유형(nodeType)은 아래와 같습니다.
    - DOCUMENT_NODE (ex. `window.document`)
    - ELEMENT_NODE (ex. `<html>, <body>, <a>, <p>, <script>, <style>, <h1>`)
    - ATTRIBUTE_NODE (ex. `class="hi"`)
    - TEXT_NODE (ex. 줄바꿈과 공백을 포함한 HTML 문서 내의 텍스트)
    - DOCUMENT_FRAGMENT_NODE (ex. `document.createDocumentFragment()`)
    - DOCUMENT_TYPE_NODE (ex. `<!DOCTYPE html>`)
- 지금 사용하고 있는 브라우저에서 console에 Node를 치면 바로 위의 노드 유형들이 나옵니다.
- 그럼 내가 만든 HTML이 곧 DOM인가 보네? 라는 생각이 들 법하지만, 아쉽게도 그렇지 않습니다.
- 맨 처음에 MDN에서 설명했듯이, DOM은 브라우저에서 로드되는 것입니다.
- 각자의 IDE에서 작성한 HTML은 DOM이 아니고, 작성 된 HTML 문서가 브라우저에 의해 해석되어 실제 문서를 나타내는 노드 트리가 DOM입니다.
- 그리고 이러한 DOM은 자바스크립트로 해당 문서에 노드 추가, 삭제, 변경, 이벤트 처리, 수정 등을 가능케 하는 API를 제공합니다.
- 내가 아무리 나의 IDE에 HTML을 작성한다 한들, 최종적으로 이 결과물을 보기 위해 브라우저가 필요합니다.
- IDE에 작성된 HTML은 단순한 문자열(string)일 뿐이며, 브라우저가 이해하기 위해서는 노드(객체)로 변환해야 합니다.
- 즉 **DOM은 HTML과 자바스크립트를 이어주는 공간으로, 내가 작성한 HTML을 자바스크립트가 이해할 수 있도록 객체(object)로 변환**하는 것입니다.
- DOM은 내가 작성한 HTML로 부터 생성되지만, 브라우저가 알아서 필요한 노드들을 붙여줍니다.
- 예를 들어, `<head>`나 `<body>`없이 `<html>`안에 어떠한 내용을 작성을 하더라도, 브라우저로 열어보면 자동으로 생성되어 있습니다.
- 그리고 자바스크립트로 인해 새로운 노드를 추가할 수도 있습니다.

```jsx
const newTextDiv = document.createElement('div')
const helloWorld = document.createTextNode('Hello world!')
newTextDiv.appendChild(helloWorld)
document.body.appendChild(newTextDiv)
```

- 따라서, 자바스크립트를 DOM API라고 부르기도 합니다.
- 그렇다면 DOM이 어떻게 브라우저로 동작 되는 걸까요?

![image](https://user-images.githubusercontent.com/87622597/197388193-49599c49-7ac0-4b7f-b7d8-54525d41683f.png)
- 브라우저가 HTML을 전달 받으면, 곧 이를 변환(파싱)하고 노드들로 이루어진 DOM 트리를 만듭니다.
- 그 후, 외부의 CSS 파일과 각 노드들의 inline 스타일을 파싱하여 스타일을 입힌 Render 트리를 만듭니다.
- Render 트리가 만들이지면, 각 노드들이 화면에서 정확히 어디에 나타나야 하는지에 대한 위치가 주어집니다.
- 그 후, paint() 메서드를 호출하면 내가 구현하고 싶었던 화면이 출력됩니다.
- DOM은 해당 과정을 계속 반복합니다.
- 즉, 오타 수정, 문구 제거 혹은 이미지를 첨부하는 사소한 일을 하더라도, DOM은 처음부터 다시 HTML을 파싱하여 DOM 트리를 만들고 CSS를 파싱하여 Render 트리를 만들고, 레이아웃을 입혀 출력합니다.
- 2000년도 초만 하더라도 하나의 웹 사이트에 몇 페이지 없었을 테지만, 현재 대부분의 웹 사이트는 수 십개 심지어 수 백, 수 천개의 페이지로 이루어졌습니다.
- 겨우 오타 하나를 잡고 싶을 뿐인데, 전체 사이트를 다시 처음부터 렌더링(위의 결과물 출력 과정)을 해야 하며, 해당 오타를 찾기 까지 너무나 많은 시간이 들어가 상당히 비효율적입니다.
- 그래서 Virtual Dom이 나왔습니다.
- Virtual Dom(이하 가상 DOM)은 수정사항이 여러 가지 있더라도, 한 번만 렌더링을 일으킵니다.

![image](https://user-images.githubusercontent.com/87622597/197388198-aee869fd-8ef0-443b-90fb-685cb0c8dffc.png)
- 위의 그림처럼, 가상 DOM은 DOM이 생성되기 전, 이전 상태 값과 수정사항을 비교하여 달라진 부분만 DOM에게 한 번에 전달하여 **딱 한 번만 렌더링**을 진행합니다.

![image](https://user-images.githubusercontent.com/87622597/197388207-35553912-059f-46fa-939b-2b099b1ff0f3.png)
- 빨간 부분에 수정사항이 생겼다면(좋아요버튼 눌림), 가상 DOM이 알아서 달라진 값을 탐지하여 변경하고 최종적인 결과물을 실제 DOM에 전달합니다.
- 만약 가상 DOM이 없었다면, DOM은 렌더링을 처음부터 해야했기 때문에 모든 동그라미가 다 빨간색으로 바뀌었을 것입니다.
- "직접 DOM에 접근하는 것은 지양해야 한다."
- 이는 DOM에 직접 접근해도 문제가 되진 않지만, DOM이 직접 변경된다면 사소한 변경사항에도 전체가 리렌더링 되기 때문에 브라우저에 과부하가 올 수 있습니다.
- 따라서 최대한 DOM에 직접 접근하지 말아야 한다, 라고 이해하면 될 것 같습니다.
