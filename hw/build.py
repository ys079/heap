def heapify2(A, i, n):
  if (2*i)<n and A[2*i]>A[i]:
    largest = 2*i
  else: largest = i
  
  if 2*i <= n and A[2*i + 1]>A[largest]:
    largest = 2*i + 1
  
  if largest != i :
    temp = A[i]
    A[i] = A[largest]
    A[largest] = temp
    heapify2(A,largest,n)
    
  else: return

def buildheap(A, n):
  
  if(n%2==0):
    a = n//2
  else :
    a = (n-1)//2
  for i in range(a, -1, -1):
    heapify2(A, i, n)


if __name__ == '__main__':
  A = [0,4,1,3,2,16,9,10,14,8,7]
  buildheap(A, 10)
  print(A)
