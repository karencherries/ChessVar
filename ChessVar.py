class ChessVar:
    """Represents a variation of chess called fog of wars."""

    def __init__(self):
        self._captured_piece = None
        self._round_number = 1
        self._player = "white"
        self._game_state = "UNFINISHED"
        self._board = {
            'audience': [
                ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
            ],
            'white': [],
            'black': []
        }
        self.dark_chess()

    def get_board(self, player):
        """Returns the board specific to the player."""
        return self._board[player]

    def get_game_state(self):
        """Returns the current game state."""
        return self._game_state

    def get_player(self):
        """Returns the player whose turn it is."""
        return self._player

    def converts_chess_notation(self, chess_notation):
        """Converts chess notation to index coordinates."""
        col, row = chess_notation
        index_row = abs(int(row) - 8)  # Convert rank to row index
        index_col = ord(col) - 97  # Convert file (a-h) to column index
        return index_row, index_col

    def make_move(self, square_from, square_to):
        """Validates and makes the move specified by the source and destination squares."""
        square_from_coordinate = self.converts_chess_notation(square_from)
        square_to_coordinate = self.converts_chess_notation(square_to)

        # Validate source and destination coordinates are within bounds
        for coordinate in [square_from_coordinate, square_to_coordinate]:
            if not (0 <= coordinate[0] <= 7) or not (0 <= coordinate[1] <= 7):
                return False

        # Validate starting square is not empty
        start_piece = self._board['audience'][square_from_coordinate[0]][square_from_coordinate[1]]
        if start_piece == " ":
            return False

        # Validate the piece belongs to the current player
        current_player = self.get_player()
        if current_player == "white" and "a" <= start_piece <= "z":
            return False
        if current_player == "black" and "A" <= start_piece <= "Z":
            return False

        # Generate possible moves
        direction = self.find_direction(square_from_coordinate)
        move_list = self.move_generator(direction, square_from_coordinate)

        # Verify destination square is valid
        if square_to_coordinate not in move_list:
            return False

        # Update board for a valid move
        self._board['audience'][square_to_coordinate[0]][square_to_coordinate[1]] = start_piece
        self._board['audience'][square_from_coordinate[0]][square_from_coordinate[1]] = " "
        self.dark_chess()  # Update fog of war

        # Update round and player turn
        self._round_number += 1
        self._player = "black" if self._player == "white" else "white"

        # Check for game state updates (e.g., king capture)
        self.update_game_state()

        # Return True indicating successful move
        return True

    def find_direction(self, square_from_coordinate):
        """Determines move direction based on the piece type."""
        letter_from = self._board['audience'][square_from_coordinate[0]][square_from_coordinate[1]]

        # Define movement rules for chess pieces
        if letter_from == "P":
            moves = [(-1, 0), (-2, 0)] if square_from_coordinate[0] == 6 else [(-1, 0)]
            moves += [(-1, -1), (-1, 1)]  # Diagonal capture
            return moves
        if letter_from == "p":
            moves = [(1, 0), (2, 0)] if square_from_coordinate[0] == 1 else [(1, 0)]
            moves += [(1, -1), (1, 1)]  # Diagonal capture
            return moves
        if letter_from in "Rr":
            return [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if letter_from in "Bb":
            return [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        if letter_from in "Qq":
            return [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        if letter_from in "Kk":
            return [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        if letter_from in "Nn":
            return [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        # Return empty list if no valid moves (for unknown pieces)
        return []

    def move_generator(self, direction, square_from_coordinate):
        """Generates valid moves for a piece based on its direction of movement."""
        list_of_moves = []
        for dx, dy in direction:
            x, y = square_from_coordinate
            if abs(dx) + abs(dy) > 2:  # Sliding pieces like rooks, bishops, queens
                while 0 <= x + dx <= 7 and 0 <= y + dy <= 7:
                    x += dx
                    y += dy
                    if self._board['audience'][x][y] != " ":  # Stop if piece blocks
                        if self._board['audience'][x][y].isalpha():  # Capture opponent
                            list_of_moves.append((x, y))
                        break
                    list_of_moves.append((x, y))
            else:  # Non-sliding pieces like knights or kings
                x, y = square_from_coordinate[0] + dx, square_from_coordinate[1] + dy
                if 0 <= x <= 7 and 0 <= y <= 7:
                    if self._board['audience'][x][y] == " " or \
                            self._board['audience'][x][y].isalpha():
                        list_of_moves.append((x, y))

        return list_of_moves

    def dark_chess(self):
        """Updates the fog of war, hiding the opponent's pieces from the player."""
        deep_copy_white = [[('*' if "a" <= letter <= "z" else letter) for letter in row] for row in self._board['audience']]
        deep_copy_black = [[('*' if "A" <= letter <= "Z" else letter) for letter in row] for row in self._board['audience']]
        self._board['white'] = deep_copy_white
        self._board['black'] = deep_copy_black

    def update_game_state(self):
        """Updates the game state to check for victory conditions."""
        if "K" not in [piece for row in self._board['audience'] for piece in row]:
            self._game_state = "BLACK_WON"
        if "k" not in [piece for row in self._board['audience'] for piece in row]:
            self._game_state = "WHITE_WON"