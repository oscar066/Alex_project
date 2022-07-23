# Programming Concepts Coursework
# Random robot
# July 2022 
# https://www.onlinegdb.com/online_python_compiler

def adjust(A):
    # A is size
    # B is third of size
    B = A % 3
    A = A + ( 3 - B ) * ( B != 0 )
    return A

def board(A, B):
    # A is game array
    # B is size
    # C is loop control variable
    # D is loop control variable
    # E is array subscript
    for C in range( B ):
        for D in range( B ):
            E = C * B + D
            print ( chr( A[E] ), end = "")
        print ()
    print ()

def square(A, B, C):
    # A is array
    # B is location
    # C is square size
    # D is loop control variable
    # E is loop control variable
    # F is array subscript
    # G is ASCII 
    G = 32
    for D in range( C  ):
        for E in range( C ):
            F = B + D + E * C * 3
            G = G + 3 * ( F == ( 3 * C * C + C ) )
            A[F] = G
    return A
            
def update(A, B):
    # A is array
    # B is size
    # C is third of side
    # D is product of B and C
    # E is subscript
    # F is loop control variable
    C = int ( B / 3 )
    D = B * C
    A = [46] * B * B
    # Add five squares
    A = square(A, 0, C)
    E =  C * 2 
    A = square(A, E, C)
    E = C + D 
    A = square(A, E, C)
    E = D * 2
    A = square(A, E, C)
    E =  2 * ( C + D )
    A = square(A, E, C)
    # Add border
    for F in range( B ):
        E = F
        A[E] = 32 
        E = F * B
        A[E] = 32
        E = F * B + B - 1 
        A[E] = 32 
        E = B * ( B - 1 ) + F
        A[E] = 32
    return A

def move(A, B, C):
    # A is array
    # B is location
    # C is size
    # D is direction
    # E is increment
    # F is new location
    D = input ("Enter direction: U, D, L, R? ")
    E = -(D=="U")*C + (D=="D")*C - (D=="L") + (D=="R")
    F = B + E
    if ( F != 32):
        B = F
    return B

def phaser(A, B, C):
    # A is array
    # B is location
    # C is size
    # D is direction
    # E is loop control variable
    # F is missile 
    # G is increment
    # H is target location
    # J is user response
    F = B
    H = 0
    D = input ("Fire: U, D, L, R? ")
    G = -(D=="U")*C + (D=="D")*C - (D=="L") + (D=="R")
    for E in range( 5 ):
        F = F + G
        if ( A[F] == 82 ):
            H = F
        if ( A[F] == 35 or A[F] == 46 ):
            A[F] = 111
    board(A, C)
    J = input ( "Press enter to continue" )
    A = update (A, C)
    return A, H

def explosion(A, B, C):
    # A is array
    # B is location
    # C is size
    # D is phaser range
    # E is loop control variable
    # F is explosion subscript
    # G is user response
    D = int ( C / 2 )
    F = 0
    for E in range(D):
        F = B - C * E
        A[F] = 42
        F = B - ( C + 1 ) * E
        A[F] = 42
        F = B + E
        A[F] = 42
        F = B + ( C + 1 ) * E
        A[F] = 42
        F = B + C * E
        A[F] = 42
        F = B + ( C - 1 ) * E
        A[F] = 42
        F = B - E
        A[F] = 42
        F = B - ( C - 1 ) * E
        A[F] = 42
    board(A, C)
    G = input ( "Press enter to continue" )
    A = update (A, C)
    return A

def main():

    # Initializes the game array
    game_array = []
    
    print("Let's play Random Robot")
    # A try block to make sure that inputs are numbers
    try:
        #varible to hold the board size
        size_a = int(input("\n Enter the size of your  board:\n "))

        #Applying ans storing the new board size
        adjust_a = adjust(size_a)
        #returns the array that is used to update the board
        update_a = update(game_array,adjust_a)

        board(update_a, adjust_a)

        while True:

            #Toggling between Security guard abd the robot

            print("Player Security Guard\n")
            
            guard_pos = move(update_a,adjust_a,adjust_a)

            

            print("Player Robot\n")

            robot_pos = move(update_a,adjust_a,adjust_a)

            print("Player security guard")

            #storing the new game array on  array and new guard position 

            array,_pos = phaser(update_a,guard_pos,adjust_a)

            update_a = update(array,adjust_a)

            #checks whether the robot and guard have collided
            if(_pos == robot_pos):
                an_array = explosion(array,robot_pos,adjust_a)
                print("Robot Wins")
                break
            # if phraser is 0 then Guard wins
            elif(_pos == 0):
                print("Security Guard wins")
                an_array = explosion(array,robot_pos,adjust_a)
                break
    except:
        print("only integers are accepted, try a number \n")
        main()

main()



