import sys
from time import sleep

def checkcolumn(c):
    #checkcolumn(c) checks if the cth column has atleast one empty spot
    if board[0][c-1] == '.':
        return True
    return False   
    
def checkcolumn2(c):
    #checkcolumn2(c) checks if the cth column has atleast one empty spot(when force of gravity is pointing upwards)
    if board[5][c-1] == '.':
        return True
    return False   
    
def checkrow(c):
    #checkrow(c) checks to see if the cth row has atleast one empty spot(when the force of gravity is pointing rightwards)
    if board[c-1][0] == '.':
        return True
    return False
    
def checkrow2(c):
    #checkrow(c) checks to see if the cth row has atleast one empty spot(when the force of gravity is pointing leftwards)
    if board[c-1][6] == '.':
        return True
    return False
    
def RotGrav(posn):
    """
    Shifts the force of gravity to downwards if posn=0
    Shifts the force of gravity to rightwards if posn=2
    Shifts the force of gravity to upwards if posn=2
    Shifts the force of gravity to leftwards if posn=2
    """
    if posn==0:
        for i in range(0,7):
            b=['.', '.', '.' ,'.', '.', '.']
            t1=0
            for j in range(0, 6):
                if(board[5-j][i]!='.'):
                    b[t1]=board[5-j][i]
                    t1=t1+1
            for j in range(0,6):
                board[j][i]=b[5-j]      
    if posn==1:
        temp=0  
        for x in board:
            b=['.', '.', '.' ,'.', '.', '.' ,'.']
            i=0
            x.reverse()
            for y in x:
                if not y=='.':
                    b[6-i]=y
                    i=i+1
            board[temp]=b
            temp=temp+1
    if posn==2:
        for i in range(0,7):
            b=['.', '.', '.' ,'.', '.', '.']
            t1=0
            for j in range(0, 6):
                if(board[j][i]!='.'):
                    b[t1]=board[j][i]
                    t1=t1+1
            for j in range(0,6):
                board[j][i]=b[j]        
    if posn==3:
        temp=0  
        for x in board:
            b=['.', '.', '.' ,'.', '.', '.' ,'.']
            i=0
            for y in x:
                if not y=='.':
                    b[i]=y
                    i=i+1
            board[temp]=b
            temp=temp+1 
                   
def checkwin(ab):
    #checkwin(ab) prints which player wins if any and returns True if a player has won or returns False otherwise
    if ab==0:
        t='X'
    else:
        t='O'
    for row in range(0,6):
        for column in range(0, 7):
            if column<=3 and t==board[row][column] and t==board[row][column+1] and t==board[row][column+2] and t==board[row][column+3]:
                print "Player "+ str(ab+1) +" wins!"
                return True
            if row<=2 and t==board[row][column] and t==board[row+1][column] and t==board[row+2][column] and t==board[row+3][column]:
                print "Player "+ str(ab+1) +" wins!"
                return True
            if column>=3 and row<=2 and t==board[row][column] and t==board[row+1][column-1] and t==board[row+2][column-2] and t==board[row+3][column-3]:
                print "Player "+ str(ab+1) +" wins!"
                return True
            if column<=3 and row<=2 and t==board[row][column] and t==board[row+1][column+1] and t==board[row+2][column+2] and t==board[row+3][column+3]:
                print "Player "+ str(ab+1) +" wins!"
                return True
    return False    
win=0  
board=[['.', '.', '.' ,'.', '.', '.' ,'.'],['.', '.', '.' ,'.', '.', '.' ,'.'],['.', '.', '.' ,'.', '.', '.' ,'.'],['.', '.', '.' ,'.', '.', '.' ,'.'],['.', '.', '.' ,'.', '.', '.' ,'.'],['.', '.', '.' ,'.', '.', '.' ,'.']]
def startGame() :
    words = "Greetings Stranger(s)! "
    #Experimental Typing
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    print ""
    words = "Welcome to my Connect-4 Game! Do you know the rules to the game?(Y/N)"
    #Experimental Typing
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    c=raw_input("")
    if c=="N":
        words = "The rules of this game are simple you connect 4 of X's or the O's, vertically,horizontally or diagonally to win the game."
        for char in words:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
    print ""
    GameOn()
def GameOn():
    #The Game begins.
    t=0 
    while(t<=42):
        temp=1
        for row in board:
            sys.stdout.write(str(temp)+ " ")
            for x in row:
                sys.stdout.write(x+" ")
            print("")
            temp+=1
        sys.stdout.write("  ")
        for p in range(1,8):
            sys.stdout.write(str(p)+" ")
        print("")
        
        if t==42:
            #If the board is Full and there is no winner
            print("TIE! Game TIED!")
            break  
        k=0  
        if t%4==0:
            while(k==0):
                c=raw_input("Choose your column, mate "+str(t%2 + 1)+ "!(1-7): ")
                if c not in "0123456789" or c=="":
                    print "Choose an integer between 1-7!"
            
                else:
                    c=int(c)
                    if c<=0 or c>=8:
                        print "Choose between 1-7!"
                    elif not checkcolumn(c):
                        print "Column full,try another column!"
                    else:
                        board.reverse()
                        for x in board:
                            if x[c-1]=='.':
                                if t%2==0:
                                    x[c-1]='X'
                                    break
                                else:
                                    x[c-1]='O'
                                    break  
                        board.reverse()                       
                        k=1   
        elif t%4==2:
            while(k==0):
                c=raw_input("Choose your column, mate "+str(t%2 + 1)+ "!(1-7): ")
                if c not in "0123456789" or c=="":
                    print "Choose an integer between 1-7!"
            
                else:
                    c=int(c)
                    if c<=0 or c>=8:
                        print "Choose between 1-7!"
                    elif not checkcolumn2(c):
                        print "Column full,try another column!"
                    else:
                        for x in board:
                            if x[c-1]=='.':
                                if t%2==0:
                                    x[c-1]='X'
                                    break
                                else:
                                    x[c-1]='O'
                                    break                        
                        k=1   
        elif t%4==1:
            while(k==0):
                c=raw_input("Choose your row, mate "+str(t%2 + 1)+ "!(1-6): ")
                if c not in "0123456789" or c=="":
                    print "Choose an integer between 1-6!"
            
                else:
                    c=int(c)
                    if c<=0 or c>=7:
                        print "Choose between 1-6!"
                    elif not checkrow(c):
                        print "Row full,try another row!"
                    else:
                        for i in range(0,7):
                            if board[c-1][6-i]=='.':
                                if t%2==0:
                                    board[c-1][6-i]='X'
                                    break
                                else:
                                    board[c-1][6-i]='O'
                                    break                        
                        k=1 
        elif t%4==3:
            while(k==0):
                c=raw_input("Choose your row, mate "+str(t%2 + 1)+ "!(1-6): ")
                if c not in "0123456789" or c=="":
                    print "Choose an integer between 1-6!"
            
                else:
                    c=int(c)
                    if c<=0 or c>=7:
                        print "Choose between 1-6!"
                    elif not checkrow2(c):
                        print "Row full,try another row!"
                    else:
                        for i in range(0,7):
                            if board[c-1][i]=='.':
                                if t%2==0:
                                    board[c-1][i]='X'
                                    break
                                else:
                                    board[c-1][i]='O'
                                    break                        
                        k=1   
        if checkwin(t%2):
            for row in board:
                for x in row:
                    sys.stdout.write(x+" ")
                print ""
            break
        t=t+1;
        RotGrav(t%4)
        if checkwin(t%2):
            for row in board:
                for x in row:
                    sys.stdout.write(x+" ")
                print ""
            break
        if checkwin((t+1)%2):
            for row in board:
                for x in row:
                    sys.stdout.write(x+" ")
                print ""
            break
startGame()
