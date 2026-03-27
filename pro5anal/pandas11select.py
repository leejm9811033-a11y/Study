# css 셀렉터를 이용
from bs4 import BeautifulSoup
html_page = """
<html>
<body>
<div id="hello">
    <a href="https://www.naver.com">naver</a><br>
    <span>
        <a href="https://www.daum.com">daum</a><br>
    </span>
    <ul class="world">
        <li>안녕</li>
        <li>반가워</li>
    </ul>
</div>
<div id="hi" class="good">
    두 번째 div
</div>
</body>
</head>
"""
soup = BeautifulSoup(html_page, 'lxml')
# aa = soup.select_one("div")
# aa = soup.select_one("div#hello")
# aa = soup.select_one("div.good")
aa = soup.select_one("div#hello > a")
print('aa : ', aa, ' ', aa.string )

print()
# bb = soup.select("div")
# bb = soup.select("div#hello > ul.world")
# bb = soup.select("div#hello ul.world")
bb = soup.select("div#hello ul.world > li")
print('bb : ', bb)
for i in bb:
    print(i, ' ', i.text)

print("---- 위키백과 사이트에서 이순신으로 검색된 자료 읽기 ----------")
import requests
url = "https://ko.wikipedia.org/wiki/이순신"
headers = {"User-Agent":"Mozilla/5.0"}
wiki = requests.get(url = url, headers=headers)
# print(wiki.text[:100])

soup = BeautifulSoup(wiki.text, 'html.parser')
# result = soup.select("p#mwHw")           # < p id = "<p id="mwHw">문반 가문 출신으로 1576년(선조 9년) 무과(武科)에 급제하여 함경도 동구비보 권관(종9품)을 시작으로 훈련원 봉사(종8품), 충청병사 군관, 전라도 발포진 수군만호(종4품), 훈련원 봉사(종8품), 함경남병사 군관, 훈련원 참군(정7품), 사복시 주부(종6품), 함경도 조산보 병마만호(종4품), 전라감사 조방장, 선전관, 전라도 정읍현감(종6품:태인현감 겸무), 전라좌도수군절도사(정3품)를 거쳐 정헌대부(정2품상계) 삼도수군통제사(종2품)에 이르렀다.<sup about="#mwt10" class="mw-ref reference" id="cite_ref-2" rel="dc:references" typeof="mw:Extension/ref" data-mw="{&quot;name&quot;:&quot;ref&quot;,&quot;attrs&quot;:{},&quot;body&quot;:{&quot;id&quot;:&quot;mw-reference-text-cite_note-2&quot;}}"><a href="#cite_note-2" id="mwIA"><span class="mw-reflink-text" id="mwIQ"><span class="cite-bracket" id="mwIg">[</span>2<span class="cite-bracket" id="mwIw">]</span></span></a></sup></p>"
result = soup.select("#mw-content-text p")

# print(result)
for s in result:
    for sup in s.find_all("sup"):
        sup.decompose()     # 태그 삭제

    print(s.get_text(strip=True))


print("--- 교촌치킨 사이트에서 메뉴, 가격 자료 읽기 --------------")
import pandas as pd
url = "https://kyochon.com/menu/chicken.asp"
headers = {"User-Agent":"Mozilla/5.0"}
response = requests.get(url, headers=headers)
# print(response.text)

soup2 = BeautifulSoup(response.text, 'html.parser')
# 메뉴명 얻기
# names = soup2.select("dl.txt>dt")
# print(names)
names = [tag.text.strip() for tag in soup2.select("dl.txt>dt")]
# print(names)
prices = [int(tag.text.strip().replace(',','')) for tag in soup2.select("p.money strong")]
print(prices)

df = pd.DataFrame({"상품명":names, "가격":prices})
print(df.head(3))
print(f"가격 평균 : {df['가격'].mean():.2f}")
print(f"가격 표준편차 : {df['가격'].std():.2f}")
cv = df['가격'].std() / df['가격'].mean() * 100
print(f"가격 변동계수(CV) : {cv:.2f}%")
# 해석 : 가격 변동계수(CV) : 28.31%이므로 평균 대비 적당히 퍼져 있는 편




