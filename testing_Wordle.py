

import webbrowser
import time


#Word list file (Same Directory as this script)
with open("2nd.txt","r") as words:
    # changing the 
    contents = words.read()
    


def search():

            #input yesterdays wordle
            Yesterdays_Wordle = input("Yesterdays Wordle : ")
            #checking that the input is in the list
            if Yesterdays_Wordle in contents:
                #redundent change (Not needed)
                words = contents
                

                next_word = words[words.index(Yesterdays_Wordle)- 7]
            

                #letter 2
                next_word1 = words[words.index(Yesterdays_Wordle)- 8]
                #Letter 3
                next_word2 = words[words.index(Yesterdays_Wordle)- 9]
                #Letter 4
                next_word3 = words[words.index(Yesterdays_Wordle)- 10]
                #Letter 5
                next_word4 = words[words.index(Yesterdays_Wordle)- 11]
                #Output 
                today = next_word + next_word1 + next_word2 + next_word3 + next_word4
                print("Todays wordle is : "+ today)
                
            else:
                print("Not Found")

search()