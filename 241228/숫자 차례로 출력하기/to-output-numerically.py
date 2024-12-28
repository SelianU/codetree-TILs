def recursive_forward(n):
    if n == 0:
        return
    
    recursive_forward(n - 1)
    print(n, end=' ')

def recursive_backward(n):
    if n == 0:
        return
    
    print(n, end=' ')
    recursive_backward(n - 1)
n = int(input())

recursive_forward(n)
print()
recursive_backward(n)