import gc
import time

from microbit import display, Image, pin_logo, button_a, button_b
from music import play, POWER_UP
from speech import say

# Generic talking educational database
generic_ted = {
                'your name': 'My name is Mr. George.',
                'food': 'I like pizza.',
              }

# Generic talking educational fill in the blank quiz database
generic_teq_f = {
                    'What is our bot\'s name?': 'Mr. George',
                    'What is Mr. George\'s favorite food?': 'pizza',
                }

# Generic talking educational multiple choice quiz database
generic_teq_m = {
                    'What is our bot\'s name?':
                    [
                        'Mr. George', 
                        'Ms. Henry', 
                        'Mr. Atencio', 
                        0
                    ],
                    'What is Mr. George\'s favorite food?':
                    [
                        'chocolate', 
                        'nachos', 
                        'pizza', 
                        2
                    ]
                }

# Customize bot speaking speed
SPEED = 95


def bot(ted, question):
    """
    Function to handle bot
    
    Params:
        ted: dict
        question: str
    """
    # Init LED happy image 
    display.show(Image.HAPPY)
    # This is an advanced topic as well however this little function
    # cleans out the unnecessary global objects or variables on what
    # we call the heap area in memory
    gc.collect()
    # Init response object
    response = '' 
    # We want to make sure that our dictionary database can 
    # find all values even if you use a capital letter
    # so we convert everything to lowercase 
    question = question.lower()
    # If you type something other than an empty string that means 
    # question has a value so the rest of the code will continue
    # on
    if question:
        # This is a bit complicated do not worry about this for now
        # all this is doing is looking through our dictionary database
        # and seeing if our input value has the word or words which
        # match an entry in the dictionary database and if it does
        # put the value in the _response object
        response = [val for key, val in ted.items() if key in question]
        gc.collect()
        # If our bot got a response from us then make sure
        # we trigger the speaking or suprised image so our bot
        # can open its mouth to talk and then have our bot
        # talk to us in our REPL and by hearing it speak as well
        # and if the user types in a trigger work that is not 
        # recognized then provide a custom default response
        if response:
            display.show(Image.SURPRISED)
            print('BOT: {0}'.format(response[0]))
            say(str(response[0]), speed=SPEED)
            display.show(Image.HAPPY)
        else:
            display.show(Image.SURPRISED)
            print('BOT: That is not something I am familiar with.')
            say('That is not something I am familiar with.', speed=SPEED)
            display.show(Image.HAPPY)      
    gc.collect()
        
        
def quiz_f(teq):
    """
    Function to fill in the blank quiz
    
    Params:
        teq: dict
    """
    # Init LED happy image 
    display.show(Image.HAPPY)
    # This is an advanced topic as well however this little function
    # cleans out the unnecessary global objects or variables on what
    # we call the heap area in memory
    gc.collect()
    # Init score object
    score = 0
    # Here we iterate through our quiz database
    for key in teq:
        print(key)
        say(str(key), speed=SPEED)
        response = input('ANSWER: ')
        response = response.lower() 
        correct_answer = teq[key].lower()
        if response == correct_answer:
            display.show(Image.SURPRISED)
            print('CORRECT!')
            say('CORRECT!', speed=SPEED)
            display.show(Image.HAPPY)
            score += 1
        else:
            display.show(Image.SURPRISED)
            print('The correct answer is {0}.'.format(teq[key]))
            say('The correct answer is', speed=SPEED)
            say(str(teq[key]), speed=SPEED)
            display.show(Image.HAPPY)
        time.sleep(1)
        gc.collect()
    # Here we reply to the student their score
    display.show(Image.SURPRISED)
    print('You got {0} out of {1} correct!'.format(score, len(teq)))
    say('You got', speed=SPEED)
    say(str(score), speed=SPEED)
    say('out of', speed=SPEED)
    say(str(len(teq)), speed=SPEED)
    say('correct!', speed=SPEED)
    # If student got a perfect score respond appropriately
    # or provide an encouring message to retry the quiz
    if score == len(teq):
        print('You got a perfect score!')
        say('You got a perfect score!', speed=SPEED)
        print('Well done!')
        say('Well done!, ', speed=SPEED)
        print('I am so proud of you!')
        say('I am so proud of you!', speed=SPEED)
        play(POWER_UP)
    else:
        print('You are doing a great job!')
        say('You are doing a great job!', speed=SPEED)
        print('I would LOVE for you to try again!')
        say('I would LOVE for you to try again!', speed=SPEED) 
    # Display happy response at the end of the quiz
    display.show(Image.HAPPY)
    gc.collect()
    
    
def quiz_m(teq):
    """
    Function to handle multiple choice quiz
    
    Params:
        teq: dict
    """
    # Init LED happy image 
    display.show(Image.HAPPY)
    # This is an advanced topic as well however this little function
    # cleans out the unnecessary global objects or variables on what
    # we call the heap area in memory
    gc.collect()
    # Init score object
    score = 0
    # Here we iterate through our quiz database with multiple
    # choice items
    for key in teq:
        display.show(Image.SURPRISED)
        print(key)
        say(str(key), speed=SPEED)
        display.show(Image.HAPPY)
        time.sleep(1)
        display.show(Image.SURPRISED)
        print('Press A for {0}.'.format(teq[key][0]))
        say('Press Ayyy for', speed=SPEED)
        say(str(teq[key][0]), speed=SPEED)
        display.show(Image.HAPPY)
        time.sleep(1)
        display.show(Image.SURPRISED)
        print('Touch the logo for {0}.'.format(teq[key][1]))
        say('Toch the logo for', speed=SPEED)
        say(str(teq[key][1]), speed=SPEED)
        display.show(Image.HAPPY)
        time.sleep(1)
        display.show(Image.SURPRISED)
        print('Press B for {0}.'.format(teq[key][2]))
        say('Press B for', speed=SPEED)
        say(str(teq[key][2]), speed=SPEED)
        display.show(Image.HAPPY)
        while True:
            if button_a.is_pressed():
                response = 0
                break
            elif pin_logo.is_touched():
                response = 1
                break
            elif button_b.is_pressed():
                response = 2
                break
            else:
                pass     
        correct_answer = teq[key][3]
        display.show(Image.SURPRISED)
        print('You selected {0}.'.format(teq[key][response]))
        say('You selected', speed=SPEED)
        say(str(teq[key][response]), speed=SPEED)
        display.show(Image.HAPPY)
        time.sleep(1)
        if response == correct_answer:
            display.show(Image.SURPRISED)
            print('CORRECT!')
            say('CORRECT!', speed=SPEED)
            display.show(Image.HAPPY)
            score += 1
        else:
            display.show(Image.SURPRISED)
            print('The correct answer is {0}.'.format(teq[key][correct_answer]))
            say('The correct answer is', speed=SPEED)
            say(str(teq[key][correct_answer]), speed=SPEED)
            display.show(Image.HAPPY)   
        time.sleep(1)
        gc.collect() 
    # Here we reply to the student their score
    display.show(Image.SURPRISED)
    print('You got {0} out of {1} correct!'.format(score, len(teq)))
    say('You got', speed=SPEED)
    say(str(score), speed=SPEED)
    say('out of', speed=SPEED)
    say(str(len(teq)), speed=SPEED)
    say('correct!', speed=SPEED)
    display.show(Image.HAPPY)
    time.sleep(1)
    # If student got a perfect score respond appropriately
    # or provide an encouring message to retry the quiz
    display.show(Image.SURPRISED)
    if score == len(teq):
        print('You got a perfect score!')
        say('You got a perfect score!', speed=SPEED)
        print('Well done!')
        say('Well done!', speed=SPEED)
        print('I am so proud of you!')
        say('I am so proud of you!', speed=SPEED)
        play(POWER_UP)
    else:
        print('You are doing a great job!')
        say('You are doing a great job!', speed=SPEED)
        print('I would LOVE for you to try again!')
        say('I would LOVE for you to try again!', speed=SPEED)
    # Display happy response at the end of the quiz
    display.show(Image.HAPPY)
    time.sleep(1)
    gc.collect()
