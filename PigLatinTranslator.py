done = True
pyg = 'ay'

while done:
        original = input('Enter a word:')

        if len(original) > 0 and original.isalpha():  
                word = original.lower()    #making sure they are all letters
                first = word[0]            #and checking if there are any letters
                if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
                        new_word = word + pyg
                        print (new_word)
                else:
                        last = len(word)
                        new_word = word[1:last] + first + pyg
                        print (new_word)
        else:
                print ('Enter a real word please.')


        again = input('''Do you want to translate another word?
                  Type Yes or No:''')
        if again == 'Yes' or again == 'yes':
                done = True
        else:
                done = False
        
