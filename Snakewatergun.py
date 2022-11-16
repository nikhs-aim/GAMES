import random
        
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



def fun():
     a=[]
     mood=input('\nPress y if you wanna play; Press any key if you dont wanna play:\n')
     a.append(mood)

     if 'Y' in a or 'y' in a:

        while True:
        
             print('CHOOSE ANY ONE: ')

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
                 print('INVALID INPUT')
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
                       print('--> tie !\n')
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
fun()