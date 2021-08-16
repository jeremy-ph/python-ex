from gensim.models import Word2Vec

# 모델 로딩
model = Word2Vec.load('nvmc.model')
print("corpus_total_words : ", model.corpus_total_words)

# '사랑'이란 단어로 생성한 단어 임베딩 벡터
# 모델을 할습할 때 설정한 size 만큼 임베딩 벡터 차원 크기가 결정
print('사랑 : ', model.wv['사랑'])

# 단어 유사도 계산
# model.wv.similarity() 함수를 호출할 경우 인자로 사용한 단어와 가장 유사한 단어를 리스트로 반환
# 즉, 백터 공간에서 가장 가까운 거리에 있는 단어들을 반환
# topn 인자는 반환되는 유사한 단어 수를 의미, 예제에선 5개까지 유사한 단어를 반환
print("월요일 = 월요일\t", model.wv.similarity(w1='일요일', w2='월요일'))
print("안성기 = 배우\t", model.wv.similarity(w1='안성기', w2='배우'))
print("대기업 = 삼성\t", model.wv.similarity(w1='대기업', w2='삼성'))
print("일요일 = 삼성\t", model.wv.similarity(w1='일요일', w2='삼성'))
print("히어로 = 삼성\t", model.wv.similarity(w1='히어로', w2='삼성'))

# 가장 유사한 단어 추출
print(model.wv.most_similar("안성기", topn=5))
print(model.wv.most_similar("시리즈", topn=5))