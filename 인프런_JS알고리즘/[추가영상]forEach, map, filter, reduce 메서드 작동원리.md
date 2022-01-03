```jsx
//forEach
//forEach, map, filter, reduce
            function forEach(predicate, thisArg){
                for(let i=0; i<a.length; i++){
                    predicate(a[i],i);
                }
            }
            a=[10,11,12,13,14,15];
            a.forEach(function(v,i){
                console.log(v, i, this);
            }, [1,2]);

//map
//forEach, map, filter, reduce
            function map(predicate, thisArg){
                let list=[];
                for(let i=0; i<a.length; i++){
                    list.push(predicate(a[i], i));
                }
                return list;
            }
        
            a=[10,11,12,13,14,15];
            let answer=a.map(function(v, i){
                if(v%2==0) return v;
            }, [1,2]);
            console.log(answer);

//filter
//forEach, map, filter, reduce
            function filter(predicate, thisArg){
                let list=[];
                for(let i=0; i<a.length; i++){
                    if(predicate(a[i], i)) list.push(a[i]);
                }
                return list;
            }
        
            a=[10,11,12,13,14,15];
            let answer=a.filter(function(v, i){
                return v%2==1;
            }, [1,2]);
            console.log(answer);

//reduce
//forEach, map, filter, reduce
            function reduce(predicate, val){
                let result=val;
                for(let i=0; i<a.length; i++){
                    result=predicate(result, a[i]);

                }
                return result;
            }
        
            a=[10,11,12,13,14,15];
            let answer=a.reduce(function(acc, v){
                return acc+v;
            }, 0);
            console.log(answer);
```

📌for Each

강사님은 자바스크립트에 그렇게 빠삭하지는 않다.

`a=[10,11,12,13,14,15];` 

일때 호출하려면 a.forEach()를 하면된다.

이 forEach는 function forEach(predicate, thisArg)

얘는 매개변수가 두개이다. 함수를 받는다. 4개의 메서드들은 다 고차함수이다. 고차함수는 함수를 매개변수로 전달받는다.

thisArg는 arg로 쓸애를 전달받는다. thisArg는 전달받지 않아도 된다.

predicate는 인자로 콜백함수를 받아야한다. 

매개변수로 주는 함수를 콜백함수라고 한다.

함수는 이미 빌트인 되어서 복잡하게 만들어져있지만 이해를 위해 뇌피셜로 한번 써보자면

for반복문을 이용해서 배열에 들어가지말고 forEach를 써보자

forEach는 for문 대신 쓰는것이다. forEach는 요소를 탐색해야한다.

forEach가 배열의 요소를 하나하나 방문하면서 콜백함수를 실행한다. (predicate) 호출한 배열요소를 하나하나 방문하면서 

predicate(a[i], i); ←이 함수를 호출한다.

예를 들어 a.forEach(function(v,i){});  일때 v가 a[i]이고 i는 i이다.

콘솔로그로 콜백함수를 하여 찍어보면 10 0 11 1 12 2 13 3 14 4 15 5가 찍힌다. forEach내부에 코드를 짤때 forEach라는 함수를 짜는게 아니라 콜백함수의 내부를 짜는것이다. 또 a.forEach(){},[1,2]);이면 [1,2]가 thisArg이다.

자바스크립트는 함수형 프로그래밍이다. 

📌map

map은 원본배열을 하나씩 탐색하면서 새로운 배열을 생성한다.

map은 새로운 빈 배열을 하나 만들고 for문이 돌면서 predicate라는 콜백함수를 호출해서 리턴된값을 받아서 새로운 배열의 원소로 하는 새로운 배열을 만든다. 만약 if(v%2 == 0) return v;이면 10 12 14 만 배열로 만들거같지만 6번 탐색하면서 무조건 6번 push해서 길이가 서로 같다. 그래서 콜백함수로 받지 못하면 undefined를 반환한다. 

map은 원본배열들의 요소를 이용해서 새로운 배열을 만든다.

📌filter

filter는 맵과 비슷하지만 원하는 원소만 리턴해준다.

콜백함수가 참인 요소들만 리턴한 요소들만 반환한다. ←맵과는 다른부분

필터는 원본배열들에서만 뽑아낸다. 요소만 뽑아낸다.

새로운 배열을 만들고 콜백함수를 반복호출한다.

원본배열의 요소만 새 리스트에 넣어 반환한다.

📌reduce

reduce는 뭔가 받아서 배출하는데 뭔가를 리턴받는데 배열을 생성하거나 쓰는게 아니라 값을 반환한다.

reduce는 let result=val;이다. 원본배열을 하나씩 탐색하면서 콜백함수를 호출하는 건 다 같다. result=predicate(result, a[i]);

reduce는 콜백함수에서 리턴한 값이 다시 누적되어 돌아온다.

리턴한값이 다시 누적되어 입력값으로 들어간다. 두번째 인자는 초기값이다. reduce는 배열의 합을 구할때 많이 쓴다. 알고리즘에서 sum으로 쓴다.

return acc+v;
