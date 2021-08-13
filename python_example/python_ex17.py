from konlpy.tag import Komoran
# pip install PyKomoran (설치)

# 코모란 형태소 분석기 객체 생성
komoran  = Komoran()

text = "아버지가 방에 들어가신다."

# 형태소 추출 - morphs 문장을 형태소 단위로 토크나이징. 리스트 형태로 반환
morphs = komoran.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출 - pos POS tagger, 문장에서 형태소를 추출한 뒤 품사 태깅. 튜플 형태로 묶여서 리스트로 반환
pos = komoran.pos(text)
print(pos)

# 명사만 추출 - nonus 문장에서 품사가 명사인 토큰들만 추출
nouns = komoran.nouns(text)
print(nouns)