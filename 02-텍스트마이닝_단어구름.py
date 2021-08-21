from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

keyword = input("키워드 입력 >> ")
encoded = par.quote(keyword) # 한글 -> 특수한 문자

page_num = 1
output_total = ""
while True:
    url = f"https://www.joongang.co.kr/_CP/496?keyword={encoded}&sort%20=&pageItemId=439&page={page_num}"
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("h2.headline a")
    if len(title) == 0: # 끝 페이지까지 크롤링 완료했으면?
        break
    for i in title:
        print("제목 :", i.text.strip())
        try:
            print("링크 :", i.attrs["href"])
        except:
            continue
        code_news = req.urlopen(i.attrs["href"])
        soup_news = BeautifulSoup(code_news, "html.parser")
        content = soup_news.select_one("div#article_body")
        try:
            result = content.text.strip().replace("     ", " ").replace("   ", "")
        except:
            result = ""
        output_total += result
        print(result)
        print()

    if page_num == 1:
        break
    page_num += 1

print("명사들을 추출합니다..")
okt = Okt()
nouns_list = okt.nouns(output_total)
print(nouns_list)

print("불용어를 제거합니다..")
no_stopwords = []
for i in nouns_list:
    if len(i) != 1:
        no_stopwords.append(i)

print("명사들의 출현 빈도수를 카운트합니다..")
count = Counter(no_stopwords)
print(count)

# 단어구름 만들기
wc = WordCloud(font_path="./NanumMyeongjoBold.ttf", background_color="white").generate_from_frequencies(count)

# 단어구름 띄우기
plt.figure() # 창을 만듦
plt.imshow(wc, interpolation="bilinear") # 이미지를 창에 넣음
plt.axis("off") # 쓸데없이 뜨는 가로축, 세로축 없앰
plt.show() # 화면에 그 창을 띄움.