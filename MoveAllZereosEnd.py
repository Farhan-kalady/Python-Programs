class Solution:
    def pushZerosToEnd(self, arr):
        count = 0
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[count]=arr[i]
                count+=1

        while count < len(arr):
            arr[count]=0
            count+=1        

def main():
    arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
    sol = Solution()
    sol.pushZerosToEnd(arr)
    print("Array after moving all zeros to the end:")
    print(arr)

if __name__ == "__main__":
    main()