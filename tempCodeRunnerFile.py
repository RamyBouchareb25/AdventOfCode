for i in range(len(arr)):
    prio = 0
    arr1 = arr[i]
    i = i+1
    arr2 = arr[i]
    i = i+1
    arr3 = arr[i]
    prio = Recherche(arr1,arr2,arr3)
    somme = somme + prio
print(somme)