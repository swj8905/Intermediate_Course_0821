from konlpy.tag import Okt

okt = Okt() # Okt 분석기를 사용하겠다!
# result = okt.pos("안녕하세요. 저는 텍스트 마이닝을 공부하고 있습니다.")
# print(result)

result = okt.nouns("안녕. 나는 텍스트 마이닝을 공부 중이야.")
print(result)