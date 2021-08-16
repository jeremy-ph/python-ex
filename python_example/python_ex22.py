# n-gram 유사도 계산
from konlpy.tag import Komoran

# 어절 단위 n-gram
# 어절 단위로 n-gram 토큰을 추출하는 함수, 추출된 토큰들은 튜플 형태로 반환
# [x:x + num_gram] 슬라이싱을 이용해 문장을 어절 단위로 n개씩 끊어서 토큰에 저장
# [0:0+2]  ('6월', '뉴턴') <==>   ('6월', '뉴턴', '선생님', '제안', '대학교', '입학')
# ex) a = [1, 2, 3, 4, 5] 에서 a[0,2] 결과는 [1, 2]

def word_ngram(bow, num_gram):
    text = tuple(bow)
    ngrams = [text[x:x + num_gram] for x in range(0, len(text))]
    return tuple(ngrams)

# 유사도 계산
# doc1 = (('6월', '뉴턴'), ('뉴턴', '선생님'), ('선생님', '제안'), ('제안', '트리니티'), ('트리니티', '입학'), ('입학',))
# token = ('6월', '뉴턴')
# similarity = if(A,B) / tokens(A)

def similarity(doc1, doc2):
    cnt = 0
    for token in doc1:
        if token in doc2:
            cnt = cnt +1
    return cnt/len(doc1)

# 문장 정의
sentence1 = '6월에 뉴턴은 선생님의 제안으로 트리니티에 입학했다.'
sentence2 = '6월에 뉴턴은 선생님의 제안으로 대학교에 입학했다.'
sentence3 = '나는 맛있는 밥을 뉴턴 선생님과 함께 먹었다.'

# 형태소 문석기에서 명사(단어) 추출
komoran = Komoran()
bow1 = komoran.nouns(sentence1)
bow2 = komoran.nouns(sentence2)
bow3 = komoran.nouns(sentence3)

# 단어 n-gram 토근 출현
doc1 = word_ngram(bow1, 2)  # 2-gram 방식으로 추출
doc2 = word_ngram(bow2, 2)
doc3 = word_ngram(bow3, 2)

# 추출된 n-gram 토큰 출력
print(doc1)
print(doc2)
print(doc3)

# 유사도 계산
r1 = similarity(doc1, doc2)
r2 = similarity(doc3, doc1)

# 계산된 유사도 출력
print('doc1, doc2 유사도 : ', r1)
print('doc3, doc1 유사도 : ', r2)

