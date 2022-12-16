file = open("input.txt","r")

arr = file.readlines()
total = 0
score = 0
for i in arr:
    winCondition = i.split(" ")[1][0]
    player1 = i.split(" ")[0]
    match winCondition:
        case 'X':
            match player1:
                case 'A':
                    score = 3
                case 'B':
                    score = 1
                case 'C':
                    score = 2
        case 'Y':
            match player1:
                case 'A':
                    score = 4
                case 'B':
                    score = 5
                case 'C':
                    score = 6
        case 'Z':
            match player1:
                case 'A':
                    score = 8
                case 'B':
                    score = 9
                case 'C':
                    score = 7
    total = total + score
    score = 0
print(total)