def CollatzSequence(n):
    Sequence=""
    while n>1:
        Sequence+='{}->'.format(n)
        n=n//2 if n%2==0 else 3*n+1
    return Sequence+'1'
n=int(input())
print(CollatzSequence(n))