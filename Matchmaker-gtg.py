# Grant Gallagher
# Matchmaker

# Constants

INTRODUCTION = '''
<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3

                  Matchmaker
          Find the Perfect One for You
              ProgrammersOnly.com

<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3

This foolproof program will determine your
exact compatibility with another user. To 
have the program function correctly please
    ONLY USE INTEGERS LISTED BELOW!

<-Strongly-----------Meh----------Strongly-->
    1        2        3        4        5
<-Disagree-------Indifferenct--------Agree-->

IF YOU THINK THERE IS A BUG IN THE PROGRAMMING
      IT IS SIMPLY A USER ERROR

<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
'''

QUESTION = [
    'Camping is a fun way to travel',
    'Peanut Butter is the amazing',
    'Hiking is miserable',
    'Dogs > cats',
    'Oatmeal Raisin Cookies > Chocolate Chip'
    ]

DESIRED_RESPONSE = [
    5,
    5,
    2,
    4,
    4
]

WEIGHT = [
    3,
    1,
    2,
    3,
    1
]

MAX_SCORE = 5 * len(QUESTION) + 25

# Execution Starts here

print(INTRODUCTION)

response = []
compatibility = []

# Ask Questions
for i in range(len(QUESTION)):
    UserResponse = int(input(QUESTION[i])) 

    if 0 < UserResponse < 6:
        response.append(UserResponse)

        questionCompatibility = ((5 * WEIGHT[i]) - ((abs(UserResponse - DESIRED_RESPONSE[i]) * WEIGHT[i] )))
        compatibility.append(questionCompatibility)

        print('QUESTION %d compatibility: %d \n' % (i+1, questionCompatibility))

        
        
    else:
        
        print('''
        PLEASE RESTART THIS MATCHMAKER AND ONLY INPUT NUMBER 1,2,3,4,5
        FOR ACCURATE CALCULATION
         THANK YOU.
        ''')
        break
        

FinalCompatibility = 0
for c in compatibility:
    FinalCompatibility += c

FinalCompatibility *= 100 / MAX_SCORE

print('Final Compatibility: %d\n' % (FinalCompatibility))

if FinalCompatibility==100:
    print('I’m on my way to get the ring!')

if 100>FinalCompatibility>=95:
    print('Is your name Google?\n ...Because you have everything I’m searching for, and I’m feeling lucky.')

if 95>FinalCompatibility>=85:
    print('Is your mame Microsoft?\n ...Because you could crash at my place')

if 85>FinalCompatibility>=75:
    print('Hey...\n I think we’d make good friends')

if 75>FinalCompatibility:
    print('Is your name Bing?\n ...Because I never plan on spending time with you.')