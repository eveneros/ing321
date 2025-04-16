def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr [:mid]
        R = arr [mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 8
        while i < len(L) and j < len(R):
            if L[1] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                # Ejemplo :
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Array ordenado: ",arr)