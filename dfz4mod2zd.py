def insortion_sort(arr):
	for i in range (1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key

arr = [12, -8, 11, 6, -1, -5, 4]
insortion_sort(arr)
print(arr)



