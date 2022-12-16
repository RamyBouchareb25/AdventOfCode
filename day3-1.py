file = open("input.txt","r")
arr = file.readlines()
def Priorite(letter):
    if ord(letter) > 96 and ord(letter) <123:
        return ord(letter)-96
    elif ord(letter) <= 90 and ord(letter) >64:
        return ord(letter)-38
    else: return 
def Recherche(arr = [],arr2 = []):
    i=0
    j=0
    length = len(arr)
    length2 = len(arr2)
    for i in range(length):
        for j in range(length2):
            if arr[i] == arr2[j]:
                return Priorite(arr[i])
somme = 0
for i in arr:
    prio = 0
    arr1 = i[int(len(i)/2):]
    arr2 = i[:int(len(i)/2)]
    prio = Recherche(arr1,arr2)
    somme = somme + prio
print(somme)