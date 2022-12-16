file = open("input.txt","r")

arr = file.readlines()
total = 0
score = 0
for i in arr:
    player1 = i.split(" ")[1][0]
    player2 = i.split(" ")[0]
    match player1:
        case 'X':
            match player2:
                case 'A':
                    score = 4
                case 'B':
                    score = 1
                case 'C':
                    score = 7
        case 'Y':
            match player2:
                case 'A':
                    score = 8
                case 'B':
                    score = 5
                case 'C':
                    score = 2
        case 'Z':
            match player2:
                case 'A':
                    score = 3
                case 'B':
                    score = 9
                case 'C':
                    score = 6
    total = total + score
    score = 0
print(total)