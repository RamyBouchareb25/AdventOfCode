file = open("input.txt",'r')

arr = file.readlines()
def recherche(array = []):
    total = 0
    max = 0
    for i in array :
        if i == '\n':
            if total > max : max = total
            total = 0
        else :
            total = total + int(i)

    return max
print(recherche(arr))