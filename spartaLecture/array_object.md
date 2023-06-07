# 글의 목적

면접을 대비해서 대답할 수 있도록 정리한다.

# 레퍼런스

[배열, 객체를 const로 선언했는데 요소나 속성을 추가할 수 있는 이유?](https://intothenight.tistory.com/15)

# 본문

Const 변수에 할당된 값은 바뀌지 않지만, 배열/객체가 변수에 할당될 때에는 배열/객체의 요소(값) 자체가 아니라 주소(이 값은 불변, 상수)가 할당되기 때문입니다.

const는 변하지 않는 상수*constant* 를 선언하는 키워드이며, 이 상수의 값은 재할당할 수 없으며 다시 선언할 수도 없습니다.

그러나 배열, 객체는 참조자료형*reference data type*이며, 참조 값은 변수에 주소를 할당합니다. (cf. 변수에 값을 직접 할당하는 원시자료형*primitive data type*)

숫자, 문자열 등의 원시 자료형은 stack 영역**에 값 자체가 저장되지만 배열, 객체, 함수 등의 참조자료형은 heap 영역**에 값이 저장되고, stack에는 heap에 저장된 데이터의 주소만 저장됩니다.

실제 heap 내에 저장되어 있는 배열, 객체 내의 요소를 변경***하더라도, 참조된 주소는 변하지 않으므로 const 사용이 가능합니다.

- stack 영역: parameters, automatic and temporary variables / 함수의 호출과 관계되는 지역 변수와 매개변수가 저장되는 영역
- * heap 영역: dynamically allocated variables / 사용자에 의해 직접 동적으로 할당되고 해제되는 메모리 공간
- ** 배열 - push, pop / 객체 - shift, unshift
