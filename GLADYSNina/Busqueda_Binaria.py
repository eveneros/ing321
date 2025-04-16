def binary_search(arr, target, low, high):
    if low > high :
        return -1
    mid = (low + high ) //2 
    if arr [mid] == target:
        return mid
    elif arr [mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else: 
        return binary_search(arr, target, low, mid - 1)
#EJEMPLO
arr = [2, 5, 8, 12, 16, 23, 38, 56]
target = 16
r = binary_search (arr, target, 0, len(arr) -1)
print(f"El elemento encontrado en indice : ", r)
    