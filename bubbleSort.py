#sorts a sequence in ascending order using the bubble sort algorithm
def bubbleSort(arr):
    n= len(arr)
    #performing n-1 bubble operations on the sequence
    for i in range (n-1):
        #bubble the largest item to the end
        for j in range(0, n-i-1):
            if arr[j]> arr[j+1]: #swap the j and j+1 items
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
arr=[]
p= int(input("Enter number of elements:"))
for i  in range(0,p):
    ele= int(input())
    arr.append(ele)
print(arr)
bubbleSort(arr)
print("Sorted array is: ")
for i in range(len(arr)):
    print("%d" % arr[i], end= " ")
