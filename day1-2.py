file = open("input.txt",'r')

arr = file.readlines()
def recherche(array = []):
    total = 0
    max1 = 0
    max2 = 0
    max3 = 0
    for i in array :
        if i != '\n':
            total = total + int(i)
        else :
            if total > max1:
                max3 = max2
                max2 = max1
                max1 = total
            elif total > max2:
                max3 = max2
                max2 = total
            elif total > max3:
                max3 = total
            total = 0
    return max1+max2+max3
print(recherche(arr))