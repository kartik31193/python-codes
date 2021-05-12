#for printing all subarrays in arr[0....n-1]
def subArray(arr,n):
    #pick starting point
    for i in range(n):
        #pick ending point
        for j in range(i,n):
            #print subarray between current starting and ending points
            for k in range(i,j+1):
                print(arr[k],end=' ')

            print("\n", end=' ')

arr = [1,2,3,4]
n=len(arr)
print("All non-empty subarrays")

subArray(arr,n)
