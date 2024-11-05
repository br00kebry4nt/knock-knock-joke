#knock.py
name = input("What is your name?")
print(f'Well hello, {name}, do you want to hear a joke?')

response = input('Please enter Yes or No:').lower()
if response == 'yes':
    print('Knock knock!')
    resp0nse = input()
   
    if resp0nse.lower() == "who's there?":
        print('WOO!')
        r3sponse = input()
        
        if r3sponse.lower() == "woo who?":
            print("Glad you're excited, too!")
        else:
            print("You are so funny, you should have said, 'Woo who?'")
    else:
        print("You silly goose, you should have said, 'Who's there?'")

if response == 'no':
        print('You missed out on a good laugh.')
    