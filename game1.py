def MainOP():
    import time
    print("---------------------------")
    print("Good Day Players!")
    time.sleep(0.5)
    while True:
        time.sleep(1)
        GameMode = str(input("Which gamemode would you like to play?\n Enter 1 for Player Vs Player\n Enter 2 for Player Vs Computer\n Enter any other input to be asked again\n Enter Input: "))
        if GameMode == "1":
            Player1Name = str(input("Player one please input your name: "))
            Player2Name = str(input("Player two please input your name: "))
            PlayerVsPlayer(Player1Name, Player2Name)
            break
        elif GameMode == "2":
            PlayerName = str(input("Hello player, please input your name: "))
            PlayerVsComputer(PlayerName)
            break
        else:
            print("That input was invalid! Please enter your request again! ")

def PlayerVsPlayer(P1,P2):
    counters = 10
    while counters >0:
        while True:
            P1_Option = int(input(P1+" how many counters would you like to take? 1,2 or 3?"))
            if P1_Option == 1 or P1_Option == 2 or P1_Option == 3:
                print("You have removed:",P1_Option,"Counters!")
                counters -= P1_Option
                print("New counter count:",counters)
                break
            else:
                print("Input denied!")
                
       
        if counters <=0:
            print("Congratulations",P2, "wins!")
            break
        else:
            while True:
                P2_Option = int(input(P2+" how many counters would you like to take? 1,2 or 3?"))
                if P2_Option == 1 or P2_Option == 2 or P2_Option == 3:
                    print("You have removed:",P2_Option,"Counters!")
                    counters-= P2_Option
                    print("New counter count:",counters)
                    break
                else:
                    print("Input denied!")
            
            if counters <= 0:
                print("Congratulations",P1,"wins!")
                break
    
def PlayerVsComputer(P1):
    import random
    import time
    counters =10
    while counters>0:
        while True:
            P1_Option = int(input(P1+" how many counters would you like to take? 1,2 or 3?"))
            if P1_Option == 1 or P1_Option == 2 or P1_Option == 3:
                print("You have removed:",P1_Option,"Counters!")
                counters -= P1_Option
                print("New counter count:",counters)
                break
            else:
                print("Input denied!")
        if counters <=0:
            print("Computer Wins!")
            break
        else:
            CompOpt = random.randint(1,3)
            counters -= CompOpt
            time.sleep(0.5)
            print("The computer selected",CompOpt)
            print("New counter count:",counters)
        if counters <= 0:
            print("Congratulations! You won! (Computer Lost)")
            break


MainOP()
            
                
        
