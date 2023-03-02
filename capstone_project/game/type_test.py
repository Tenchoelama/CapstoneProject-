from flask import Blueprint, Flask, render_template, request
import time
import requests




def type_test():
    
   
    while True:
        
        
        option = input("\nHit Enter to start the timer or 'q' to Quit the game. Hit Enter again once you are done typing: ")
        
        words ="""\nWhen Mr. Bilbo Baggins of Bag End announced that he would shortly be
                celebrating his eleventy-first birthday."""
                
        
        
        if option.lower() == 'q':
            print("\nThank you for playing. Come test your speed next time!")
            break
        else:
            
            print(words)
        
        
        print("\nTimer Started! Start Typing!!")
        start = time.time()
        
        timeout = start + 5  # set the timeout to 30 seconds
        
        while time.time() < timeout:
        
        
            
            user_input = str(input('\nEnter here: '))
            
            end = time.time()
            
            wordcount=len(words.split())#counts the number of words in a string
        
            user_words = set(user_input.split())#splits the words individualy and stores them in a set
            # print(user_words)
        
            correct_words = set(words.split()).intersection(user_words)#finds the set intersection between the set of words 
            #from the paragrpah and the set of words from user_words to find the common matching words. 
            # print(correct_words)
        
            accuracy = len(correct_words) / wordcount * 100 #calculates the precentage of words typed correctly 
        
            total_time = end - start 
        
            wpm = len(correct_words) / total_time * 60 #calculates words typed per minute
        
            print("Words Per Minute(wpm): ", round(wpm, 2), "\nAccuracy: ", round(accuracy, 2),"%", "\nTimetaken: ", round(total_time, 2),"secs")
    
            break
    
type_test()  