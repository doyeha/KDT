
much = int(input('몇칸으로 만들래...? 굳이 만들어야할까 ...? 이걸 왜? 뭐 땜에 ?'))
MGs = []
MG = []
for i in range(much):
    MGs = []
    for j in range(much):
        MGs.append(0)
    MG.append(MGs)

print(MG[0][0])