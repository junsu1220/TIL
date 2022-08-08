## 인증이 필요한 이유

웹 사이트의 모든 사용자가 모든 콘텐츠에 접속할 수 있어야 하는 것은 아닙니다. 이러한 **콘텐츠에 대한 접근을 "인증(Authentication)"을 통해 보호**할 수 있습니다. 예를 들면, 사용자 프로필 페이지는 로그인한 사용자만이 접근할 수 있도록 되어야 합니다.

페이지 뿐만 아니라 데이터베이스에 저장되어 있는 데이터도 보호되어야 합니다. 예를 들어, 비밀번호를 변경하는 요청을 서버에게 보낼 때 이는 데이터베이스의 사용자 비밀번호를 업데이트하는 것입니다. 이러한 **URI(API Endpoint)요청에 대한 동작은 인증을 받은 사용자만 접근을 허용하도록, 즉 인증을 받지 않은 사용자들은 접근할 수 없도록 제한**되어야 합니다.만약 URI이 제한되지 않았다면 이 URI을 아는 사용자라면 누구라도 비밀번호를 바꾸는 요청 보낼 수 있으므로 다른 사용자의 비밀번호를 변경할 수도 있게됩니다.

즉, 서버측에서는 클라이언트에게 전달받은 요청에 대해서 인증을 받은 사용자인지 검사를 한 뒤에 인증을 받은 사용자에게만 요청에 대한 응답을 클라이언트에게 전달해주도록 동작해야 합니다.

## 인증이 동작하는 방식

**인증을 얻는 방법으로 "로그인"**이 있습니다. 로그인을 위한 제출 버튼을 누르면 계정과 비밀번호가 서버로 보내지고, 서버는 연결된 데이터베이스에 저장된 계정과 비밀번호를 확인한 뒤에 사용자 유효성이 입증되면 서버가 클라이언트에게 인증을 응답으로 제공하게 됩니다.

클라이언트는 서버로부터 응답받은 인증을 매 요청마다 같이 전달합니다. 그러면 서버측에서는 요청이 유효한지 검사하여 사용자에게 보호된 리소스에 대한 접근을 허용하게 됩니다.

이때 서버측에서 브라우저(클라언트)에게 전달하는 응답으로 "접근 가능" 혹은 "접근 불가능"이라는 단순한 응답으로는 충분하지 않습니다. 이는 인증받지 않은 사용자가 보호된 리소스에 대한 요청을 서버에게 보낼 때 임의로 "접근 가능"이라고 요청을 보낼 수 있기 때문에 **인증의 형태가 정교하게 구성되어야 합니다.**

**즉, 서버가 클라이언트측에 전달하는 응답은 단순한 "접근", "접근 불가"보다는 복잡한 과정을 가져야 합니다.**

## Http 통신의 특징 & Cookies

먼저 이에 대해 알아보기 전에 "HTTP 통신의 특징"과 "Cookie", "Session"에 대해서 간략하게 설명하겠습니다.

- HTTP는 **"Stateless(무상태성)"** 하고 **"Connectionless(비연결성)"** 합니다. 이는 Connectionless한 성질 때문에 Stateless 해진다고 생각하면 됩니다.클라이언트가 서버에게 요청을 보내고, 서버가 그에 대한 응답을 클라이언트에게 보내면 접속이 끊어집니다. 이는 **요청에 대한 응답을 처리하게 되면 연결이 끊어져(Connectionless) 이전 정보나 현재 통신의 상태가 남아있지 않습니다(Stateless).즉, 연결 상태가 유지되지 않기** 때문에 클라이언트는 서버에게 **매요청을 할 때마다 "연결 상태를 유지하기위한 정보(인증)를 추가적으로 전달"**해주어야 합니다.
- Cookie : **"서버가 클라이언트에게 전달하는 정보(데이터)"**입니다. 그리고 쿠키는 브라우저가 서버에게 어떤 요청을 보낼 때마다 **서버는 클라이언트가 요청한 정보(Payload)와 함께 쿠키를 응답으로 보냅니다.** 그리고 **브라우저가 갖고 있는 이 쿠키는 서버에게 요청을 보낼 때 같이 전달**됩니다.
- Session : HTTP는 Stateless(무상태성)하고 Connectionless(비연결성)합니다. 이러한 특징으로 인해서 **클라이언트와 서버간 상태를 유지하기 위해서 "Session"을 사용**하게 됩니다. 즉, **Session이란 서버와 클라이언트간 상태 정보를 유지하기 위한 기술**이라고 볼 수 있습니다.

인증을 위한 두 가지 접근법이 존재합니다. **"Server-side Sessions(세션)"** 혹은 **"Authentication Tokens(인증 토큰)"**을 사용할 수 있습니다.

## Session

세션은 인증을 처리하는 아주 전통적인 접근법입니다. 세션은 서버가 사용자(브라우저)에게 접근권을 줄 때 서버가 **사용자를 위한 "고유한 식별자(Session ID)"** 를 만들고 서버에 저장합니다. 즉, 모든 웹사이트 방문자는 **인증을 받으면 각 사용자의 고유한 식별자인 Session ID가 서버에 저장**됩니다.이 Session ID는 서버에게만 저장되는 것이 아니고 **사용자에게도 쿠키로 전달**됩니다. 따러서 서버의 응답은 단순한 "접근", "접근 불가"만이 아니라 Session ID도 포함됩니다. 그리고 **사용자가 서버에게 요청을 보낼 때는 Session ID와 함께 보내면 서버측에서는 갖고 있는 Seesion ID와 일치하는지 검사하여 접근할 수 있는지 검사합니다.** 만약 브라우저가 전달한 Session ID가 서버가 갖고 있는 Session ID와 일치하지 않는다면 접근 요청을 거부하게 됩니다.

## Authentication Token

기본적인 개념은 같습니다. 계정과 비밀번호를 서버에 보내면 서버가 데이터베이스에 저장된 이메일과 비밀번호를 비교해서 유효성을 인증합니다. **유효성이 입증되면 서버가 "인증 토큰"을 만들게 됩니다.**

인증 토큰이라는 것은 아주 **"긴 문자열 형태"이며 데이터가 문자열로 인코딩되어 있습니다.** 서버는 데이터를 인코딩할 때 특정 알고리즘(암호화 알고리즘)으로 **서버만이 갖고 있는 key를 사용하여 인증 토큰을 생성**합니다.

다시 말해, 서버가 인증 토큰을 만들 때 **서버만이 알고 있는 "key"를 갖고 특정 알고리즘을 사용하여 데이터를 문자열로 인코딩**하게 됩니다. 토큰을 만드는 과정에 포함되는 **키는 서버만이 알고 있기 때문에 사용자는 토큰 디코드하거나 어떻게 생성되었는지는 알 수 없습니다.** 그리고 생성된 토큰은 서버에 저장되지 않고 단지 사용자에게 전달됩니다.

사용자는 서버에게 요청을 보낼 때 인증 토큰도 함께 전달합니다. 토큰을 받은 서버는 자신이 갖고 있는 키를 이용하여 디코드합니다. 그리고 토큰이 유효한 경우에 리소스에 대한 접근을 허용하게 됩니다. 이는 앞선 Session 방식처럼 **서버측에서 각 사용자마다 고유한 Session ID를 갖고 있지 않아도 됩니다.**

서버가 인증 토큰을 응답으로 보냈다는 것은 사용자가 유효하다는 의미입니다. 만약 유효하지 않은 사용자라면 서버측에서는 인증 토큰 자체를 전달해주지 않을 것입니다. 따라서 우리는 **서버가 응답한 인증 토큰의 존재 유무를 사용자가 인증이 되었다는 근거로 사용**할 수 있습니다.

## Firebase Auth Rest API

Firebase에서 제공하는 인증 토큰을 이용하여 제한된 리소스에 접근하는 방법에 대해서 알아보겠습니다.

1. Firebase 페이지의 Authentication에 들어갑니다.
    
    ![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F1dddaa4f-b23c-4e9d-8a05-c08e227c3ae8%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2017.28.52.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F1dddaa4f-b23c-4e9d-8a05-c08e227c3ae8%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2017.28.52.png)
    
2. 인증을 받는 방식을 선택합니다. 여기서는 이메일/비밀번호로의 인증 방식을 사용하겠습니다.
    
    ![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Fa0a6aae7-b9b5-4d1f-bb0d-57ed1d629488%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2017.30.05.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Fa0a6aae7-b9b5-4d1f-bb0d-57ed1d629488%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2017.30.05.png)
    
    ![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F1d9c32e6-282d-495b-a4c0-f218acb59925%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2017.31.50.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F1d9c32e6-282d-495b-a4c0-f218acb59925%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2017.31.50.png)
    

---

[Firebase Auth Rest API](https://firebase.google.com/docs/reference/rest/auth) 문서에서 Authentication Rest API 문서를 참조하여 인증 토큰을 발급받는 방식에 대해서 알아보겠습니다.

### 아이디 / 비밀번호로 가입

사용자 아이디를 데이터베이스에 추가하기 위해서 아래 API 문서를 참조하면

![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F3dcbd62c-2c56-4398-b517-9a56773d73c4%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2017.38.41.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F3dcbd62c-2c56-4398-b517-9a56773d73c4%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2017.38.41.png)

- Http 요청 메서드는 POST 방식
- 요청 몸체의 MIME Type은 applicaiton/json
- API의 URI는 `https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=[API_KEY]`여기서 [API_KEY] 부분은 자신이 부여받은 웹 API 키로 치환하여 작성합니다. 자신의 웹 API 키는 프로젝트 설정에서 확인할 수 있습니다.

![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Fbbf67208-6061-4cdc-bef8-ca5d046e3276%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2017.49.45.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Fbbf67208-6061-4cdc-bef8-ca5d046e3276%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2017.49.45.png)

요청 몸체의 구성과 응답되는 응답 객체의 구성이 위와 같습니다.

```
,,,
const createUserRequest = async () => {

    try {
        const response = await fetch("https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=자신의웹API키", {
                method: 'POST',
                body: JSON.stringify({ email: enteredEmail, password: enteredPassword, returnSecureToken: true }),
                headers: {
                    'Content-Type': 'application/json'
                }
        });

        const data = await response.json();

        if(data.error && data.error.message) {
            throw new Error(data.error.message);
        }

        console.log(data);

    } catch(error) {
        console.log(error);
    }
};
```

만약 성공적으로 사용자 추가가 완료된다면 응답으로 아래와 같은 객체를 전달받습니다.

![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Fa5abc710-2042-4384-949a-d0042844de65%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-12%2002.00.43.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Fa5abc710-2042-4384-949a-d0042844de65%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-12%2002.00.43.png)

만약 에러가 발생한다면 다음과 같은 에러 객체를 전달받습니다.

![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Fb19d3619-a348-4306-badb-d760943c8fd7%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-12%2002.00.13.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Fb19d3619-a348-4306-badb-d760943c8fd7%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-12%2002.00.13.png)

그리고 Firebase Authentication에서 추가된 사용자를 확인할 수 있습니다.

![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Fe3f3241f-4c0a-4830-b547-2f52a6b24b0e%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2018.41.07.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Fe3f3241f-4c0a-4830-b547-2f52a6b24b0e%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2018.41.07.png)

### 로그인 하기

이메일 / 패스워드로 로그인하는 API 문서는 다음과 같습니다.

![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F5a5c9420-7acc-4b0d-a89f-58c24a64e790%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2019.25.11.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F5a5c9420-7acc-4b0d-a89f-58c24a64e790%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2019.25.11.png)

- Http 요청 메서드는 POST
- 요청 몸체의 MIME Type은 application/json
- API의 URI는 `https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=[API_KEY]`입니다.

![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F163c903c-e617-4103-b435-c9fe58c45e6e%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2019.27.09.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F163c903c-e617-4103-b435-c9fe58c45e6e%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2019.27.09.png)

그리고 전달해야하는 요청 몸체와 응답으로 전달받는 응답 객체는 위 그림과 같습니다.

```
const LoginRequest = async () => {
    try {
        const response = await fetch('https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=자신의웹API키', {
            method: 'POST',
            body: JSON.stringify({
                email: enteredEmail,
                password: enteredPassword,
                returnSecureToken: true
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });

        const data = await response.json();

        if(data.error && data.error.message) {
            throw new Error(data.error.message);
        }

        console.log(data);

    } catch(error) {
        console.log(error);
    }
};
```

만약 로그인이 성공적이라면 아래와 같은 응답 객체가 전달되고

![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Fbd404ca9-291b-470a-8630-57bfc5ab525f%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-12%2001.50.43.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Fbd404ca9-291b-470a-8630-57bfc5ab525f%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-12%2001.50.43.png)

로그인에 실패한다면 아래와 같은 응답 객체가 전달됩니다(비밀번호 잘못 입력한 경우).

![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Ff2c8cc62-165f-4034-af59-c608ede16dce%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-12%2001.51.19.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Ff2c8cc62-165f-4034-af59-c608ede16dce%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-12%2001.51.19.png)

### 페이지 접근 제한하기

비밀번호 변경 페이지, 프로필 페이지 등 인증을 받아야 접근이 가능하도록 만들어 주어야하는 페이지들이 있습니다. 즉, 인증이 된 상태에서만 접근 가능하도록 만들어주어야 합니다.

우리는 로그인을 성공적으로 완료한 경우 firebase가 전달해주는 응답 객체에 idToken을 통해서 인증 토큰을 사용할 수 있습니다.

참고로 서버에게 전달받은 **인증 토큰은 만료 기간이 존재**합니다. 이는 **응답의 일부로 만료 기간을 알 수 있습니다.** 로그인을 하면 서버측에서 응답을 브라우저에게 전달할 때 토큰과 함께 **토큰의 만료 시간을 초 단위로 전달**합니다. Firebase 인증 토큰의 경우 인증 토큰의 만료 기간은 한 시간입니다. 아래 그림의 응답 객체의 **expiresIn 프로퍼티에 만료 시간을 초단위로 갖고 있습니다.**

![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F02fb2a0a-2a1a-4345-b890-4956336c0c4d%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2019.55.45.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F02fb2a0a-2a1a-4345-b890-4956336c0c4d%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-11%2019.55.45.png)

서버에게 전달받은 인증 토큰(idToken)이 존재하는 경우에만 Route 컴포넌트를 조건부로 추가해주는 방식으로 접근을 제한할 수 있습니다.

Route 컴포넌트 또한 컴포넌트이므로 일반적인 컴포넌트처럼 조건부 렌더링이 가능합니다.

```
<Routes>
    <Route path='/' element={<HomePage />} />
    <Route path='/auth' element={<AuthPage />} />
    // idToken이 빈문자열인 경우 UserProfile 컴포넌트는 렌더링되지 않음
    {idToken && <Route path='/profile' element={<UserProfile />} />}
<Routes>
```

위 코드처럼 경로가 `/profile`일 때 UserProfile 컴포넌트를 렌더링하는 Route 컴포넌트가 활성화 됩니다. 단, token, 즉 인증 토큰이 존재하는 경우에만 Route 컴포넌트가 추가되므로 일반적으로 주소창에 `/profile`을 입력하더라도 UserProfile 컴포넌트를 렌더링하는 Route 컴포넌트가 활성화 되지 않습니다.

### 사용자 인증 상태 유지하기

현재 페이지를 리프레시하거나 브라우저 주소창에 URL을 입력하면 인증 상태를 잃어버리게 됩니다. 이는 리액트 앱을 다시 시작하기 때문에 인증 상태를 잃어버리는 것은 당연합니다.

우리는 적어도 한 시간 동안은 로그인 상태를 유지하기 위해서 인증 토큰을 리액트 앱 바깥 어딘가에 저장해야 한다는 의미입니다. 이때 우리는 **브라우저의 저장 메커니즘인 cookie, localStorage 등**을 사용하여 인증 상태를 저장하여 유지해야 합니다.

**브라우저 저장소**를 이용하여 페이지가 로드될 때 저장소를 확인하여 토큰이 존재하면 해당 토큰을 초기값으로 사용하여 로그인 상태를 유지하도록 구현합니다. 그리고 **만료 시간(expiresIn)도 브라우저 저장소에 저장하여 만료 시간이 지난 경우 자동적으로 로그아웃**되도록 구현합니다.

---

인증 상태는 여러 컴포넌트에서 사용되는 데이터이므로 **전역 상태로 관리하기 위해서 Context API나 Redux를 사용**하여 인증 토큰을 애플리케이션 전체에서 사용할 수 있도록 만들어야 합니다. 아래 예제에서는 Redux를 사용하여 인증 토큰을 전역 상태로서 관리하겠습니다.

그리고 브라우저 저장소인 localStroage에 인증 토큰을 저장하여 인증 상태를 유지하는 코드를 작성해보겠습니다. 아래는 localStroage의 메서드입니다.

- `localStroage.setItem(key, value)`: localStorage에 key-value 쌍을 저장합니다. 참고로 localStroage에는 **원시값(숫자, 문자, 불리언 등)만 저장가능**합니다. **객체를 저장하기 위해서는 `JSON.stringify` 메서드로 직렬화한 후에 저장**이 가능합니다.
- `localStrorage.removeItem(key)`: localStroage에 인수로 전달한 키에 해당하는 값을 제거합니다.
- `localStroage.getItem(key)`: localStroage에서 인수로 전달한 키에 해당하는 값을 검색하여 반환합니다.

---

1. redux로 "인증 토큰"과 "로그인 상태"를 전역 상태로서 등록

```
// store/auth-slice.js
import { createSlice } from '@reduxjs/toolkit';

const authSlice = createSlice({
    name: 'auth',
    initialState: {
        // localStroage에서 token에 해당하는 값을 초기값으로
        token: localStorage.getItem('token'),

        // localStorage에 인증 토큰이 존재한다면 로그인 상태를 불리언 값으로
        isLoggedIn: !!localStorage.getItem('token'),
    },
    reducers: {
        login(state, action) {
            state.token = action.payload.token;
            state.isLoggedIn = true;

            // localStroage에 token이라는 키로 인증 토큰을 저장
            localStorage.setItem('token', action.payload.token);

            // localStorage experationTime이라는 키로 토큰 만료 기간을 저장
            localStorage.setItem('experationTime', action.payload.experationTime);
        },
        logout(state) {
            state.token = null;
            state.isLoggedIn = false;

            // localStorage에 token이라는 키의 값을 제거한다.
            localStorage.removeItem('token');

            // localStorage에 experationTime이라는 키의 값 제거
            localStorage.removeItem('experationTime');
        }
    }
});

export default authSlice;
```

```
// store/store.js
import { configureStore } from '@reduxjs/toolkit';

import authSlice from './auth-slice.js';

const store = configureStore({
    reducer: {
        auth: authSlice.reducer
    }
});

export default store;
```

---

1. 로그인시 redux에서 관리하는 인증 토큰 상태를 업데이트

```
// 로그인시 인증 토큰 가져오기
import { useSelector, useDispatch } from 'react-redux';
import authSlice from '../../store/auth-slice.js';
import { useNavigate } from 'react-router-dom';

,,,
const navigation = useNavigate();

const dispatch = useDispatch();
const { login } = authSlice.actions;

const sumbitHandler = () => {
    // 이메일과 패스워드 모두 유효한 경우에만 Http 요청 전송 가능
    if (emailIsValid && passwordIsValid) {
        setIsLoading(true);
    }
};

useEffect(() => {
    // 1. login fetching 로직
    if (isLogin && isLoading) {
        const loginFetch = async() => {
            try {
                // 1-1. 서버에게 Http 요청 전송
                const response = await fetch('https://,,,', {
                    method: 'POST',
                    body: JSON.stringify({
                        email: enteredEmail,
                        password: enteredPassword,
                        returnSecureToken: true
                    },
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });

                // 1-2. 응답 몸체 취득
                const data = await response.json();

                // 1-3. 응답 상태 확인
                if (response.ok) {
                    // 1-3-1. 로그인 성공시 인증 토큰과 토큰 만료기간을 localStorage에 저장
                    dispatch(authSlice.login({
                        token: data.idToken,
                        experationTime: data.expiresIn
                    }));
                } else {
                    // 1-3-2. 로그인 실패시 실패 메세지로 에러 객체 생성후 에러 발생
                    throw new Error(data.error.message);
                }

            } catch(error) {
                alert(error.message);
            } finally {
                setIsLoading(false);
            }
        };

        loginFetch();
    }

    // 2. create user fetching 로직
    if(!isLogin && isLoading) {
        const createFetch = async() => {
            try {
                // 2-1. 서버에게 Http 요청 전송
                const response = await fetch('https://,,,', {
                    method: 'POST',
                    body: JSON.stringify({
                        email: enteredEmail,
                        password: enteredPassword,
                        returnSecureToken: true
                    },
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });

                // 2-2. 서버가 전달한 응답 몸체 취득
                const data = await response.json();

                // 2-3. 응답 상태 확인
                if (response.ok) {
                    alert('Create Success!');
                } else {
                    throw new Error(data.error.message);
                }
            } catch(error) {
                alert(error.message);
            } finally {
                setIsLaoding(false);
            }
        };

        createFetch();
    }
}, [isLogin, isLoading])
,,,
```

---

1. 앱을 다시 시작하더라도 브라우저의 localStorage에 존재하는 **토큰의 만료 기간(epxerationTime)이 양수**인 경우 **자동 로그 아웃을 위한 호출 스케줄링**

```
// App.js

const App = () => {
    // App 컴포넌트가 첫 렌더링된 이후 호출
    useEffect(() => {
        // 인증 토큰 만료 기간이 아직 남은 경우
        if(localStorage.getItem('experationTime') > 0) {
            const currentTime = new Date().getTime();
            const experationTime = localStorage.getItem('experationTime');

            const remainTime = experationTime - currentTime;

            setTimeout(() => {
                dispatch(logout());
            }, remainTime);
        } else {  // -> 인증 만료 기간이 0보다 작은 경우
            localStorage.removeItem('experationTime');
        }
    }, [ dispatch, logout ]);
};

export default App;
```

## JWT

일반적으로 인증 토큰은 JSON 웹 토큰 형식(JWT)을 사용합니다. 인코딩된 문자열은 아래와 같은 형태를 갖습니다.

![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F6f03798e-0b29-40eb-beee-8cbf3e9c4e7b%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-02-21%2005.26.02.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F6f03798e-0b29-40eb-beee-8cbf3e9c4e7b%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-02-21%2005.26.02.png)

서버가 응답 헤더에 포함시켜 전달한 이러한 문자열을 토큰이라고 부릅니다.

자세히 보면 문자열에 `.`으로 구분되어 총 세 부분으로 나누어져 있다는 사실을 알 수 있습니다.

---

1. Header: 첫 번째 부분은 Header 부분으로 두 가지 정보가 존재합니다. 인코딩할 때 사용되는 **"알고리즘"**과 **"토큰의 타입"**이 존재합니다. **Header 부분은 "Base 64 인코딩 방식으로 인코딩되어 문자열"**이 됩니다.이때 토큰의 타입은 JWT로 고정되어 있으며, 알고리즘은 세 번째 부분인 Verify Signature 부분의 값을 만드는데 사용되는 알고리즘입니다. 여러 암호화 방식 중 하나로 지정될 수 있으며 **"첫 번째 Header"와 "두 번째 Payload" 그리고 "서버가 갖고 있는 키 값" 이 셋을 이 암호화 알고리즘 사용하여 만들어진 것이 바로 세 번째 Verify Signature**입니다.

![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F3de11c66-3652-4ff3-b6a7-448f87babe55%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-02-21%2005.39.03.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F3de11c66-3652-4ff3-b6a7-448f87babe55%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-02-21%2005.39.03.png)

---

1. Payload: 두 번째 부분은 Payload 부분으로 **사용자 혹은 토큰에 대한 정보**를 갖고 있습니다. Payload는 **Base 64 방식으로 인코딩되어 문자열**이 됩니다. 참고로 Payload 부분에는 사용자의 **민감한 정보를 포함시키지 않습니다.** Payload 부분은 Base 64 방식으로 누구나 디코드하여 확인이 가능하기 때문입니다. 즉, 서버는 사용자가 유효하다면 **사용자에 대한 고유한 키값을 생성하여 Payload에 포함시키는 방법으로 사용자에 대한 정보를 포함**시킵니다.

![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F634f01a3-ea3c-4afc-b7d7-16de3c37136d%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-02-21%2005.39.12.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2F634f01a3-ea3c-4afc-b7d7-16de3c37136d%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-02-21%2005.39.12.png)

---

1. Verify Signiture: 세 번째 부분은 Verify Signature 부분이 바로 **서버가 인증 상태의 유효성을 입증할 때 사용되는 부분**입니다. 서버는 **"Header와 Payload 부분을 각각 Base 64로 인코딩한 문자열을 합친 문자열과"**과 **"자신이 갖고 있는 키 값"**으로 **해싱**하여 JWT의 Verify Signiture 부분의 문자열을 생성하게 됩니다.클라이언트가 요청과 함께 JWT을 전달하면 서버는 전달받은 JWT의 **Veirty Signiture 문자열을 자신이 갖고 있는 키 값으로 복호화**하여 Header와 Payload를 확인할 수 있습니다. Payload 부분의 사용자 고유 ID나 인증 토큰 만료 시간 등 정보를 통해서 유효한지 확인합니다.

![https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Fd324c472-8f81-4556-8fc8-db201d9d34e5%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-02-21%2005.39.22.png](https://velog.velcdn.com/images%2Fkim98111%2Fpost%2Fd324c472-8f81-4556-8fc8-db201d9d34e5%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-02-21%2005.39.22.png)
