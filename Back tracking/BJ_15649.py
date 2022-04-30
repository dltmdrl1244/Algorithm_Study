import sys
n, m = map(int, sys.stdin.readline().split())

s = []

def f() :
    if len(s) == m :
        print(" ".join(map(str, s)))
    
    for i in range(1, n+1) :
        if i not in s :
            s.append(i)
            f()
            s.pop()
            
f()

# s라는 리스트를 만들고, 리스트에 없으면 숫자를 집어넣는다.
# 그리고 집어넣은 후에 바로 재귀적으로 함수를 한번 더 부른다. 그렇다면 두 번째, 세 번째 숫자도 계속해서 들어갈 것이다.
# 그러다 숫자가 m개 모두 들어가게 되면 s 리스트의 원소들을 출력한다.

# 순서는 [1]에서 다시 f([1])이 호출되어 f([1, 2])... 이런 식으로 계속 호출할 것이고 다시 1이 pop 되어 []이 된다.
# 그러고는 다음 루프에서 2가 들어가서 [2]가 될 것이다. not in s로 s에 없는 숫자들만 넣기 때문에 중복은 당연히 없고
# for 루프가 1부터 9까지 훑어보면서 돌아가기 때문에 출력값 역시 자연스럽게 사전순으로 배열될 것이다.