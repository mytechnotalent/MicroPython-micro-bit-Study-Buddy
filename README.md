![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/MicroPython-micro-bit%20Study%20Buddy.png?raw=true)

# MicroPython-micro-bit
# Study Buddy
The micro:bit Study Buddy is a micro:bit Electronic Educational Engagement Tool designed to help students learn a new classroom subject with the assistance of a micro:bit TED (Talking Educational Database) and a micro:bit TEQ (Talking Educational Quiz).

## Mission Statement
Over the next 10 years we are going to see a fundamental transformation of technology in a way never before seen in history.  

Future careers will look very different than they do today to which literally every opportunity will include the usage of a microcontroller in combination with an automation engine and the skills necessary to adapt to this new paradigm.

With this landscape directly over the horizon we need to empower our Educators, the single more important group of leaders in the twenty-first century, with the tools necessary to inspire and engage the next generation of makers in an exciting new way.

Today is born the concept of a micro:bit Electronic Educational Engagement Tool to connect with students in a very emotional and inspiring way which will help solidify classroom subject curriculum in a significantly enhanced time frame in addition to preparing these future leaders with the software engineering fundamentals necessary to compete in tomorrow's economy.

The micro:bit Electronic Educational Engagement Tool is comprised of a micro:bit TED (Talking Educational Database) and a micro:bit TEQ (Talking Educational Quiz) to enhance Educators world-wide with the curriculum integration to take their students to the next level.

## Project Hypothetical
YOU are a History and Biology Educator and are about to teach your students the 50 state capitals of the US in your history curriculum in addition to parts of a cell in your biology curriculum.  YOU now have a grant and with that grant a micro:bit V2 for each student and YOU get to take advantage of the micro:bit EEET (Electronic Educational Engagement Tool) to integrate into your curriculum!

YOU follow the steps below and very easily see how YOU can integrate this technology in a way NEVER done in history!  YOU will be able to BRING TO LIFE a micro:bit TED (Talking Educational Database) or talking chat bot that can help the student learn the 50 state capitals and the parts of a cell as it makes facial animations and literally TALKS to the student!

The student will then be able to work with the micro:bit TED on their own to help strengthen their curriculum concept development and then take the micro:bit TEQ to help them prepare for the subject exam or test.  They can engage the TED and TEQ on demand which will build their confidence and comfort level of the subject matter in a revolutionary new way!

We are going to utilize the micro:bit Python V2 web editor to design our project with detailed steps to help any educator regardless of their background or comfort level to implement this feature.

## Schematic
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/schematic.png?raw=true)

## Parts
[micro:bit](COMING NOVEMBER 2020)

## STEP 1: Navigate To The FREE micro:bit Python Web Editor
[micro:bit Python Web Editor](https://python.microbit.org/v/beta)<br><br>
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%201.png?raw=true)

## STEP 2: Plug micro:bit V2 Into Computer
***PLUG IN USB CABLE TO COMPUTER AND DEVICE***

## STEP 3: Click CONNECT
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%203.png?raw=true)

## STEP 4: Click "BBC micro:bit CMSIS-DAP" & CONNECT
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%204.png?raw=true)

## STEP 5: Highlight Sample Code - Select All
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%205.png?raw=true)

## STEP 6: Click Backspace On Keyboard To Delete Sample Code
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%206.png?raw=true)

## STEP 7: Copy Study Buddy Python Code Template Into Python Web Editor
```python
import gc
import time

from microbit import display, Image, pin_logo, button_a, button_b
from music import play, POWER_UP
from speech import say


def generic_bot(question):
    """Bot function

    Parameters
    ----------
    question : str
        Question to parse for trigger words

    Returns
    -------
    None
    """
    # Our Python dictionary which is a database
    # and here is where we can type in new key/value
    # pairs or in our case trigger word or words and
    # then a response
    db = {
            'your name': 'My name is Mr. George.',
            'food': 'I like pizza.',
         }

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
        response = [val for key, val in db.items() if key in question]
        
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
            say(str(response[0]))
            display.show(Image.HAPPY)
        else:
            display.show(Image.SURPRISED)
            print('BOT: That is not a state or state capital I am familiar with.')
            say('That is not a state or state capital I am familiar with.')
            display.show(Image.HAPPY)
            
            
def generic_quiz_f():
    """Fill in the blank quiz function

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    # Our Python dictionary which is a database
    # and here is where we can type in new key/value
    # pairs or in our case trigger word or words and
    # then a response
    db = {
            'What is our bot\'s name?': 'Mr. George',
            'What is Mr. George\'s favorite food?': 'pizza',
         }

    # Init LED happy image 
    display.show(Image.HAPPY)

    # This is an advanced topic as well however this little function
    # cleans out the unnecessary global objects or variables on what
    # we call the heap area in memory
    gc.collect()
    
    # Init score object
    score = 0
    
    # Here we iterate through our quiz database
    for key in db:
        print(key)
        say(str(key))
        response = input('ANSWER: ')
        response = response.lower()
        correct_answer = db[key].lower()
        print(response)
        print(correct_answer)
        if response == correct_answer:
            display.show(Image.SURPRISED)
            print('CORRECT!')
            say('CORRECT!')
            display.show(Image.HAPPY)
            score += 1
        else:
            display.show(Image.SURPRISED)
            print('The correct answer is {0}.'.format(db[key]))
            say('The correct answer is')
            say(str(db[key]))
            display.show(Image.HAPPY)
        gc.collect()
    
    # Here we reply to the student their score
    display.show(Image.SURPRISED)
    print('You got {0} out of {1} correct!'.format(score, len(db)))
    say('You got')
    say(str(score))
    say('out of')
    say(str(len(db)))
    say('correct!')
    
    # If student got a perfect score respond appropriately
    # or provide an encouring message to retry the quiz
    if score == len(db):
        print('You got a perfect score!')
        say('You got a perfect score!')
        print('Well done!')
        say('Well done!')
        print('I am so proud of you!')
        say('I am so proud of you!')
        play(POWER_UP)
    else:
        print('You are doing a great job!')
        say('You are doing a great job!')
        print('I would LOVE for you to try again!')
        say('I would LOVE for you to try again!')
        
    # Display happy response at the end of the quiz
    display.show(Image.HAPPY)
    
    
def generic_quiz_m():
    """Multiple choice quiz function

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    # Our Python dictionary which is a database
    # and here is where we can type in new key/value
    # pairs or in our case trigger word or words and
    # then a response
    db = {
            'What is our bot\'s name?': [
                                            'Mr. George', 
                                            'Ms. Henry', 
                                            'Mr. Atencio', 
                                            0
                                        ],
            'What is Mr. George\'s favorite food?': [
                                                        'chocolate', 
                                                        'nachos', 
                                                        'pizza', 
                                                        2
                                                    ]
         }

    # Init LED happy image 
    display.show(Image.HAPPY)

    # This is an advanced topic as well however this little function
    # cleans out the unnecessary global objects or variables on what
    # we call the heap area in memory
    gc.collect()
    
    # Init response object
    response = ''
    
    # Init score object
    score = 0
    
    # Here we iterate through our quiz database with multiple
    # choice items
    for key in db:
        display.show(Image.SURPRISED)
        print(key)
        say(str(key))
        print('Press A for {0}.'.format(db[key][0]))
        say('Press A for')
        say(str(db[key][0]))
        print('Touch the logo for {0}.'.format(db[key][1]))
        say('Touch the logo for')
        say(str(db[key][1]))
        print('Press B for {0}.'.format(db[key][2]))
        say('Press B for')
        say(str(db[key][2]))
        display.show(Image.HAPPY)
        while not button_a.is_pressed() and not pin_logo.is_touched() and not button_b.is_pressed():
            if button_a.is_pressed():
                response = 0
                break
            elif pin_logo.is_touched():
                response = 1
                break
            elif button_b.is_pressed():
                response = 2
                break
        correct_answer = db[key][3]
        if response == correct_answer:
            display.show(Image.SURPRISED)
            print('CORRECT!')
            say('CORRECT!')
            display.show(Image.HAPPY)
            score += 1
        else:
            display.show(Image.SURPRISED)
            print('The correct answer is {0}.'.format(db[key][correct_answer]))
            say('The correct answer is')
            say(str(db[key][correct_answer]))
            display.show(Image.HAPPY)
        gc.collect()
    
    # Here we reply to the student their score
    display.show(Image.SURPRISED)
    print('You got {0} out of {1} correct!'.format(score, len(db)))
    say('You got')
    say(str(score))
    say('out of')
    say(str(len(db)))
    say('correct!')
    
    # If student got a perfect score respond appropriately
    # or provide an encouring message to retry the quiz
    if score == len(db):
        print('You got a perfect score!')
        say('You got a perfect score!')
        print('Well done!')
        say('Well done!')
        print('I am so proud of you!')
        say('I am so proud of you!')
        play(POWER_UP)
    else:
        print('You are doing a great job!')
        say('You are doing a great job!')
        print('I would LOVE for you to try again!')
        say('I would LOVE for you to try again!')
        
    # Display happy response at the end of the quiz
    display.show(Image.HAPPY)
```
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%207.png?raw=true)

## STEP 8: Rename Script Name To sb_template
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%208.png?raw=true)


