import sys
input=sys.stdin.readline

T=int(input())

def VPS():
    test=input()
    stack=[]
    size=0
    for i in test:
        if i=='(':
            stack.append(i)
            size+=1
        else:
            if size==0:
                print('NO')
                return
            else:
                stack.pop()
                size-=1
                
    if size==0:
        print('YES')
    else:
        print('NO')

for i in range(T):
    VPS()