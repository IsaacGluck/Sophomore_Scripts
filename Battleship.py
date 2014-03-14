from random import randint

board = []

for x in range(0,5):
  board.append(["o"] * 5)

def print_board(board):
  for row in board:
    print ' '.join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#gives away location \/
print ship_row
print ship_col

for turn in range(5):
    guess_row = input("Guess Row:") - 1
    guess_col = input("Guess Col:") - 1
    print
    
    if guess_row == ship_row and guess_col == ship_col:
      print "Congratulations! You sunk my battleship!"
      print
      break
    else:
      if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
        print "Oops, that's not even in the ocean."
        print
      elif(board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
        print
      else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
        print
      if turn == 4:
        print 'Game Over'
        print 'The ship was at ' + '(' + str(ship_row + 1) + ', ' +  str(ship_col + 1) + ')'
        break
    
        print
    print 'Turn:' + str(turn + 1)
    print str(5 - (turn + 1)) + ' turns left'
    print
    print
    print_board(board)
