import random
import sys

bye=('''
 _                
| |               
| |__  _   _  ___ 
| '_ \| | | |/ _ \

| |_) | |_| |  __/
|_.__/ \__, |\___|
        __/ |     
       |___/     ''')

swgg=('''
   _____             _             __          __   _                   _____             
  / ____|           | |            \ \        / /  | |                 / ____|            
 | (___  _ __   __ _| | _____       \ \  /\  / /_ _| |_ ___ _ __      | |  __ _   _ _ __  
  \___ \| '_ \ / _` | |/ / _ \       \ \/  \/ / _` | __/ _ \ '__|     | | |_ | | | | '_ \ 
  ____) | | | | (_| |   <  __/  _     \  /\  / (_| | ||  __/ |     _  | |__| | |_| | | | |
 |_____/|_| |_|\__,_|_|\_\___| ( )     \/  \/ \__,_|\__\___|_|    ( )  \_____|\__,_|_| |_|
                               |/                                 |/                      
                                                                                          ''')

hngg = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

s=('''
--..,_                        _,.--.
       `'.'.                .'`__ o  `;__.      
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'` ''')

g=('''
  +-'~`---------------------------------/\--
 ||"""""""""""""""""""""""""""""""" \\\\\\  \/~)
 ||                                  \\\\\\  \/_
  |~~~~~~~~-________________-_________________\ ~--_
  !---------|_________       ------~~~~~(--   )--~~
                      \ /~~~~\~~\   )--- \_ /(
                       ||     |  | \   ()   \\
                       \\____/_ / ()\        \\
                        `~~~~~~~~~-. \        \\
                                    \ \  <($)> \\
                                     \ \        \\
                                      \ \        \\
                                       \ \        \\
                                        \ \  ()    \|
                                        _\_\__====~~~ ''')

w=(''' 
  ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(
`-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  ` 
   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(
`-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `
   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(
`-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `''')

win=(''' 
     .-""""""-.
   .'          '.
  /   O      O   \
 :                :
 |                |   
 : ',          ,' :
  \  '-......-'  /
   '.          .'
     '-......-'
''')

los=('''
     .-""""""-.
   .'          '.
  /   O      O   \
 :           `    :
 |                |   
 :    .------.    :
  \  '        '  /
   '.          .'
     '-......-'
 ''')

tie=('''
     .-""""""-.
   .'          '.
  /   -=-    O   \
 :                :
 |                |  
 :             ,' :
  \    ......-'  /
   '.          .'
     '-......-'
''')

bye=('''
 _                
| |               
| |__  _   _  ___ 
| '_ \| | | |/ _ \

| |_) | |_| |  __/
|_.__/ \__, |\___|
        __/ |     
       |___/     ''')



while True:

 def choose():
         print('\nPress 1 to play snake water gun')
         print('\nPress 2 to play hang man ')
         print('\nPress \'e\' to exit')
         n=input('\nEnter your choice: ')
         if n=='1':
            print(swgg)
            swg()
         elif n=='2':
           print(hngg)
           hng()
         elif n=='e' or n=='E':
            print(bye)
            sys.exit()
  

 def swg():
     a=[]
     mood=input('\nPress \'y\' to start ; Press any key to exit:\n')
     a.append(mood)
     
     if 'Y' in a or 'y' in a:

        while True:
        
             print('\nCHOOSE ANY ONE:\n ')

             you=input("snake(s), water(w), gun(g)....Press 'e' to exit:\n")


             if you=='s' or you=='S':
                   print('--> You choose snake')
                   print(s)

             elif you=='w' or you=='W':
                     print('--> You choose water')
                     print(w)

             elif you=='g' or you=='G':
                     print('--> You choose gun')
                     print(g)
                     
             elif you=='e' or you=='E':
                print(bye)
                break

             else:
                 print('\nINVALID INPUT\n')
                 continue


             print('\nCOMPUTER TURN:')

             comp=random.randint(1,3)
 
             if comp==1:
                     print('--> Computer choose snake')
                     print(s)
             elif comp==2:
                     print('--> Computer choose water')
                     print(w)
             elif comp==3:
                     print('--> Computer choose gun')
                     print(g)


             print('\nRESULT: ',end='')
     
             if you=='s' and comp==1:
                       print('\n--> Tie !\n')
                       print(tie)
             elif you=='w' and comp==2:
                       print('\n--> Tie !\n')
                       print(tie)
             elif you=='g' and comp==3:
                       print('\n--> Tie !\n')
                       print(tie)
             elif you=='s' and comp==2:
                       print ('\n--> You win !\n')
                       print(win) 
             elif you=='s' and comp==3:
                       print ('\n--> You lost !\n')
                       print(los)
             elif you=='w' and comp==1:
                       print ('\n--> You lost !\n')
                       print(los)
             elif you=='w' and comp==3:
                       print ('\n--> You win !\n')
                       print(win)
             elif you=='g' and comp==1:
                       print ('\n--> You win !\n')
                       print(win)
             elif you=='g' and comp==2:
                       print ('\n--> You lost !\n')
                       print(los)
             elif you=='S' and comp==1:
                       print('\n--> Tie !\n')
                       print(tie)
             elif you=='W' and comp==2:
                       print('\n--> Tie !\n')
                       print(tie)
             elif you=='G' and comp==3:
                       print('\n--> Tie !\n')
                       print(tie)
             elif you=='S' and comp==2:
                       print ('\n--> You win !\n')
                       print(win)
             elif you=='S' and comp==3:
                       print ('\n--> You lost !\n')
                       print(los)
             elif you=='W' and comp==1:
                       print ('\n--> You lost !\n')
                       print(los)
             elif you=='W' and comp==3:
                       print ('\n--> You win !\n')
                       print(win)
             elif you=='G' and comp==1:
                       print ('\n--> You win !\n')
                       print(win)
             elif you=='G' and comp==2:
                     print ('\n--> You lost !\n')
                     print(los)
     else:
         print(bye)      


 def hng(): 

   word_list = ['abruptly','absurd','abyss','affix','askew','avenue','awkward','axiom','azure','fuchsia','funny',
  'bagpipes','bandwagon','banjo','bayou','beekeeper''bikini','blitz','blizzard','boggle','bookworm','jazziest'
  'boxcar','boxful','buckaroo','buffalo','buffoon','buxom','buzzard','buzzing','buzzwords','dwarves','jazzy',
  'caliph','cobweb','cockiness','croquet','crypt','curacao','cycle','daiquiri','dirndl','disavow','dizzying','duplex',
  'embezzle','equip','espionage','euouae','exodus','stronghold','stymied','subway','swivel','syndrome',
  'faking','fishhook','fixable','fjord','flapjack','flopping','fluffiness','flyby','foxglove','frazzled','frizzled',
  'gabby','galaxy','galvanize','gazebo','giaour','gizmo','glowworm','glyph','gnarly','gnostic','gossip','grogginess',
  'haiku','haphazard','hyphen','iatrogenic','icebox','injury','ivory','ivy','jackpot','jaundice','jawbreaker','jaywalk',
  'jelly','jigsaw','jinx','jiujitsu','jockey','jogging','joking','jovial','joyful','juicy','jukebox',
  'kilobyte','kiosk','kitsch','kiwifruit','klutz','knapsack','larynx','lengths','lucky','luxury','lymph',
  'marquis','matrix','megahertz','microwave','mnemonic','mystify','naphtha','nightclub','nowadays',
  'numbskull','nymph','onyx','ovary','oxidize','oxygen','pajama','peekaboo','phlegm','pixel','pizazz',
  'pneumonia','polka','pshaw','psyche','puppy','puzzling','quartz','queue','quips','quixotic','quiz',
  'quizzes','quorum','razzmatazz','rhubarb','rhythm','rickshaw','jumbo','kayak','kazoo','keyhole','khaki',
  'schnapps','scratch','shiv','snazzy','sphinx','spritz','squawk','staff','strength','strengths','stretch',
  'thriftless','thumbscrew','topaz','transcript','transgress','transplant','triphthong','twelfth','twelfths',
  'unknown','unworthy','unzip','uptown','vaporize','vixen','vodka','voodoo','vortex','voyeurism',
  'walkway','waltz','wave','wavy','waxy','wellspring','wheezy','whiskey','whizzing',
  'whomever','wimpy','witchcraft','wizard','woozy','wristwatch','wyvern','xylophone','yachtsman',
  'yippee','yoked','youthful','yummy','zephyr','zigzag','zigzagging','zilch','zipper','zodiac','zombie',]

   stages = ['''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========
  ''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========
  ''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========
  ''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========
  ''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========
 ''', '''
    +---+
    |   |
        |
        |
        |
        |
  =========
  ''']

   chosen_word = random.choice(word_list)
   word_length = len(chosen_word)

   end_of_game = False
   lives = 6

   display = []
   for i in range(word_length):
     display += "_"
   while True:
    user=input('\nPress \'y\' to start: (blank to  exit)\n')
    if user=='y' or user=='Y':
  
     while not end_of_game:
     
       guess = input("\nGuess a letter: ").lower()

       if guess in display:
         print(f"You have already guessed {guess}")

       for position in range(word_length):
         letter = chosen_word[position]

         if letter == guess:
             display[position] = letter

       if guess not in chosen_word:

         print("You have guessed the wrong letter.")
         lives -= 1
         if lives == 0:
             end_of_game = True
             print("You lose.")

       print(f"{' '.join(display)}")
       
       if "_" not in display:
         end_of_game = True
         print("You win.")

       print(stages[lives])
     print(f'\nThe choosen word was {chosen_word}')    
    elif user=='':
     print(bye)
     break
    
 choose()
 continue
