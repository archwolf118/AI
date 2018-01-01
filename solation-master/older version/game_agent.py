"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random

# place_value ={}

# temp_row = 3

# block_groups = {}

# block1 = []
# block2 = []
# block3 = []
# block4 = []

# for i in range(1,8):
#     temp = 3
#     for j in range(1,8):
#         if j <=4 and i <= 4:
#             place_value[(i-1, j-1)] = i*j
#             block1.append((i-1,j-1))

#         elif i <= 4 and  j > 4:
#             place_value[(i-1, j-1)] = i * temp
#             temp = temp -1
#             block2.append((i-1, j-1))

#         elif j <= 4 and i > 4:
#             place_value[(i-1, j-1)] = j* temp_row

#             block3.append((i-1, j-1))

#         elif j > 4 and  i > 4:
#             place_value[(i-1, j-1)] = temp * temp_row
#             temp = temp - 1
#             block4.append((i-1, j-1))

#     if i > 4:
#         temp_row = temp_row - 1

# print(place_value)
# # print(block2)
# # print(block3)
# # print(block4)

# # print(len(block1) + len(block2) + len(block3) + len(block4))


place_value ={
(0, 0): 1, (0, 1): 2, (0, 2): 3, (0, 3): 4, (0, 4): 3, (0, 5): 2, (0, 6): 1, 
(1, 0): 2, (1, 1): 4, (1, 2): 6, (1, 3): 8, (1, 4): 6, (1, 5): 4, (1, 6): 2, 
(2, 0): 3, (2, 1): 6, (2, 2): 9, (2, 3): 12, (2, 4): 9, (2, 5): 6, (2, 6): 3, 
(3, 0): 4, (3, 1): 8, (3, 2): 12, (3, 3): 16, (3, 4): 12, (3, 5): 8, (3, 6): 4, 
(4, 0): 3, (4, 1): 6, (4, 2): 9, (4, 3): 12, (4, 4): 9, (4, 5): 6, (4, 6): 3, 
(5, 0): 2, (5, 1): 4, (5, 2): 6, (5, 3): 8, (5, 4): 6, (5, 5): 4, (5, 6): 2, 
(6, 0): 1, (6, 1): 2, (6, 2): 3, (6, 3): 4, (6, 4): 3, (6, 5): 2, (6, 6): 1}





class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    score = 0.0

    for move in game.get_legal_moves(player):
        score += place_value[move]

    return score
    # raise NotImplementedError

def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_score = 0.0
    opp_score = 0.0

    for move in game.get_legal_moves(player):
        own_score += place_value[move]

    for move in game.get_legal_moves(game.get_opponent(player)):
        opp_score += place_value[move]

    return own_score - opp_score
    # raise NotImplementedError


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_score = 0.0
    opp_score = 0.0

    for move in game.get_legal_moves(player):
        own_score += place_value[move]

    for move in game.get_legal_moves(game.get_opponent(player)):
        opp_score += place_value[move]

    return own_score - 2 * opp_score


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        
        legal_moves = game.get_legal_moves()
        
        if not legal_moves:
            return (-1, -1)

        best_move = legal_moves[0]
        best_score = float("-inf")

        for move in legal_moves:
            v = self.min_value(game.forecast_move(move), depth-1)
            if v > best_score:
                best_score = v
                best_move = move
        return best_move

    def max_value(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        if depth == 0 or not game.get_legal_moves():
            return self.score(game, game.active_player)

        v = float("-inf")

        for m in game.get_legal_moves():
            v = max(v, self.min_value(game.forecast_move(m), depth-1))

        return v

    def min_value(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        if depth == 0 or not game.get_legal_moves():
            return self.score(game, game.inactive_player)

        v = float("inf")

        for m in game.get_legal_moves():
            v = min(v, self.max_value(game.forecast_move(m), depth-1))
        return v

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # TODO: finish this function!

        best_move = (-1, -1)





        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.

            depth = 1
            while self.time_left() > 0:
                best_move = self.alphabeta(game, depth, float("-inf"), float("inf"))
                depth += 1

            # return self.alphabeta(game, self.search_depth, float("-inf"), float("inf"))

        except SearchTimeout:
            return best_move  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        
        
        legal_moves = game.get_legal_moves()
        
        if not legal_moves:
            return (-1, -1)

        best_move = legal_moves[0]
        # best_score = float("-inf")

        for m in legal_moves:
            v = self.min_value(game.forecast_move(m), depth-1, alpha, beta)
            if v > alpha:
                alpha = v
                best_move = m
        return best_move


    def max_value(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        if depth == 0 or not game.get_legal_moves():
            return self.score(game, game.active_player)

        v = float("-inf")

        for m in game.get_legal_moves(): 
            v = max(self.min_value(game.forecast_move(m), depth-1, alpha, beta), v)

            if v >= beta:
                return v               
            alpha = max(alpha, v)

        return v


    def min_value(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        if depth == 0 or not game.get_legal_moves():
            return self.score(game, game.inactive_player)

        v = float("inf")

        for m in game.get_legal_moves():
            v = min(self.max_value(game.forecast_move(m), depth-1, alpha, beta), v)
            if v <= alpha:
                return v
            beta = min(beta, v)

        return v
