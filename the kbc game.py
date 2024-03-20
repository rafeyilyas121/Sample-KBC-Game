print('.......welcome to the KBC game......')
print('''rule.....
1.we will be asked 5 questions. 
2.You have to select your answer from the 4 options provided. 
3. For every correct answer you will be awarded with 1000 Rs. 
4. In case of wrong answer, you will be penalized by 500 Rs.''')

you_win_amount = 0
correct_ans = 0
print()
print("question 1.where is the capital of india?")
print('''
1.mumbai.
2.delhi.
3.lucknow.
4.bareilly.''')
ans = input('please enter your answer:')
if ans == '2':
    print("Congratulations! That's the correct answer.")
    you_win_amount = you_win_amount+1000
    print()
    print("question 2.who is the first prime minister of india?")
    print('''
    1.nehru g.
    2.gandhi g.
    3.patel g.
    4.khan g.''')
    ans = input('please enter your answer:')
    if ans == '1':
        print("Congratulations! That's the correct answer.")
        you_win_amount = you_win_amount + 1000
        print()
        print("question 3.what is the national animal of india?")
        print('''
        1.lion.
        2.horse.
        3.tiger.
        4.cheetah.''')
        ans = input('please enter your answer:')
        if ans == '3':
            print("Congratulations! That's the correct answer.")
            you_win_amount = you_win_amount + 1000
            print()
            print("question 4.where is the taj mahal?")
            print('''
            1.mumbai.
            2.delhi.
            3.lucknow.
            4.agra.''')
            ans = input('please enter your answer:')
            if ans == '4':
                print("Congratulations! That's the correct answer.")
                you_win_amount = you_win_amount + 1000
                print()
                print("question 1.where is the red fort?")
                print('''
                1.mumbai.
                2.delhi.
                3.lucknow.
                4.bareilly.''')
                ans = input('please enter your answer:')
                if ans == '2':
                    print("Congratulations! That's the correct answer.")
                    you_win_amount = you_win_amount + 1000
                    print()
                else:
                    print("That's the incorrect answer")
                    you_win_amount = you_win_amount - 500
            else:
                print("That's the incorrect answer")
                you_win_amount = you_win_amount - 500
        else:
            print("That's the incorrect answer")
            you_win_amount = you_win_amount - 500
    else:
        print("That's the incorrect answer")
        you_win_amount = you_win_amount - 500
else:
    print("That's the incorrect answer")
    you_win_amount = you_win_amount - 500
print()
print(f'your wining amount{you_win_amount}')
print('thank you........')
