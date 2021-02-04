# -*- coding: utf-8 -*-

from step_1.tournament import Tournament
from step_2.find_impostors import GetImpostors
from step_3.clues import TimeComparator
from step_4.hamiltonian_path import EndTask

def run_first():
    print('''
    ##############
    # First Step #
    ##############
    ''')
    Tournament().run()

def run_second():
    print('''
    ###############
    # Second Step #
    ###############
    ''')
    GetImpostors().run()

def run_third():
    print('''
    ##############
    # Third Step #
    ##############
    ''')
    TimeComparator().run()

def run_fourth():
    print('''
    ###############
    # Fourth Step #
    ###############
    ''')
    EndTask().run()


if __name__ == '__main__':
    

    while True :
        print("""
        ######################################
        # Welcome to the Among US Tournament #
        ######################################

        """)
        choice = int(input('If you want to display all the steps please clique 1 , else click 0 to select the step to display :  '))

        if choice == 1 :

            run_first()
            run_second()
            run_third()
            run_fourth()

        if choice == 0:
            step = int(input('Now Please choose the number oh the step you want to run (1, 2, 3, or 4) : '))

            if step == 1:
                run_first()
            elif step == 2 :
                run_second()
            elif step == 3 :
                run_third()
            elif step == 4 :
                run_fourth()
        restart = input('If you want to restart click ENTER, else write "exit" : \n')

        if restart == 'exit':
            break
