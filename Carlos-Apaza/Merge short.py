def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Corregido: era Z en lugar de 2
        L = arr[:mid]        # Corregido: era arr[mid] (solo un elemento)
        R = arr[mid:]        # Correcto
        
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
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

# Ejemplo:
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Array ordenado:", arr)