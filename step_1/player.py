class Player:
    """
    This class represents a player of the tournament. It also represent the nodes of the AVL Tree
    """

    def __init__(self,id=None, score=0, total = 0, left = None, right = None,played_game=0):
        if id is None:
            raise ValueError('You have to set an id for the player')
        else:
            self.id = id
            self.value = score
            self.right = right
            self.left = left
            self.total = total
            self.played_game = played_game
            self.height = 1

    def re_init(self):
        """
        Function to set all atributes of the player at "zero" (like a new player)
        """
        self.value = 0
        self.total = 0
        self.played_game = 0
        self.height = 1
    
    def set_score(self):
        """
        Function to update the player score
        """
        if self.played_game != 0:
            self.value =  round(self.total / self.played_game,2)
    
    def get_score(self):
        """
        Function to get the player score
        """
        return self.value

    def set_total(self,new_score,add=True):
        """
        Function to set all the point of the player
        """
        if add :
            self.total += new_score
        else:
            self.total = new_score
    
    def update_games_number(self,new_games):
        """
        Function to update number of played games
        """
        self.played_game += new_games

    def get_id(self):
        """
        Function to get the player name/id
        """
        return self.id
    
    def refresh_childerns(self):
        """
        Function to set player as a leaf node (without childrens)
        """
        self.left = None
        self.right = None
    
    def __str__(self):
        return f'{self.id} : {self.value}'