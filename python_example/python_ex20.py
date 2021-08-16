# one-hot incoding
from konlpy.tag import Komoran
import numpy as np

komoran = Komoran()
text = "오늘 날씨는 구름이 많아요."

# 명사만 추출
nouns = komoran.nouns(text)
print(nouns) # ['오늘', '날씨', '구름']

# 단어 사전 구축 및 단어별 인덱스 부여
# len()은 리스트에 들어있는 원소 개수, 그러니까 리스트의 크기를 알려줌
dics = {}
for word in nouns:
    if word not in dics.keys():
        dics[word] = len(dics)
print(dics) # {'오늘': 0, '날씨': 1, '구름': 2}

# 원-핫 인코딩
nb_classes = len(dics)
print(nb_classes) # 3

targets = list(dics.values())
print(targets) # [0, 1, 2]

one_hot_targets = np.eye(nb_classes)[targets]
print(one_hot_targets)
