gm = [1,2,3,4,5,6,7,8,9]
X = "✖"
O = "⭘"
pl = []
queue = [X, O]
win = 0
for i in range(2):
    player = input("Додати гравця - ")
    pl.append(player)
qu = 1
no_game = 0
is_game = 0
is_game1 = 0
is_game2 = 0
is_game3 = 0
is_game4 = 0
is_game5 = 0
is_game6 = 0
is_game7 = 0
is_game8 = 0
is_game9 = 0


while win == 0 and is_game == 0 and no_game == 0:
        
    print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
    if qu == 0:
        ans = int(input(f"{pl[0]}, ваша черга! Куди походите? - "))
        qu = 1
    else:
        ans = int(input(f"{pl[1]}, ваша черга! Куди походите? - "))
        qu = 0
    if ans == 1 or ans == 2 or ans == 3 or ans == 4 or ans == 5 or ans == 6 or ans == 7 or ans == 8 or ans == 9:
        if qu == 0:
            if  gm[ans-1] != X and gm[ans-1] != O:
                gm[ans-1] = X
        if qu == 1:
            if  gm[ans-1] != X and gm[ans-1] != O:
                gm[ans-1] = O
            else:
                no_game = 1


    if gm[0] == X and gm[1] == X and gm[2] == X:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[1]} переміг(ла)")
        win = 1
    elif gm[3] == X and gm[4] == X and gm[5] == X:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[1]} переміг(ла)")
        win = 1
    elif gm[6] == X and gm[7] == X and gm[8] == X:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[1]} переміг(ла)")
        win = 1
    elif gm[0] == X and gm[4] == X and gm[8] == X:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[1]} переміг(ла)")
        win = 1
    elif gm[6] == X and gm[4] == X and gm[2] == X:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[1]} переміг(ла)")
        win = 1
    elif gm[0] == X and gm[3] == X and gm[6] == X:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[1]} переміг(ла)")
        win = 1
    elif gm[1] == X and gm[4] == X and gm[7] == X:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[1]} переміг(ла)")
        win = 1
    elif gm[2] == X and gm[5] == X and gm[8] == X:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[1]} переміг(ла)")
        win = 1





    if gm[0] == O and gm[1] == O and gm[2] == O:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[0]} переміг(ла)")
        win = 1
    elif gm[3] == O and gm[4] == O and gm[5] == O:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[0]} переміг(ла)")
        win = 1
    elif gm[6] == O and gm[7] == O and gm[8] == O:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[0]} переміг(ла)")
        win = 1
    elif gm[0] == O and gm[4] == O and gm[8] == O:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[0]} переміг(ла)")
        win = 1
    elif gm[6] == O and gm[4] == O and gm[2] == O:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[0]} переміг(ла)")
        win = 1
    elif gm[0] == X and gm[3] == X and gm[6] == X:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[0]} переміг(ла)")
        win = 1
    elif gm[1] == X and gm[4] == X and gm[7] == X:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[0]} переміг(ла)")
        win = 1
    elif gm[2] == X and gm[5] == X and gm[8] == X:
        print(f"\n|     |     |     |\n|  {gm[0]}  |  {gm[1]}  |  {gm[2]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[3]}  |  {gm[4]}  |  {gm[5]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {gm[6]}  |  {gm[7]}  |  {gm[8]}  |\n|     |     |     |\n")
        print(f"{pl[0]} переміг(ла)")
        win = 1



    if gm[0] != 1:
        is_game1 = 1
    if gm[1] != 2:
        is_game2 = 1
    if gm[2] != 3:
        is_game3 = 1
    if gm[3] != 4:
        is_game4 = 1
    if gm[4] != 5:
        is_game5 = 1
    if gm[5] != 6:
        is_game6 = 1
    if gm[6] != 7:
        is_game7 = 1
    if gm[7] != 8:
        is_game8 = 1
    if gm[8] != 9:
        is_game9 = 1

    if is_game1 == 1 and is_game2 == 1 and is_game3 == 1 and is_game4 == 1 and is_game5 == 1 and is_game6 == 1 and is_game7 == 1 and is_game8 == 1 and is_game9 == 1:
        is_game = 1

if is_game == 1:
    print("")
    print("Нічия")
if no_game == 1:
    print("")
    print("Неправильний хід, кінець гри")
