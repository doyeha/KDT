from konlpy.tag import Okt

okt = Okt()
text = "마음에 꽂힌 칼 한 자루보다 마음에 꽂힌 꽃 한 송이가 더 아파서 잠이 오지 않는다."

okt_tags = okt.pos(text, norm=True, stem = True)

print(okt_tags)

okt_nouns = okt.nouns(text)
print(okt_nouns)
