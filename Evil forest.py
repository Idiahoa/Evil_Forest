print('''

                                      __,,,
                                 _.--'    /
                              .-'        /
                            .'          |
                          .'           /
                         /_____________|
                       /`~~~~~~~~~~~~~~/
                     /`               /
      ____,....----'/_________________|---....,___
,--""`             `~~~~~~~~~~~~~~~~~~`           `""--,
`'----------------.----,------------------------,-------'`
               _,'.--. \                         \
             .'  (o   ) \                        |
            c   , '--'  |                        /
           /    )'-.    \                       /
          |  .-;        \                       |
          \_/  |___,'    |                    .-'
         .---.___|_      |                   /
        (          `     |               .--'
         '.         __,-'\             .'
           `'-----'`      \        __.'
                      jgs  `-..--'`

''')
print("Welcome to The Evil Forest.")
name=input("What is your name my child?.\n")
print("       ")
print("Only those pure of heart may enter!")
print("To prove that you are favoured by the gods, you must make it to the other side.") 
print("                       ")
print(f'Beware {name} this will not be an easy task!')
print("MUHAAHAHHAHHAHA!!!")
print("**witch disappears**")

print("                     ")

print("The road ahead divides into two paths")
Direction=input("Decide your path!, 'left' or 'right'?\n").lower()
if Direction=='left':
   stage=input("Ahead is the Black sea, will you 'swim' or 'wait'?.\n").lower()
   print("     ")
   if stage=='wait':
    final=input("pick a door,'Red','Blue' or 'Yellow'?.\n").lower()
    if final=='yellow':
      print("YOU WIN!.")
      print('''
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
          jgs `"""""""`


''')
    elif final=='red':
      print("You no know say red na danger? Ogun don kee you.")
    else:
      print("Oshey Baba blue")
   else: 
    print("You think say na swimming pool be this?, Ọya don drown you!")
else:
  print(f"Struck by SANGO!, chai {name}! Na so you take die.")
