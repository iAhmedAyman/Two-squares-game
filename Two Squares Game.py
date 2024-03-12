#Program: This game is played on a board of 4 x 4 squares. Two players take turns;
#each of them takes turn to place a rectangle (that covers two squares) on the board, covering
#any 2 squares. Only one rectangle can be on a square. A square cannot be covered twice. The
#last player who can place a card on the board is the winner.
#Author: Name) Ahmed Ayman Saeed Bakry, ID) 20230008
#Version: 2.0
#Date: 1/3/2024

#these are used for terminal colors
RED = "\033[91m"
BLUE = "\033[34m"
END = "\033[0m"

#this is the board
grid = [['1', '2', '3', '4'],
        ['5', '6', '7', '8'],
        ['9', '10', '11', '12'],
        ['13', '14', '15', '16']]

#this function fill the grid with numbers so players can play again
def clear_grid():
    counter = 1
    for i in range(4):
        for j in range(4):
            grid[i][j] = str(counter)
            counter += 1

#this function prints the current grid
def print_grid():
    values = []
    for row in grid:
        values.extend(row)
    values_index = 0
    for i in range(9):
        for j in range(4):
            if i % 2 == 0:
                print("+ - - ", end='')
            elif 'X' in values[values_index] or values_index < 9:
                print(f"|  {values[values_index]}  ", end='')
                values_index += 1
            else:
                print(f"| {values[values_index]}  ", end='')
                values_index += 1
        if i % 2 == 0:
            print("+")
        else:
            print("|")

#this function checks if the game is over
def win_check():
    for i in range(4):
        for j in range(4):
            #if the square's value is X, then it can't be coverd again. else check if there is a square next to it that is not covered
            if 'X' in grid[i][j]:
                continue
            elif i - 1 >= 0 and not 'X' in grid[i - 1][j]:
                return False
            elif j - 1 >= 0 and not 'X' in grid[i][j - 1]:
                return False
            elif i + 1 <= 3 and not 'X' in grid[i + 1][j]:
                return False
            elif j + 1 <= 3 and not 'X' in grid[i][j + 1]:
                return False
    return True

#player gameplay
def player_move(player_number, color):
        print(f"{color}Player {player_number}{END}, please choose two squares, next to each other, to cover")
        while True:
            #get input from the player. 
            #the input has to be a not covered square in the grid
            first_square = input("First square: ")
            while not first_square.isdigit() or int(first_square) < 1 or int(first_square) > 16:
                first_square = input("Invalid input, please choose a number from the grid that wasn't chosen before.\nFirst square: ")
            
            second_square = input("Second square: ")
            while not second_square.isdigit() or int(second_square) < 1 or int(second_square) > 16:
                second_square = input("Invalid input, please choose a number from the grid that wasn't chosen before.\nSecond square: ")
           
            first_square = int(first_square)
            second_square = int(second_square)
            if not abs(first_square - second_square) == 4 and not abs(first_square - second_square) == 1:
                print("Invalid input, please choose two adjacent squares.")
                continue
        
            #get grid coordinates for the first square
            first_coordinates = [0, 0]
            while first_square > 4:
                first_square -= 4
                first_coordinates[1] += 1
            first_coordinates[0] = first_square - 1

            #get grid coordinates for the second square
            second_coordinates = [0, 0]
            while second_square > 4:
                second_square -= 4
                second_coordinates[1] += 1
            second_coordinates[0] = second_square - 1

            #check if the squares are covered
            if 'X' in grid[first_coordinates[1]][first_coordinates[0]] or 'X' in grid[second_coordinates[1]][second_coordinates[0]]:
                print("Invalid input, one or both of these two are covered. Please try again")
                continue
            else:
                grid[first_coordinates[1]][first_coordinates[0]] = color + "X" + END
                grid[second_coordinates[1]][second_coordinates[0]] = color + "X" + END
                break

    
def main():
    while True:
        #main menu
        print("-----Welcome to the Two squares game-----")
        print("This game is played on a board of 4 x 4 squares. Two players take turns; each of them takes turn to place a rectangle (that covers two squares) on the board, covering any 2 squares. Only one rectangle can be on a square. A square cannot be covered twice. The last player who can place a card on the board is the winner.")
        menu_choice = input("A)Start\nB)Exit\n")
        while not menu_choice.upper() == 'A' and not menu_choice.upper() == 'B':
            menu_choice = input("Invalid choice, please try again\nA)Start\nB)Exit\n")
        if menu_choice.upper() == 'B':
            break
        
        #gameplay
        while True:
            print_grid()
            player_move(1, RED)
            if win_check():
                print_grid()
                print(f"No more squares to cover. {RED}Player 1 wins!{END}")
                break
            print_grid()
            player_move(2, BLUE)
            if win_check():
                print_grid()
                print(f"No more squares to cover. {BLUE}Player 2 wins!{END}")
                break
        clear_grid()
main()