from Game import Game
import json
import os
import sys

def main()->None:
    # initialize and run the Tetris game
    print("Welcome to Tetris!")
    try:
        currentHighscore = json.load(open(os.path.join(sys.path[0],"highscore.json"), "r"))
    except FileNotFoundError:
        currentHighscore = 0
    TR = selectDifficulty()
    SP = selectGameMode()
    print ("Starting game with tickrate: " + str(TR))
    game = Game(tickrate=TR, highscore=currentHighscore, gliched=SP)
    game.run()
    # Save highscore
    json.dump(game.board.score, open(os.path.join(sys.path[0],"highscore.json"), "w"))
    return 

def selectDifficulty():
        '''
        None -> Int
        Prompts the user to select a difficulty level and returns the tickrate.
        '''
        print("Select a difficulty level (1-5):")
        print("1. Easy")
        print("2. Normal")
        print("3. Hard")
        print("4. Expert")
        print("5. Impossible")
        
        while True:
            try:
                difficulty = int(input("Enter a number: "))
                if difficulty in range(1,6):
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Please enter a number between 1 and 5.")
        return difficulty*2-1

def selectGameMode():
        '''
        None -> Int
        Prompts the user to select a game mode and returns the game mode.
        '''
        print("Select a game mode (1-2):")
        print("1. Normal")
        print("2. Gliched")
        print("\t Gliched mode is a mode where the controls are reversed.")
        
        while True:
            try:
                gameMode = int(input("Enter a number: "))
                if gameMode in range(1,3):
                    break
                else:
                    print("Please enter a number between 1 and 2.")
            except ValueError:
                print("Please enter a number between 1 and 2.")
        return gameMode-1

if __name__ == "__main__":
    main()
    