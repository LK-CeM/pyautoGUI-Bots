
def main():
    file1 = open("numbers", "r")
    lines = file1.readlines()
    strat = [[1,4],[2,3],[3,4],[4,2]]
    new_list = []
    for line in lines:
        new_list.append([int(i) for i in line.split(",")])
    
    print(new_list)
    games_won = len(new_list)
   
    for i in range(len(new_list)):
        lose = False
        for j in range(4):
            if new_list[i][strat[j][0]-1] != j+1 and new_list[i][strat[j][1]-1] != j+1:
                lose = True
        if lose == True:
            games_won -= 1
        else:
            print(new_list[i])
    print("games played: ", len(new_list))
    print("games won: " ,games_won)
    games_won = len(new_list)
    for i in range(len(new_list)):
        lose = False
        for j in range(4):
            if new_list[i][j] != j+1 and new_list[i][new_list[i][j]-1] != j+1:
                lose = True
        if lose == True:
            games_won -= 1
        else:
            print(new_list[i])
    print("games played: ", len(new_list))
    print("games won: " ,games_won)
    return 0



if __name__ == "__main__":
    main()