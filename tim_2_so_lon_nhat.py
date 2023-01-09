def Find_Max(arr):    
    max = arr[0]

    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]

    return max
def Find_max_second(a):
    max_1 = max(a[0], a[1])
    max_2 = min(a[0], a[1])

    for i in range(2, len(a)):
        if a[i] > max_1:
            max_2 = max_1
            max_1 = a[i]
        elif (a[i] > max_2) and (max_1 != a[i]):
            max_2 = a[i]

    return max_2

def Enter_List(n):
    
    a = []
    for i in range(n):
        print("\tPhan tu thu", i+1, "la:", end=" ")
        a.append(int(input()))

    return a


n = int(input("Nhap vao so luong phan tu: n = "))
print("Nhap vao mang:")
arr = Enter_List(n)

print("\nPhan tu lon nhat la: ", Find_Max(arr))
print("\nPhan tu lon thu hai la:", Find_max_second(arr))