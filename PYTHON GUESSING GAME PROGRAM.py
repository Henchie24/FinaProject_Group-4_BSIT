#This system determines what word will be used in the game according to what diffuclty the player wants.
easylist = [
    #3 letter words
    "and", "are", "for", "own", "put", "all", "but", "not", "yet", "out", "you", "yes", "fun", "get", "one", "act", "old", "new", "run", "war", 
    "now", "net", "may", "win", "air", "ask", "fit", "big", "god", "row",

    #4 letter words
    "four", "five", "come", "cool", "game", "gold", "good", "gone", "here", "have", "keep", "life", "like", "love", "main", "move", "more", 
    "near", "only", "push", "pull", "ride", "stay", "tree", "word", "hope", "hide", "kick", "sell", "also",

    #5 letter words
    "about", "above", "again", "after", "agree", "ahead", "alive", "allow", "among", "apart", "apply", "being", "black", "block", "bring", 
    "build", "cause", "child", "clean", "clear", "close", "could", "dance", "early", "every", "found", "given", "great", "happy", "human"
    ]

normallist = [
    #6 letter words
    "accept", "access", "affect", "agency", "amount", "animal", "appear", "artist", "attack", "author", "better", "beyond", "branch", "camera", 
    "carbon", "career", "circle", "client", "common", "copper", "damage", "debate", "decade", "defend", "demand", "depend", "design", "direct", 
    "effect", "effort",

    #7 letter words
    "ability", "account", "advance", "affect", "agency", "artist", "author", "average", "beauty", "because", "better", "budget", "camera", 
    "capital", "career", "choice", "comfort", "connect", "control", "design", "device", "direct", "effect", "family", "feature", "finance", 
    "freedom", "history", "journal", "meaning",

    #8 letter words
    "absolute", "academic", "accurate", "activity", "addition", "advisory", "advocate", "aircraft", "analysis", "apparent", "approval", 
    "audience", "average", "bulletin", "calendar", "campaign", "category", "chemical", "creative", "database", "decision", "designer", 
    "document", "economic", "employee", "evaluate", "evidence", "feature", "function", "guidance",


    #9 letter words
    "acquiesce", "adjacency", "adjustive", "amazement", "bamboozle", "benchmark", "blackball", "blockhead", "customize", "economize", 
    "effluvium", "enjoyable", "excavator", "exquisite", "fizziness", "glamorize", "harmonize", "humanizer", "immovable", "juxtapose", 
    "optimize", "recognize", "symbolize", "vaccinate", "vandalize", "visualize", "weaponize", "workplace", "xylophone", "zestfully"
    ]

hardlist = [
    #10 Letter Words
    'alchemized', 'amberjacks', 'aquaphobia', 'abandoning', 'abdication', 'aberration','abhorrence', 'abnegation', 'abnormally', 'background',
    'calculable', 'deadlocked', 'earthquake', 'fabricated', 'generously', 'headboards', 'ichthyoses', 'idealizing', 'jackhammer', 'kickboxing',
    'laboratory', 'marginally', 'nativities', 'obligatory', 'quadrupeds', 'racetracks', 'saccharide', 'tabulation', 'unoxidized', 'zoolatries',

    #11 Letter Words
    'abandonment', 'abbreviator', 'acknowledgement', 'acquisition', 'acupuncture', 'babyishness', 'backbencher', 'backscatter', 'battlefield',
    'beachcomber', 'calligraphy', 'candlelight', 'creationism', 'credibility', 'cryosurgery', 'declaration', 'denigration', 'documentary',
    'domesticate', 'doxorubicin', 'eccentrical', 'elaboration', 'electricity', 'elimination', 'emotionless', 'fabrication', 'featherhead',
    'fingerprint', 'formulation', 'germaphobia'



    #12 Letter Words
    'abbreviation', 'acceleration', 'accommodator', 'acknowledgment', 'adjudication', 'administration', 'agriculture', 'alphabetical', 'alternative',
    'application', 'appreciation', 'association', 'calculation', 'celebration', 'characterization', 'civilization', 'collaboration', 'communication',
    'concentration', 'configuration', 'conservation', 'consideration', 'consolidation', 'contemplation', 'coordination', 'corporation', 'declaration',
    'dedication', 'demonstration'
    ]

impossiblelist = [
    #13 letters
    'pneumonoultramicroscopicsilicovolcanoconiosis','hippopotomonstrosesquippedaliophobia','osteosarchaematosplanchnochondroneuromuelous',
    'osseocarnisanguineoviscericartilaginonervomedullary','pseudopseudohypoparathyroidism','floccinaucinihilipilification',
    'antidisestablishmentarianism','supercalifragilisticexpialidocious','incomprehensibilities','honorificabilitudinitatibus'
    ]

correct_letters = []
wrong_letter = []
lives = 0
score = 0
highscore1 = 0
highscore2 = 0
highscore3 = 0
highscore4 = 0

import random

while True:
    print(f"\n====================\n\nGamemodes:\n1. Classic\n2. Survival\n")
    gamemode = int(input("Select a Number: "))

#----------------------------------------------------------CLASSIC GAME MODE----------------------------------------------------------------------#
    if gamemode == 1:
        print("\n====================\n\nDifficulty list:")
        print("1. Easy 3-5 letter words, 8 lives")
        print("2. normal 6-9 letter words, 6 lives") 
        print("3. Hard 10-12 letter words, 4 lives")
        print("4. Impossible 13+ letter words, 2 lives")
        difficulty = int(input("\nSelect a Number: "))

        #EASY DIFFICULTY
        if difficulty == 1:
            word_answer = random.choice(easylist)
            lives += 8

        #NORMAL DIFFICULTY
        elif difficulty == 2:
            word_answer = random.choice(normallist)
            lives += 6

        #HARD DIFFICULTY
        elif difficulty == 3:
            word_answer = random.choice(hardlist)
            lives += 4

        #IMPOSSIBLE DIFFICULTY
        elif difficulty == 4:
            word_answer = random.choice(impossiblelist)
            lives += 2

        else:
                print("Invalid Difficulty.")
                break

        print(f"\n====================\nGAME START!\nYour Current life: {lives}")
        while True:
            print(word_answer)
            print(f"Letters in the word: {len(word_answer)}")
            attempt = str.lower(input("\nWhat will be your answer?: "))

            #WORD LENGTH CHECKER
            if len(attempt) != len(word_answer):  
                print(f"Word length not meet")
                continue
            
            elif len(attempt) == len(word_answer):

                #WRONG ANSWER
                if attempt != word_answer:
                    lives -= 1
                    print(f'"{attempt.upper()}" is a wrong word!\n\n====================')

                    #CORRECT LETTERS
                    for letter in attempt:
                        if letter in word_answer:
                            if letter not in correct_letters:
                                correct_letters.append(letter)
                            
                        #WRONG LETTERS
                        else:
                            if letter not in wrong_letter:
                                wrong_letter.append(letter)

                    #AFTER ANSWER REVIEWS
                    print(f'\nLife Points: {lives}\nCorrect Letters: {correct_letters}\nWrong Letters: {wrong_letter}')

                    #GAME OVER
                    if lives == 0:
                        print(f'\nGAME OVER!\nThe word is "{word_answer}"')
                        break

                #RIGHT ANSWER
                if attempt == word_answer:
                    print(f'\n====================\nCongratulations!\n"{attempt.upper()}" is the correct word\n====================\n')
                    correct_letters.clear()
                    wrong_letter.clear()
                    lives -= lives
                    break

#-----------------------------------------------------SURVIVAL MODE------------------------------------------------------------------------------#
    elif gamemode == 2:
        print("\n====================\n\nDifficulty list:\n1. Easy 3-5 letter words, 15 lives\n2. normal 6-9 letter words, 12 lives\n3. Hard 10-12 letter words, 9 lives\n4. Impossible 13+ letter words, 6 lives")
        difficulty = int(input("\nSelect a Number: "))

        #EASY DIFFICULTY SURVIVAL
        if difficulty == 1:
            lives += 15
            word_answer = random.choice(easylist)
            print(f"\n====================\n\nGAME START!\nLife Points: {lives}")

        #HARDLIST SURVIVAL
        elif difficulty == 2:
            lives += 12
            word_answer = random.choice(normallist)

        #HARD DIFFICULTY SURVIVAL
        elif difficulty == 3:
            word_answer = random.choice(hardlist)
            lives += 9

        #IMPOSSIBLE DIFFICULTY SURVIVAL
        elif difficulty == 4:
            word_answer = random.choice(impossiblelist)
            lives += 6
            print(f"\n====================\n\nGAME START!\nLife Points: {lives}")

        else:
                print("Invalid Difficulty.")
                break
        
        while True:
            print(f"Letters in the word: {len(word_answer)}\n")
            print(word_answer)
            attempt = str.lower(input("What will be your answer?: "))

            if len(attempt) != len(word_answer): 
                print("Word length not meet")   
                continue

            elif len(attempt) == len(word_answer):

                #WRONG ANSWER
                if attempt != word_answer:
                    lives -= 1
                    print(f'"{attempt.upper()}" is a wrong word!\n\n====================')

                    #CORRECT LETTERS
                    for letter in attempt:
                        if letter in word_answer:
                            if letter not in correct_letters:
                                correct_letters.append(letter)
                            
                        #WRONG LETTERS
                        else:
                            if letter not in wrong_letter:
                                wrong_letter.append(letter)

                    #AFTER ANSWER REVIEWS
                    print(f'\nLife Points: {lives}\nCorrect Letters: {correct_letters}\nWrong Letters: {wrong_letter}')

                    #GAME OVER
                    if lives <= 0:
                        print(f'\nGAME OVER!\nThe word is: "{word_answer}"')
                        break
                    
                #RIGHT ANSWER
                if attempt == word_answer:
                    correct_letters.clear()
                    wrong_letter.clear()
                    score += 1
                    lives += 3
                    print(f'\n"{attempt.upper()}" is correct\nYour Current life: {lives}\nscore: {score}')
                    
                    #EASY DIFFICULTY SURVIVAL
                    if difficulty == 1:
                        word_answer = random.choice(easylist)

                    #NORMAL DIFFICULTY SURVIVAL
                    if difficulty == 2:
                        word_answer = random.choice(normallist)

                    #HARD DIFFICULTY SURVIVAL
                    if difficulty == 3:
                        word_answer = random.choice(hardlist)

                    #IMPOSSIBLE DIFFICULTY SURVIVAL
                    if difficulty == 4:
                        word_answer = random.choice(impossiblelist)
                    
    
        #GAME OVER
        #EASY DIFFICULTY SURVIVAL
        if difficulty == 1:
            if score > highscore1:
                highscore1 = score
            print(f"Score: {score}\nHighest Score For Easy Difficulty: {highscore1}")
            score -= score

        #NORMAL DIFFICULTY SURVIVAL
        if difficulty == 2:
            if score > highscore2:
                highscore2 = score
            print(f"Score: {score}\nHighest Score For Normal Difficulty: {highscore2}")
            score -= score
        
        #HARD DIFFICULTY SURVIVAL
        if difficulty == 3:
            if score > highscore3:
                highscore3 = score
            print(f"Score: {score}\nHighest Score For Hard Difficulty: {highscore3}")
            score -= score

        #IMPOSSIBLE DIFFICULTY SURVIVAL
        if difficulty == 4:
            if score > highscore4:
                highscore4 = score
            print(f"Score: {score}\nHighest Score For Impossible Difficulty: {highscore4}")
            score -= score
    
    else:
        print("Invalid Input")
        continue
    
    #PLAY AGAIN
    play_again = int(input("\nPlay Again?:\n1. Yes\n2. No\n\nSelect a Number: "))
                    
    if play_again == 1:
        continue

    elif play_again == 2:
        break
