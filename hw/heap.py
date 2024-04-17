# def heapify(arr):
#     last = len(arr) // 2 - 1
#     for current in range(last, -1, -1):
#         while current <= last:
#             child = current * 2 + 1
#             sibling = child + 1
#             if sibling < len(arr) and arr[child] > arr[sibling]:
#                 child = sibling
#             if arr[current] > arr[child]:
#                 arr[current], arr[child] = arr[child], arr[current]
#                 current = child
#             else:
#                 break
              
              
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

# def buildheap(A, n):
#   for i in range(n//2, -1. -1):
#     heapify2(A, i, n)


#테스트 코드
if __name__ == '__main__':
  A = [0,16,4,10,14,7,9,3,2,8,1]
  heapify2(A, 2, 10)
  print(A)
  
  
  