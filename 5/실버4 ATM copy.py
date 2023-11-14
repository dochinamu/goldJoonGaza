def quickSort(a:list, left:int, right:int) :
    if left > right : return
    pivot = a[left]
    j= left
    for i in range(left + 1, right + 1) :
        if a[i] < pivot:
            j+= 1
            tmp= a[j]
            a[j] = a[i]
            a[i] = tmp
    tmp= a[left]
    a[left] = a[j]
    a[j] = tmp
    quickSort(a, left, j -1)
    quickSort(a, j + 1, right)
    return a

#재귀함수로 정렬하려고 했으나 백준에서 recursion error(최대 재귀 깊이 초과)에 걸렸기 때문에 sort로 정렬함

N = int(input())
List = list(map(int,input().split()))
x = 0

List.sort()

for i in range(N):
    x = x + List[i]*(N-i)
print(x)