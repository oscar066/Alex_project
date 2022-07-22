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
            print ( chr( A[E] ), end=' ')
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
    print("\n\n --- ROBOT VERSION --- \n")

    # Getting input for the size of the board
    size = int(input("Enter an integer divisible by 3 for the game board:"))
    game_array = [46]* (size**2)

    #array_length = len(game_array)
    game_array = update(game_array,size)


    board(game_array,size)
    # Start position
    # For the robot
    robot_position = int((0.5 * size) + size - 1)
    # For the security guard
    gaurd_position = int((0.5 * size) * size + 1)

    # initializing the positions 
    # rogue robot
    game_array[robot_position] = 82
    # Security guard
    game_array[gaurd_position] = 83

    board(game_array,size)

    GAME_ON = True
    while(GAME_ON):
        # movement for the entities
        # Rogue Robot
        robot_position = move(game_array,robot_position,size)
        # Security guard
        gaurd_position = move(game_array,gaurd_position,size)

        # representing the movement of the entities with their letter
        # Rogue robot
        game_array[robot_position] = 82

        # Security guard
        game_array[gaurd_position] = 83
        board(game_array,size)

        # caution on shooting before reaching the intersection

        intersection = int((0.5 * size) * size + 1) + ((size / 3) - 1)
        intersection_2 = int(((size / 3 * 2) * size) * size + 1) + ((size / 3) - 1)
        
        if (gaurd_position >= intersection and gaurd_position < intersection_2):
            phaser(game_array,gaurd_position,size)
            
        #elif (gaurd_position < intersection and phaser(game_array,gaurd_position,size)):
            #print("-!!!- The Security Gaurd blasted himself -!!!-")
            #GAME_ON = False

        # adding Explosion after the robot has been hit
        # adding shooting down the rogue robot
        
        #shooting_range = []
        #for i in list(range(5)):
            #shooting_range.append(gaurd_position[i])
            #if robot_position in shooting_range:
                #print("-**- The Robot has been terminated -**-")
                #print("-****- The Security Guard has Won the game -****-")
                #GAME_ON = False

        if gaurd_position == robot_position:
            print("-**- The Robot has been terminated -**-")
            print("-****- The Security Guard has Won the game -****-")
            GAME_ON = False
            
        # An if-else statement to ensure looping until the condition is reached
        # Winning the game 
        antimatter_location = int(size * (size - 2) + 1)
        
        if robot_position >= antimatter_location:
            print("-****-The Robot Wins the Game-****-")
            GAME_ON = False

        elif gaurd_position >= antimatter_location:
            print("\n\n-****-The Security gaurd Wins the Game -****-\n ")
            GAME_ON = False

        #if (robot_position > 89 and gaurd_position > 200):
            #GAME_ON = False


if __name__ == "__main__":
    main()