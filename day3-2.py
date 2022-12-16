file = open("input.txt","r")
arr = file.readlines()
def Priorite(letter):
    if ord(letter) > 96 and ord(letter) <123:
        return ord(letter)-96
    elif ord(letter) <= 90 and ord(letter) >64:
        return ord(letter)-38
    else: return 
def Recherche(arr = [],arr2 = [],arr3 = []):
    i=0
    j=0
    k=0
    length = len(arr)
    length2 = len(arr2)
    length3 = len(arr3)
    for i in range(length):
        for j in range(length2):
            if arr[i] == arr2[j]:
                for k in range(length3):
                    if arr[i] == arr3[k]:
                        return Priorite(arr[i])
somme = 0
i = 0
for i in range(0,len(arr),3):
    prio = 0
    if i > len(arr)-3:break
    arr1 = arr[i]
    arr2 = arr[i+1]
    arr3 = arr[i+2]
    print(arr1,arr2,arr3)
    prio = Recherche(arr1,arr2,arr3)
    somme = somme + prio
print(somme)