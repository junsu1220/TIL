## DNS란?
- 도메인 네임 시스템(Domain Name System, DNS) 은 호스트의 도메인네임(www.example.com)을 네트워크주소(192.168.1.0)로 변환하거나,
그 반대의 역할을 수행하는 시스템입니다.
- DNS시스템은 이름과 숫자 간의 매핑을 관리하여 마치 전화번호부와 같은 기능을 합니다.
- DNS 서버는 사용자가 도메인 이름을 브라우저에 입력하면, 사용자를 어떤 서버에 연결할 것인지 제어합니다.
이러한 요청을 쿼리 라고 합니다.
- 문자열의 탈을 쓴 IP라고 볼 수 있습니다.
- 우리가 입력한 도메인 주소(www.naver.com)을 숫자인 IP주소로 변환하는 과정이 필요한데 이것을 담당하는 시스템이 DNS입니다.
- 사용자가 입력한 도메인 주소 = 문자로 된 우리집 주소
- IP 주소 = 집배원 아저씨가 알아볼 수 있도록 우리집 주소를 숫자로 된 우편 주소로 나타낸 것

![](../assets/DNS_2.png)
![](../assets/DNS_3.png)

## DNS를 사용하는 이유
- 길고 복잡한 IP주소를 외울수가 없기 때문입니다.

## DNS 서비스 유형 
- 신뢰할 수 있는 DNS
  - 개발자가 퍼블릭 DNS 이름을 관리하는 데 사용하는 업데이트 매커니즘을 제공합니다.
  - 이를 통해 DNS 쿼리에 응답하여 도메인 이름을 IP주소로 변환합니다.
  - 신뢰할 수 있는 DNS는 도메인에 대해 최종 권한이 있습니다.
  - 재귀적 DNS 서버에 IP주소 정보가 담긴 답을 제공할 책임이 있습니다.

- 재귀적 DNS
  - 보통 클라이언트는 신뢰할 수 있는 DNS 서비스에 직접 쿼리를 수행하지 않습니다.
  - 해석기 또는 재귀적 DNS 서비스라고 알려진 다른 유형의 DNS 서비스에 연결하는 경우가 일반적입니다.
  - DNS 레코드를 소유하고 있지 않지만 사용자를 대신해서 DNS 정보를 가져올 수 있는 중간자의 역할을 합니다.
  - 일정 기간 동안 캐시된 또는 저장된 DNS 레퍼런스를 가지고 있는 경우, 소스 또는 IP 정보를 제공하여 DNS 쿼리에 답을 하거나, 
해당 정보를 찾기 위해 쿼리를 하나 이상의 신뢰할 수 있는 DNS 서버에 전달합니다.

## DNS 구성요소
- 인터넷상에서 사용되는 도메인은 전 세계적으로 고유하게 존재하는 이름
- 정해진 규칙 및 체계에 따라야 하며, 임의로 변경되거나 생성될 수 없음
- 도메인 네임 스페이스
  - 최상위에 루트 DNS서버가 존재하고, 그 하위로 인터넷에 연결된 모든 노드가 연속해서 이어진 계층구조로 구성
- 네임 서버
  - 주소를 변환 시키기 위해 도메인 네임 스페이스의 트리구조에 대한 정보가 필요
  - 이 정보를 가진 서버 도메인 이름을 IP주소로 변환하는 것이 네임 서비스
- 리졸버
  - DNS클라이언트의 요청을 네임 서버로 전달하고 네임 서버로부터 도메인 이름과 IP주소를 받아 클라이언트에게 제공하는 기능을 수행

## DNS 기본 동작 설명
![](../assets/DNS_5.gif)
![](../assets/DNS_1.gif)

- 웹 브라우저에 www.naver.com 을 입력합니다. 그러면 PC는 미리 설정되어 있는 DNS(단말에 설정되어 있는 이 DNS를 Local DNS라 부릅니다, 
위에서는 203.248.252.2)에게 "www.naver.com 이라는 hostname" 에 대한 IP주소를 요청합니다.
- Local DNS 에는 "www.naver.com의 IP주소" 가 있을 수도, 없을 수도 있습니다. 만약 있다면 Local DNS가 바로 PC에 IP주소를 주고 끝나지만 
여기서는 Local DNS에 "www.naver.com 의 IP 주소"가 없다고 가정합니다.
- Local DNS는 이제 "www.naver.com의 IP주소"를 찾아내기 위해 다른 DNS 서버들과 통신(DNS 메시지)을 시작합니다. 
  - 먼저 Root DNS 서버에게 "www.naver.com 의 IP주소"를 요청하며, 이를 위해 각 Local DNS 서버에는 Root DNS 서버의 정보(IP 주소)가 
미리 설정되어 있어야 합니다.
  - Root DNS 서버는 전세계에 13대가 구축되어 있습니다.
  - 미국에 10대, 일본/네덜란드/노르웨이에 각 1대씩이며, 
우리나라의 경우 Root DNS 서버가 존재하지는 않지만 Root DNS 서버에 대한 미러 서버를 3대 운용하고 있다고 합니다.
  - Root DNS는 인터넷의 도메인 네임 시스템의 루트존입니다. 루트 존의 레코드의 요청에 직접 응답하고 적절한 최상위 도메인에 대해 권한이 있는
네임 서버 목록을 반환함으로써 다른 요청에 응답합니다. 전세계에 961개의 루트 DNS가 운영되고 있습니다.
- Root DNS 서버는 "www.naver.com 의 IP주소"를 찾을 수 없어 Local DNS 서버에게 "www.naver.com 의 IP 주소 찾을 수 없음. 다른 DNS서버에게 
물어봐" 라고 응답합니다.
- 이 다른 DNS 서버는 com 도메인을 관리하는 DNS 서버입니다. (TLD-Top-Level Domain)
- 이제 Local DNS서버는 com 도메인을 관리하는 DNS서버에 다시 www.naver.com에 대한 IP주소를 요청합니다.
- com 도메인을 관리하는 DNS 서버에도 해당 정보가 없으면, Local DNS 서버에게 "www.naver.com 의 IP주소 찾을 수 없음. 다른
 DNS서버에게 물어봐"라고 응답합니다. 이 다른 DNS 서버는 naver.com 도메인을 관리하는 DNS서버입니다.
- 이제 Local DNS 서버는 naver.com DNS 서버에게 다시 "www.naver.com 의 IP주소"를 요청합니다.
- naver.com DNS 서버에는 "www.naver.com의 IP주소"가 있습니다. 그래서 Local DNS서버에게 "www.naver.com에 대한 IP주소는
 222.122.195.6"라는 응답을 합니다.
 - 이를 수신한 Local DNS는 www.naver.com 의 IP 주소를 캐싱을 하고 이후 다른 요청이 있을시 응답할 수 있도록 IP주소 정보를 단말(PC)에
 전달해 줍니다.
 - Local DNS 서버가 여러 DNS 서버에 차례대로 (Root DNS 서버 -> com DNS 서버 -> naver.com DNS 서버) 요청하여 
그 답을 찾는 과정을 Recursive Query 라고 부릅니다.

***

1. DNS Query (from Web Browser to Local DNS) : "제가 원하는 웹 사이트의 IP 주소를 알고 계신가요?" Local DNS 서버에게 전달

 

2. DNS Query (from Local DNS to Root DNS) : "제가 원하는 웹 사이트의 IP 주소를 알고 계신가요?" Root DNS서버에게 전달

 

3. DNS Response (from Root DNS to Local DNS) : "저는 모르지만 , Com 도메인을 관리하는 네임서버의 이름과 IP 주소를 알려드릴 테니 거기에 물어보세요"

 

4. DNS Query (from Local DNS to com NS) : “ 안녕하세요. www. naver. com의 IP 주소를 알고 계신가요?"

 

5. DNS Response (from com NS to Local DNS) : "저는 모르지만 , Com 도메인을 관리하는 네임서버의 이름과 IP 주소를 알려드릴 테니 거기에 물어보세요"

 

6. DNS Query (from Local DNS to naver. com NS) : “ 안녕하세요. www. Naver .com의 IP 주소를 알고 계신가요?"

 

7. DNS Response (from naver .com NS to Local DNS) : "저는 모르지만 해당 웹은 www. g.naver. com이라는 이름으로 통해요. g.naver .com 도메인을 관리하는 네임서버의 이름과 IP 주소를 알려드릴테니 거기에 물어보세요"

 

8. DNS Query (from Local DNS to g.naver. com NS) : “ 안녕하세요. www. g.naver. com의 IP 주소를 알고 계신가요?"

 

9. DNS Response (from g.naver .com NS to Local DNS) : " 네 www. g.naver .com의 IP 주소는 222.222.222.22와 333.333.333.33입니다"

 

10. DNS Response (from Local DNS to Web Browser) : "네 www. naver .com의 IP 주소는 222.222.222.22와 333.333.333.33입니다"

***

## TLD의 구조
![](../assets/DNS_4.jpg)

- 최상위 ICANN 아래에 REGISTRY, NIC이 있고 REGISTRY 아래에 우리가 흔이 보는 gTLD 
그리고 new gTLD가 있고 NIC아래에는 공공사이트에서 쓰는 ccTLD 도메인 주소가 있습니다.
- velog.io 와 github.io (깃허브 블로그)는 영국령 인도양 지역의 인터넷 국가 코드 최상위 도메인입니다. 
io 도메인을 쓰면 기존 com, net이 점유하고 있던 도메인들을 벗어나 새롭게 도메인을 확보할 수 있다고 합니다. 
개별국가 NIC이 관리하고 주로 회사들이 이용해서 비싸다고 합니다...

참고:

https://velog.io/@doomchit_3/Internet-DNS-%EC%9E%91%EB%8F%99%EC%9B%90%EB%A6%AC-IMBETPY

https://velog.io/@goban/DNS%EC%99%80-%EC%9E%91%EB%8F%99%EC%9B%90%EB%A6%AC

https://ja-gamma.tistory.com/entry/DNS%EA%B0%9C%EB%85%90%EB%8F%99%EC%9E%91%EC%9B%90%EB%A6%AC

https://ijbgo.tistory.com/27

https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=sharp428&logNo=220633341869
