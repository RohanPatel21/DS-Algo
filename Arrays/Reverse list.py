def reverseList(A, start, end):
    while start<end:
        A[start],A[end] = A[end],A[start]
        end -=1
        start+= 1

# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)
