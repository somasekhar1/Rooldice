import random as r #Import random Module for Shuffling.
i=[[6,1],[3,4],[5,2]]# i is initial Position of Dice.
print('initial values: ',i)


print(f"""                      back:{i[1][1]}
                +---------------------+
               /                     /|
              /        Top:{i[0][0]}        / |
             /                     /  |
            /                     /   |right:{i[2][1]}
           +---------------------+    |
           |                     |    |
           |                     |    |
    left:{i[2][0]} |                     |    |
           |                     |    +
           |      front:{i[1][0]}        |   /
           |                     |  /
           |                     | /
           +---------------------+
                    bottom:{i[0][1]}
                    
****************Let's Play******************                                       """)

r.shuffle(i)
x=i # x is Shuffled List.
print('After shuffling: ',x)



def dice():
        """ dice() function returns the final position of dice. """
        while(True):
        
            if select=='r':
                x[0][0],x[2][1],x[0][1],x[2][0]=i[2][0],i[0][0],i[2][1],i[0][1]
        
            return print(f"""                      back:{i[1][1]}
                +---------------------+
               /                     /|
              /        Top:{i[0][0]}        / |
             /                     /  |
            /                     /   |right:{i[2][1]}
           +---------------------+    |
           |                     |    |
           |                     |    |
    left:{i[2][0]} |                     |    |
           |                     |    +
           |      front:{i[1][0]}        |   /
           |                     |  /
           |                     | /
           +---------------------+
                    bottom:{i[0][1]}                             
                                                                   """)
    
    
    
            if select=='l':
                x[2][0],x[0][0],x[2][1],x[0][1]=i[0][0],i[2][1],i[0][1],i[2][0]
                return print(f"""                      back:{i[1][1]}
                +---------------------+
               /                     /|
              /        Top:{i[0][0]}        / |
             /                     /  |
            /                     /   |right:{i[2][1]}
           +---------------------+    |
           |                     |    |
           |                     |    |
    left:{i[2][0]} |                     |    |
           |                     |    +
           |      front:{i[1][0]}        |   /
           |                     |  /
           |                     | /
           +---------------------+
                    bottom:{i[0][1]}                             
                                                                   """)

            if select=='u':
                x[0][0],x[1][1],x[1][0],x[0][1]=i[1][0],i[0][0],i[0][1],i[1][1]
                return print(f"""                      back:{i[1][1]}
                +---------------------+
               /                     /|
              /        Top:{i[0][0]}        / |
             /                     /  |
            /                     /   |right:{i[2][1]}
           +---------------------+    |
           |                     |    |
           |                     |    |
    left:{i[2][0]} |                     |    |
           |                     |    +
           |      front:{i[1][0]}        |   /
           |                     |  /
           |                     | /
           +---------------------+
                    bottom:{i[0][1]}                             
                                                                   """)

            if select=='d':
                x[1][0],x[0][0],x[0][1],x[1][1]=i[0][0],i[1][1],i[1][0],i[0][1]
                return print(f"""                      back:{i[1][1]}
                +---------------------+
               /                     /|
              /        Top:{i[0][0]}        / |
             /                     /  |
            /                     /   |right:{i[2][1]}
           +---------------------+    |
           |                     |    |
           |                     |    |
    left:{i[2][0]} |                     |    |
           |                     |    +
           |      front:{i[1][0]}        |   /
           |                     |  /
           |                     | /
           +---------------------+
                    bottom:{i[0][1]}                             
                                                                   """)

        
    


def right():
        """ This function rotates dice to the Right side """
        x[0][0],x[2][1],x[0][1],x[2][0]=i[2][0],i[0][0],i[2][1],i[0][1]   
        return x

def left():
        """ This function rotates dice to the Left side """
        x[2][0],x[0][0],x[2][1],x[0][1]=i[0][0],i[2][1],i[0][1],i[2][0]
        return x

def up():
        """ This function rotates dice to the Up side """
        x[0][0],x[1][1],x[1][0],x[0][1]=i[1][0],i[0][0],i[0][1],i[1][1]
        return x

def down():
        """ This function rotates dice to the Down side """
        x[1][0],x[0][0],x[0][1],x[1][1]=i[0][0],i[1][1],i[1][0],i[0][1]
        return x



while True:
  select = input('pick your move\nR/L/U/D/Q : ').lower()
  if select == 'r':
    print(right())
  elif select == 'l':
    print(left())
  elif select == 'u':
    print(up())
  elif select == 'd':
    print(down())
  elif select == 'q':
    print("")
    print("**********Hey!!! This is Your Final Dice**********")
    print()
    (dice())
    print("*******************Thank You*********************")
    break
  else:
          print("This is Invalid move \nPlease Enter R/L/U/D to Rotate or Q to Quit. ")
