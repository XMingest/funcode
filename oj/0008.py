#solo发现他参加Online Judge的比赛表现很不稳定，于是他翻开历史记录，发现他在每一轮的比赛中他的排名R都能整除参赛人数N(包括solo)，于是他每次参赛都会先预测他的排名情况，以给自己更大的自信
def func():
    prsns = int(input().strip())
    lil = []
    lir = []
    n = 0
    i = 1
    while i * i < prsns:
        if prsns % i == 0:
            n += 2
            lil.append(str(i))
            lir = [str(prsns // i)] + lir
        i += 1
    if i * i == prsns:
        print(' '.join([str(n + 1)] + lil + [str(i)] + lir))
    else:
        print(' '.join([str(n)] + lil + lir))
    return

if __name__ == "__main__":
    func()
