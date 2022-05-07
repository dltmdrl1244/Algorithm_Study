import sys
input = sys.stdin.readline

n = int(input())
dic = {}
cards = list(map(int, input().split()))
answer = []

for c in cards :
    if c in dic :
        dic[c] += 1
    else :
        dic[c] = 1

m = int(input())
search = list(map(int, input().split()))

for s in search :
    if s in dic :
        answer.append(dic[s])
    else :
        answer.append(0)

print(*answer)