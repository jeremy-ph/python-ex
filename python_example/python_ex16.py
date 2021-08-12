from konlpy.tag import Kkma
# KoNLPy 코엔엘파이 라이브러리 (한국어 자연어 처리)
# pip install konlpy
## Install Java 1.8 or up (Java 설치)
## $ sudo apt-get install g++ openjdk-8-jdk python3-dev python3-pip curl

# 꼬꼬마 형태소 분석기 객체 생성
kkma = Kkma()

text = "아버지가 방에 들어가신다."
# 형태소 추출 morphs - 인자로 문장을 형태소 단위로 토크나이징. 리스트 형태로 반환
morphs = kkma.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출 pos - POS tagger, 형태소를 추출한 뒤 품사 태깅, 추출된 형태소와 품사가 튜플 형태로 묶여서 리스트로 반환
pos = kkma.pos(text)
print(pos)

# 명사만 추출 nouns - 인자로 입력한 문장에서 품사가 명사인 토큰만 추출
nouns = kkma.nouns(text)
print(nouns)

# 문장 분리 sentences - 여러 문장을 분리해주는 역할. 리스트 형태로 반환
sentences = "오늘 날씨는 어때요? 내일은 덥다던데."
s = kkma.sentences(sentences)
print(s)
