import random  #used to randomly select element from the list
def print_board(matrix):    #this function is defined to convert the list into number board
    for i in range(0,len(matrix)):   #to split the list
        matrix[i]=str(matrix[i])
        if(matrix[i]=='1' or matrix[i]=='2' or matrix[i]=='3' or matrix[i]=='4' or matrix[i]=='5' or matrix[i]=='6' or matrix[i]=='7' or matrix[i]=='8' or matrix[i]=='9' or matrix[i]=='0'):
            matrix[i]='0'+matrix[i]
    list1=matrix[0:5:]
    list2=matrix[5:10:]
    list3=matrix[10:15:]
    list4=matrix[15:20:]
    list5=matrix[20:25:]
    list6=[list1,list2,list3,list4,list5]
    pmatrix=[]
    for i in list6:
        pmatrix.append(i)
    for i in range(0,len(pmatrix)):
        print "   ".join(pmatrix[i])
    for i in range(0,len(matrix)):
        matrix[i]=int(matrix[i])
    return matrix
        
def check_bingo(matrix):    #check if the bingo has been made.
    z=0
    num1=num2=num3=num4=num5=num6=num7=num8=num9=num10=num11=num12=0
    a=matrix[0]+matrix[1]+matrix[2]+matrix[3]+matrix[4]
    b=matrix[5]+matrix[6]+matrix[7]+matrix[8]+matrix[9]
    c=matrix[10]+matrix[11]+matrix[12]+matrix[13]+matrix[14]
    d=matrix[15]+matrix[16]+matrix[17]+matrix[18]+matrix[19]
    e=matrix[20]+matrix[21]+matrix[22]+matrix[23]+matrix[24]
    f=matrix[0]+matrix[5]+matrix[10]+matrix[15]+matrix[20]
    g=matrix[1]+matrix[6]+matrix[11]+matrix[16]+matrix[21]
    h=matrix[2]+matrix[7]+matrix[12]+matrix[17]+matrix[22]
    i=matrix[3]+matrix[8]+matrix[13]+matrix[18]+matrix[23]
    j=matrix[4]+matrix[9]+matrix[14]+matrix[19]+matrix[24]
    k=matrix[0]+matrix[6]+matrix[12]+matrix[18]+matrix[24]
    l=matrix[4]+matrix[8]+matrix[12]+matrix[16]+matrix[20]
    if(a==0):
        num1=1
    if(b==0):
        num2=1
    if(c==0):
        num3=1
    if(d==0):
        num4=1
    if(e==0):
        num5=1
    if(f==0):
        num6=1
    if(g==0):
        num7=1
    if(h==0):
        num8=1
    if(i==0):
        num9=1
    if(j==0):
        num10=1
    if(k==0):
        num11=1
    if(l==0):
        num12=1
    z=num1+num2+num3+num4+num5+num6+num7+num8+num9+num10+num11+num12
    
    if(z==1):
        x=['X','I','N','G','O']
        return x
    elif(z==2):
        x=['X','X','N','G','O']
        return x
    elif(z==3):
        x=['X','X','X','G','O']
        return x
    elif(z==4):
        x=['X','X','X','X','O']
        return x
    elif(z==5):
        x=['X','X','X','X','X']
        return x
    elif(z==0):
        x=['B','I','N','G','O']
        return x
    else:
        x=['X','X','X','X','X']
        return x
    
        
print "PLAY BINGO !!"
learn=raw_input("Learn How to Start ? (y/n)")

if(learn=="y" or learn=="Y"):
    print "In this game you first Choose two variables a & b, these variables form a function in the form y=ax+b. This function is used to design your Matrix of order 5*5."
    print "This is a Player vs CPU game. Here the numbers are called out and cancelled in order to finish forming BINGO. The player to first finish BINGO is the winner"
else:
    print "The Game Begins !!"
a=input("Choose a number for a such that {gcd(a,25)=1} = ") #get the input to make the matrix
b=input("Choose a number for b=")
print "Your function is y="+str(a)+"x"+"+"+str(b)
print "So your matrix is:"  #this generate the number board to play
board=[]    #player board
for i in range(1,26):
    board.append(((a*i)+b)%25)
for i in range(len(board)):
    if(board[i]==0):
        board[i]=25
#print board
print_board(board)

random_integers=[]  #list for cpu to work on
for i in range(1,26):
    random_integers.append(i)
c=random.choice(random_integers)
if(c%5==0):
    c=c+1
d=random.choice(random_integers)
#print c,d
cpu_board=[]    #board for CPU
for i in range(1,26):
    cpu_board.append(((c*i)+d)%25)
for i in range(len(cpu_board)):
    if(cpu_board[i]==0):
        cpu_board[i]=25

#print_board(cpu_board)
#print random_integers
bingo=['B','I','N','G','O']
cpu_bingo=['B','I','N','G','O']
m=n=0
while(1):
    while(1):
        z=input("Please Enter number= ")    #start playing the game by giving the input
        if z not in random_integers:
            print "Don't repeat Number !!"
            break
        random_integers.remove(z)
        cpu_z=random.choice(random_integers)
        print "CPU's Number="+str(cpu_z)    #this generates the CPU number for board
#        print random_integers
        random_integers.remove(cpu_z)
        
#        print random_integers
        
        for i in range(0,len(cpu_board)):
            if(cpu_board[i]==z or cpu_board[i]==cpu_z):
                cpu_board[i]=0
        if z in board:
            for i in range(0,len(board)):
                if(board[i]==z or board[i]==cpu_z):
                    board[i]=0
        else:
            print "Invalid Input"
            break
        print "\n"
        p=check_bingo(board)
        print p
        if(p==['X','X','X','X','X']): #this checks for if player reached the bingo 
            m=1
            break
        
        print "\n"
        q=check_bingo(cpu_board)
#        print q
        if(q==['X','X','X','X','X']):   #this checks if CPU reached the bingo
            n=1
            break
        print_board(board)
        print "\n\n"
#        print_board(cpu_board)
    if(m==1 or n==1):
        break
print "GAME OVER"
if(m==1):
    print "YOU WIN !!"
if(n==1):
    print "YOU LOSE, CPU WINS !! BETTER LUCK NEXT TIME" #Declare the game

    

