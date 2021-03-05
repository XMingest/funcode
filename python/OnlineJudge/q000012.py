#Word Maze 是一个网络小游戏，你需要找到以字母标注的食物，但要求以给定单词字母的顺序吃掉。假设给定单词if，你必须先吃掉i然后才能吃掉f
#但现在你的任务可没有这么简单，你现在处于一个迷宫Maze（n×m的矩阵）当中，里面到处都是以字母标注的食物，但你只能吃掉能连成给定单词W的食物
#注意区分英文字母大小写,并且你只能上下左右行走
def func():
    n, m = map(int, input().strip().split())
    w = input().strip()
    wl = len(w)
    has_letters = [0 for _ in range(wl)]
    mazz = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        in_tmp = input()
        for j in range(m):
            start = w.find(in_tmp[j]) + 1
            while start > 0:
                mazz[i][j] |= 1 << (start - 1)
                has_letters[start - 1] = 1
                start = w.find(in_tmp[j], start) + 1
    if min(has_letters) > 0:
        for i in range(n):
            for j in range(m):
                if mazz[i][j] & 1:
                    footprint = [[i, j]]
                    nohope = [[] for _ in range(wl)]
                    step = 1
                    while footprint:
                        if step < wl:
                            now = footprint.pop()
                            step -= 1
                            can_next = False
                            for dxy in range(4):
                                pnext = now[:]
                                if dxy & 2:
                                    pnext[1] += 1 if dxy & 1 else -1
                                    if pnext[1] < 0 or pnext[1] >= m:
                                        continue
                                else:
                                    pnext[0] += 1 if dxy & 1 else -1
                                    if pnext[0] < 0 or pnext[0] >= n:
                                        continue
                                if not pnext in nohope[step + 1] and not pnext in footprint and mazz[pnext[0]][pnext[1]] & 2 << step:
                                    can_next = True
                                    footprint.append(now)
                                    footprint.append(pnext)
                                    step += 2
                                    break
                            if not can_next:
                                nohope[step].append(now)
                        else:
                            print('YES')
                            return
    print('NO')
    return

if __name__ == "__main__":
    func()
