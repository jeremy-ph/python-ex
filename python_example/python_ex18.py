from konlpy.tag import Okt
# Okt는 띄어쓰기가 어느 정도 되어 있는 문장을 빠르게 분석할때 많이 사용

# Okt 형태소 분석기 객체 생성
okt = Okt()

text = "아버지가 방에 들어가신다."

# 형태소 추출 - morphs 문장을 형태소 단위로 토크나이징. 리스트 형태로 반환
morphs = okt.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출 pos - POS tagger, 형태소를 추출한 뒤 품사 태깅, 추출된 형태소와 품사가 튜플 형태로 묶여서 리스트로 반환
pos = okt.pos(text)
print(pos)

# 명사만 추출 - nonus 문장에서 품사가 명사인 토큰들만 추출
nouns = okt.nouns(text)
print(nouns)

# 정규화, 어구 추출 - mormalize 입력한 문장을 정규화시킨다.(사랑햌ㅋ => 사랑해ㅋㅋ), phrase 문장의 어구를 추출 (오늘 날씨가 좋아요 => '오늘', '오늘 날씨', '날씨')
text = "오늘 날씨가 좋아욬ㅋㅋ"
print(okt.normalize(text))
print(okt.phrases(text))