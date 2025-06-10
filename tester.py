from ChessVar_revise import *
game = ChessVar()

print(game.make_move('d2', 'd4'))
print(game.make_move('c7', 'c5'))
print(game.make_move('d4', 'd5'))   #white pawn eats dark pawn is okay
print(game.make_move('d8', 'a5'))
print(game.make_move('b2', 'b4'))

print(game.make_move('d7', 'd6'))
print(game.make_move('b4', 'b5')) #white pawn eats dark queen is okay
print(game.make_move('a7', 'a5'))
print(game.make_move('c1', 'h6'))
print(game.make_move('c8', 'h3'))

print(game.make_move('b1', 'c3'))
print(game.make_move('g7', 'g6'))   #dark pawns eats white bishop is okay
print(game.make_move('g2', 'g3'))       #white pawn eats dark bishop is okay
print(game.make_move('g6', 'g5'))
print(game.make_move('f1', 'h3'))
print(game.make_move('a5', 'a3'))

print(game.make_move('h3', 'c8'))
print(game.make_move('e7', 'e6'))
print(game.make_move('e2', 'e3'))
print(game.make_move('f8', 'h6'))
print(game.make_move('h2', 'h3'))
print(game.make_move('g5', 'g4'))
print(game.make_move('e3', 'e4'))

print(game.make_move('h6', 'c1'))
print(game.make_move('e4', 'e5'))
print(game.make_move('g8', 'h6'))
print(game.make_move('d1', 'g4'))
print(game.make_move('f7', 'f6'))
print(game.make_move('f2', 'f3'))
print(game.make_move('c1', 'd2'))

print(game.make_move('f3', 'f4'))
print(game.make_move('d2', 'e1'))
print(game.make_move('b2', 'b3'))#check empty piece starts with
print(game.make_move('h1', 'h2'))#check already end of game
print(game.get_game_state())


views = [
    game.get_board("audience"),
    game.get_board("black"),
    game.get_board("white")
]
for view in views:
    print()
    for row in view:
        print(row)