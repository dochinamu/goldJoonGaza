def ManSwitch(a : list, N : int, L : int):      #a : 스위치 리스트 / N : 남학생이 부여받은 숫자 / L : 스위치 개수
    if N == 1:
        for i in range(L):
            Switch(a,i)
    else : 
        x = L//N
        for i in range(1,x+1):
            Switch(a,N*i-1)

    return a

def WomanSwitch(a : list, N : int , L : int):
    if N==1:
        Switch(a,0)
    else:  
        z = min(abs(L-N+1),N)
        Switch(a,N-1)
        for i in range(1,z):
            if a[N-i-1]==a[N+i-1]:
                Switch(a,N-i-1)
                Switch(a,N+i-1)
            else:
                break
    return a

def Switch(a,N):
    if a[N]==0:
        a[N]=1
    else : a[N]=0


NumSwitch = int(input())     #스위치 개수
ListSwitch = list(map(int,input().split())) #스위치 리스트
NumStudent = int(input())
for i in range(NumStudent):
    Sex,Num = map(int,input().split())
    if Sex == 1 :
        ManSwitch(ListSwitch,Num,len(ListSwitch))

    else:
        WomanSwitch(ListSwitch,Num,len(ListSwitch))


a = NumSwitch//20+1
for i in range(1,a):
    print(*ListSwitch[20*(i-1):20*(i)])
print(*ListSwitch[(a-1)*20:len(ListSwitch)])
