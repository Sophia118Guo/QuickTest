def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Take user input for numbers to be sorted
arr = list(map(int, input("Enter the numbers to be sorted: ").split()))

# Call bubble sort function
bubble_sort(arr)

# Print sorted array
print("Sorted array:", arr)
