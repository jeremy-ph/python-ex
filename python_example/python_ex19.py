from konlpy.tag import Komoran

komoran = Komoran(userdic='./python_ex19.tsv')
text = "코리 우리 챗봇은 엔엘피를 좋아합니다."
pos = komoran.pos(text)
print(pos) 