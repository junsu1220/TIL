import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    number = music.select_one('td.number')
    a = music.select_one('td.info > a.title.ellipsis')
    art = music.select_one('td.info > a.artist.ellipsis')

    rank = number.text[0:2].strip()
    title = a.text.strip()
    artist = art.text.strip()

    if("19금" in title):
        print(rank, title.replace("19금", "").strip(), artist)
        continue
    print(rank, title, artist)
