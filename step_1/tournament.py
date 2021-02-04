import random
from .player import Player
from .database  import AVLTree

class Tournament : 
    
    def __init__(self):
        self.ranking = AVLTree()
        self.players = [Player(id= 'Player_'+str(i), score = 0) for i in range(1,101)]
        # Inserting players into database
        for player in self.players:
            self.ranking.root = self.ranking.insert_node(self.ranking.root,player,self.ranking) 


    def elimination_rounds(self):
        """
        Function to perform the first three games to rank players and to play the elimination games
        """
        print(f'Start Tournament ')
        print('\n--------------------------------\n')
        print('Pre-Eliminations Games (3 random games) : Done.')
        score_1 = [random.randint(0,12) for i in range(100)]
        score_2 = [x+random.randint(0,12) for x in  score_1]
        score_3 = [x+random.randint(0,12) for x in  score_2]
        
        self.update_ranking(score_3,match_played=3)
        print('\n--------------------------------\n')
        print('\nEliminations Rounds : \n')
        
        for i in range(9):
            
            print(f'Round {i+1} : \n')
            scores = [random.randint(0,12) for j in range(100 - i * 10)]
            self.update_ranking(scores)
            self.eject_last_ten()
            print('\n--------------------------------\n')
        
        print('Finalists Players : ')
        self.display_podium()

    def display_podium(self):
        """
        Function to print the best 10 players id
        """
        print()
        players = self.ranking.inorder(self.ranking.root)
        rank = 1
        for i in range(-1,-11, -1):
            print(f"{rank} : {players[i].id} ({players[i].value} points)")
            rank += 1

    
    def update_ranking(self,scores,match_played=1):
        """
        Function to update our ranking after each round. We create a new AVL tree after each round
        to store trhe new ranking.
        """
        new_ranking = AVLTree()
        i = 0
        players = self.ranking.inorder(self.ranking.root)
        for player in players:
            player.update_games_number(match_played)
            player.set_total(scores[i])
            player.set_score()
            player.refresh_childerns()
            new_ranking.root = new_ranking.insert_node(new_ranking.root,player,new_ranking)
            i+=1

        self.ranking = new_ranking
        
    def eject_last_ten(self):
        """
        Function to delete the 10 badest player based on them ranking
        """
        ejected = []
        for i in range(10):
            temp_node = self.ranking.get_min_value_node(self.ranking.root)
            ejected.append(temp_node.id)
            self.ranking.root = self.ranking.delete_node(self.ranking.root,temp_node,self.ranking)

        print('List of ejected player : ', ejected)
        print(f'{self.ranking.nodes_number} players remaining')

    def finals(self):
        """
        Function to play the finals games.
        """
        print('\n--------------------------------\n')
        print("Let's start finals : ")
        print('\n--------------------------------\n')
        print("Play 5 New Games : Done. ")
        print('\n--------------------------------\n')
        for player in self.ranking.inorder(self.ranking.root):
            player.re_init()
        final_scores = [0]*10
        final_scores = [[score+random.randint(0,12) for score in final_scores] for i in range(5)]
        final_scores = [sum(i) for i in zip(*final_scores)]
        self.update_ranking(scores = final_scores, match_played= 5)
        print('FINAL RANKING :')
        print('\n--------------------------------\n')
        self.display_podium()

    def run(self):
        """
        Function to run the first part of the tournament until the end.
        """
        self.elimination_rounds()
        self.finals()


