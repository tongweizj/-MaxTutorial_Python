colors = ['green', 'yellow', 'red']
alien_a_color = colors[1]
alien_b_color = colors[2]
play_record = 0

if alien_a_color == colors[1]:
    print('Yes, alien color is green, you get 5 points')
    play_record += 5
else:
    print('Sorry, alien color is not green, you get 10 points')
    play_record += 10
print(play_record)  

if alien_b_color == colors[0]:
    print('Yes, alien color is green')
    play_record += 5
elif alien_b_color == colors[1]:
    print('Yes, alien color is yellow, you get 10 points')
    play_record += 10
elif alien_b_color == colors[2]:
    print('Yes, alien color is red, you get 15 points')
    play_record += 15
print(play_record) 