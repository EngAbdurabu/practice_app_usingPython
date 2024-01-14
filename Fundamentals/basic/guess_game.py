my_number = 7
guess_num = int(input('Enter the guess number : '))
    
if guess_num == my_number:
    print("you are win 😍😊")
elif guess_num == my_number + 1 or  guess_num == my_number - 1:
    print('you are close near from the correct answer ')
elif guess_num == my_number + 2 or guess_num == my_number - 2:
    print('you are near from the correct answer but not close think about that')
        # hind = input('if you want hind print "help hind" : ')
        # if hind == 'help hind':
        #     print('you can go down or up by two step ')
            

        # else:
        #     print('you have error in word of hind 5')
else:
    print('you are loss 😟☹️😮')
