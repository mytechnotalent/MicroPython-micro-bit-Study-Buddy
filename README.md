![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/MicroPython-micro-bit%20Study%20Buddy.png?raw=true)

# MicroPython-micro-bit
# Study Buddy
The micro:bit Study Buddy is a micro:bit Electronic Educational Engagement Tool designed to help students learn a new classroom subject with the assistance of a micro:bit TED (Talking Educational Database) and a micro:bit TEQ (Talking Educational Quiz).

<br> 

## DEMO VIDEO - WATCH NOW [HERE](https://youtu.be/0OG5Vfdh5bM) ON YOUTUBE

<br>

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

We will begin with a Study Buddy template example to experiment with so that we can get familiar with the framework.

We will then create a fully-featured Study Buddy application which encompasses both the state capital curriculum and the parts of a cell curriculum demonstrating the multi-curriculum architecture of the micro:bit V2!

## Schematic
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/schematic.png?raw=true)

## Parts
[micro:bit](https://microbit.org/buy/?location=US&version=microbitV2)

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


def bot_proc(ted, question):
    """Bot proc function
    
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
        
        
def quiz_f_proc(teq):
    """Fill in the blank quiz proc function
    
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
    
    
def quiz_m_proc(teq):
    """Multiple choice quiz proc function
    
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
```

![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%207.png?raw=true)

## STEP 8: Rename Script Name To sb_template
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%208.png?raw=true)

## STEP 9: Click Save
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%209.png?raw=true)

## STEP 10: Click Download Python Script
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%2010.png?raw=true)

## STEP 11: Click Flash
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%2011.png?raw=true)

## STEP 12: Click Open Serial
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%2012.png?raw=true)

## STEP 13: Communicate With The micro:bit generic TED Bot & Take The Fill In The Blank Quiz, Multiple-Choice Quiz
```
>>> import main
>>> main.bot(generic_ted, 'What is your name?')
BOT: My name is Mr. George.
>>> main.bot(generic_ted, 'What is your favorite food?')
BOT: I like pizza.
>>> main.bot(generic_ted, 'What is your favorite song?')
BOT: That is not something I am familiar with.
>>>
>>> main.quiz_f(generic_teq_f)
What is our bot's name?
ANSWER: Mr. George
CORRECT!
What is Mr. George's favorite food?
ANSWER: pizza
CORRECT!
You got 2 out of 2 correct!
You got a perfect score!
Well done!
I am so proud of you!
>>>
>>> main.quiz_m(generic_teq_m)
What is our bot's name?
Press A for Mr. George.
Touch the logo for Ms. Henry.
Press B for Mr. Atencio.
You selected Ms. Henry.
The correct answer is Mr. George.
What is Mr. George's favorite food?
Press A for chocolate.
Touch the logo for nachos.
Press B for pizza.
You selected pizza.
CORRECT!
You got 1 out of 2 correct!
You are doing a great job!
I would LOVE for you to try again!
>>> 
```

## STEP 14: Rename Script Name To sb_sc
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%2014.png?raw=true)

## STEP 15: Populate Our State Capital Database
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%2015.png?raw=true)<br>
Click close serial and return to the Python Web Editor. Delete our `generic_ted` database and replace it with the following database.
```python
# State capital talking educational database
sc_ted = {
            'alabama': 'The capital of Alabama is Montgomery.',
            'montgomery': 'Montgomery is the capital of Alabama.',
            'alaska': 'The capital of Alaska is Juneau.',
            'juneau': 'Juneau is the capital of Alaska.',
            'arizona': 'The capital of Arizona is Phoenix.',
            'phoenix': 'Phoenix is the capital of Arizona.',
            'arkansas': 'The capital of Arkansas is Little Rock.',
            'little rock': 'Little Rock is the capital of Arkansas.',
            'california': 'The capital of California is Sacramento.',
            'sacramento': 'Sacramento is the capital of California.',
            'colorado': 'The capital of Colorado is Denver.',
            'denver': 'Denver is the capital of Colorado.',
            'connecticut': 'The capital of Connecticut is Hartford.',
            'hartford': 'Hartford is the capital of Connecticut.',
            'delaware': 'The capital of Delaware is Dover.',
            'dover': 'Dover is the capital of Delaware.',
            'florida': 'The capital of Florida is Tallahassee.',
            'tallahassee': 'Tallahassee is the capital of Florida.',
            'georgia': 'The capital of Georgia is Atlanta.',
            'atlanta': 'Atlanta is the capital of Georgia.',
            'hawaii': 'The capital of Hawaii is Honolulu.',
            'honolulu': 'Honolulu is the capital of Hawaii.',
            'idaho': 'The capital of Idaho is Boise.',
            'boise': 'Boise is the capital of Idaho.',
            'illinois': 'The capital of Illinois is Springfield.',
            'springfield': 'Springfield is the capital of Illinois.',
            'indiana': 'The capital of Indiana is Indianapolis.',
            'indianapolis': 'Indianapolis is the capital of Indiana.',
            'iowa': 'The capital of Iowa is Des Moines.',
            'des moines': 'Des Moines is the capital of Iowa.',
            'kansas': 'The capital of Kansas is Topeka.',
            'topeka': 'Topeka is the capital of Kansas.',
            'kentucky': 'The capital of Kentucky is Frankfort.',
            'frankfort': 'Frankfort is the capital of Kentucky.',
            'louisiana': 'The capital of Louisiana is Baton Rouge.',
            'baton rouge': 'Baton Rouge is the capital of Louisiana.',
            'maine': 'The capital of Maine is Augusta.',
            'augusta': 'Augusta is the capital of Maine.',
            'maryland': 'The capital of Maryland is Annapolis.',
            'annapolis': 'Annapolis is the capital of Maryland.',
            'massachusetts': 'The capital of Massachusetts is Boston.',
            'boston': 'Boston is the capital of Massachusetts.',
            'michigan': 'The capital of Michigan is Lansing.',
            'lansing': 'Lansing is the capital of Michigan.',
            'minnesota': 'The capital of Minnesota is Saint Paul.',
            'saint paul': 'Saint Paul is the capital of Minnesota.',
            'mississippi': 'The capital of Mississippi is Jackson.',
            'jackson': 'Jackson is the capital of Mississippi.',
            'missouri': 'The capital of Missouri is Jefferson City.',
            'jefferson city': 'Jefferson City is the capital of Missouri.',
            'montana': 'The capital of Montana is Helena.',
            'helena': 'Helena is the capital of Montana.',
            'nebraska': 'The capital of Nebraska is Lincoln.',
            'lincoln': 'Lincoln is the capital of Nebraska.',
            'nevada': 'The capital of Nevada is Carson City.',
            'carson city': 'Carson City is the capital of Nevada.',
            'new hampshire': 'The capital of New Hampshire is Concord.',
            'concord': 'Concord is the capital of New Hampshire.',
            'new jersey': 'The capital of New Jersey is Trenton.',
            'trenton': 'Trenton is the capital of New Jersey.',
            'new mexico': 'The capital of New Mexico is Santa Fe.',
            'santa fe': 'Santa Fe is the capital of New Mexico.',
            'new york': 'The capital of New York is Albany.',
            'albany': 'Albany is the capital of New York.',
            'north carolina': 'The capital of North Carolina is Raleigh.',
            'raleigh': 'Raleigh is the capital of North Carolina.',
            'north dakota': 'The capital of North Dakota is Bismarck.',
            'bismarck': 'Bismarck is the capital of North Dakota.',
            'ohio': 'The capital of Ohio is Columbus.',
            'columbus': 'Columbus is the capital of Ohio.',
            'oklahoma': 'The capital of Oklahoma is Oklahoma City.',
            'oklahoma city': 'Oklahoma City is the capital of Oklahoma.',
            'oregon': 'The capital of Oregon is Salem.',
            'salem': 'Salem is the capital of Oregon.',
            'pennsylvania': 'The capital of Pennsylvania is Harrisburg.',
            'harrisburg': 'Harrisburg is the capital of Pennsylvania.',
            'rhode island': 'The capital of Rhode Island is Providence.',
            'providence': 'Providence is the capital of Rhode Island.',
            'south carolina': 'The capital of South Carolina is Columbia.',
            'columbia': 'Columbia is the capital of South Carolina.',
            'south dakota': 'The capital of South Dakota is Pierre.',
            'pierre': 'Pierre is the capital of South Dakota.',
            'tennessee': 'The capital of Tennessee is Nashville.',
            'nashville': 'Nashville is the capital of Tennessee.',
            'texas': 'The capital of Texas is Austin.',
            'austin': 'Austin is the capital of Texas.',
            'utah': 'The capital of Utah is Salt Lake City.',
            'salt lake city': 'Salt Lake City is the capital of Utah.',
            'vermont': 'The capital of Vermont is Montpelier.',
            'montpelier': 'Montpelier is the capital of Vermont.',
            'virginia': 'The capital of Virginia is Richmond.',
            'richmond': 'Richmond is the capital of Virginia.',
            'washington': 'The capital of Washington is Olympia.',
            'west virginia': 'The capital of West Virginia is Charleston.',
            'charleston': 'Charleston is the capital of West Virginia.',
            'wisconsin': 'The capital of Wisconsin is Madison.',
            'madison': 'Madison is the capital of Wisconsin.',
            'wyoming': 'The capital of Wyoming is Cheyenne.',
            'cheyenne': 'Cheyenne is the capital of Wyoming.',
         }
```

## STEP 16: Populate Our State Capital Fill In The Blank Quiz
Go into the Python Web Editor and delete our `generic_teq_f` database and replace it with the following database.
```python
# State capital talking educational fill in the blank quiz database
sc_teq_f = {
                'What is the capital of Pennsylvania?': 'Harrisburg',
                'Harrisburg is the capital of what state?': 'Pennsylvania',
                'What is the capital of Texas?': 'Austin',
                'What is the capital of Arkansas?': 'Little Rock',
                'What is the capital of California?': 'Sacramento',
                'Olympia is the capital of what state?': 'Washington',
                'What is the capital of Utah?': 'Salt Lake City',
                'What is the capital of Kansas?': 'Topeka',
                'What is the capital of Maine?': 'Augusta',
                'What is the capital of Virginia?': 'Richmond'
           }
```

## STEP 17: Populate Our State Capital Multiple Choice Quiz
Go into the Python Web Editor and delete our `generic_teq_m` database and replace it with the following database.
```python
# State capital talking educational multiple choice quiz database
sc_teq_m = {
                'What is the capital of Pennsylvania?': 
                [
                    'Philadelphia', 
                    'Pittsburgh', 
                    'Harrisburg', 
                    2
                ],
                'Harrisburg is the capital of what state?':
                [
                    'West Virginia', 
                    'Pennsylvania', 
                    'New Jersey', 
                    1
                ],
                'What is the capital of Texas?':
                [
                    'Houston',
                    'El Paso',
                    'Austin',
                    2
                ],
                'What is the capital of Arkansas?':
                [
                    'Little Rock',
                    'Mobile',
                    'Hope',
                    0
                ],
                'What is the capital of California?':
                [
                    'Los Angeles',
                    'San Francisco',
                    'Sacramento',
                    2
                ],
                'Olympia is the capital of what state?':
                [
                    'Oregon',
                    'Washington',
                    'Idaho',
                    1
                ],
                'What is the capital of Utah?':
                [
                    'Salt Lake City',
                    'Provo',
                    'Salem',
                    0
                ],
                'What is the capital of Kansas?':
                [
                    'Topeka',
                    'Omaha',
                    'Kansas City',
                    0
                ],
                'What is the capital of Maine?':
                [
                    'Portland',
                    'Augusta',
                    'Lewiston',
                    1
                ],
                'What is the capital of Virginia?':
                [
                    'Chantilly',
                    'Richmond',
                    'Arlington',
                    1
                ]
           }
```

## STEP 18: Repeat Steps 9-12

## STEP 19: Communicate With The micro:bit sc TED Bot & Take The Fill In The Blank Quiz, Multiple-Choice Quiz
```
>>> import main
>>> main.bot(sc_ted, 'What is the capital of Pennsylvania?')
BOT: The capital of Pennsylvania is Harrisburg.
>>> main.bot(sc_ted, 'What is the capital of Texas?')
BOT: The capital of Texas is Austin.
>>> main.bot(sc_ted, 'Topeka is the capital of what state?')
BOT: Topeka is the capital of Kansas.
>>>
>>> main.quiz_f(sc_teq_f)
Harrisburg is the capital of what state?
ANSWER: Pennsylvania
CORRECT!
What is the capital of Utah?
ANSWER: Provo
The correct answer is Salt Lake City.
What is the capital of Maine?
ANSWER: Augusta
CORRECT!
What is the capital of Virginia?
ANSWER: Richmond
CORRECT!
What is the capital of Pennsylvania?
ANSWER: Harrisburg
CORRECT!
What is the capital of Arkansas?
ANSWER: Hope
The correct answer is Little Rock.
What is the capital of California?
ANSWER: Sacramento
CORRECT!
What is the capital of Texas?
ANSWER: Houston
The correct answer is Austin.
Olympia is the capital of what state?
ANSWER: Wyoming
The correct answer is Washington.
What is the capital of Kansas?
ANSWER: Topeka
CORRECT!
You got 6 out of 10 correct!
You are doing a great job!
I would LOVE for you to try again!
>>>
>>> main.quiz_m(sc_teq_m)
Harrisburg is the capital of what state?
Press A for West Virginia.
Touch the logo for Pennsylvania.
Press B for New Jersey.
You selected Pennsylvania.
CORRECT!
What is the capital of Utah?
Press A for Salt Lake City.
Touch the logo for Provo.
Press B for Salem.
You selected Provo.
The correct answer is Salt Lake City.
What is the capital of Maine?
Press A for Portland.
Touch the logo for Augusta.
Press B for Lewiston.
You selected Portland.
The correct answer is Augusta.
What is the capital of Virginia?
Press A for Chantilly.
Touch the logo for Richmond.
Press B for Arlington.
You selected Richmond.
CORRECT!
What is the capital of Pennsylvania?
Press A for Philadelphia.
Touch the logo for Pittsburgh.
Press B for Harrisburg.
You selected Harrisburg.
CORRECT!
What is the capital of Arkansas?
Press A for Little Rock.
Touch the logo for Mobile.
Press B for Hope.
You selected Little Rock.
CORRECT!
What is the capital of California?
Press A for Los Angeles.
Touch the logo for San Francisco.
Press B for Sacramento.
You selected Sacramento.
CORRECT!
What is the capital of Texas?
Press A for Houston.
Touch the logo for El Paso.
Press B for Austin.
You selected Houston.
The correct answer is Austin.
Olympia is the capital of what state?
Press A for Oregon.
Touch the logo for Washington.
Press B for Idaho.
You selected Washington.
CORRECT!
What is the capital of Kansas?
Press A for Topeka.
Touch the logo for Omaha.
Press B for Kansas City.
You selected Topeka.
CORRECT!
You got 7 out of 10 correct!
You are doing a great job!
I would LOVE for you to try again!
>>>
```

## STEP 20: Populate Our Parts Of A Cell Database
Go into the Python Web Editor and select line 116.  Press enter to create a new blank line and paste the following on the new blank line 117.
```python
# Parts of a cell educational database
poc_ted = {
            'nucleus': 'The nucleus controls the cell\'s operations.',
            'cell membrane': 'The cell membrane controls what comes into and out of the cell.',
            'cytoplasm': 'Cytoplasm is the fluid inside a cell surrounding the nucleus.',
            'cell wall': 'A cell wall is a rigid layer outside of the plasma membrane.',
            'central vacuole': 'A central vacuole is a watery fluid that maintains the life of a cell.',
            'endoplasmic reticulum': 'Endoplasmic reticulum is the transportation system of a cell.',
            'ribosome': 'A ribosome produces proteins with ribonucleic acid.',
            'golgi body': 'A golgi body packages proteins into vesicles.',
            'lysosome': 'A lysosome contains digestive enzymes.',
            'chloroplast': 'A chloroplast makes energy for a cell.',
            'mitochondria': 'Mitochondria provides energy that cells need to divide, move and contract.',
            'cytoskeleton': 'A cytoskeleton is in animals only and is used for support.',
            'centrioles': 'Centrioles helps in cell division in animals.'
          }
```

## STEP 21: Populate Our Parts Of A Cell Fill In The Blank Quiz
Go into the Python Web Editor and select line 245.  Press enter to create a new blank line and paste the following on the new blank line 246.
```python
# Parts of a cell talking educational fill in the blank quiz database
poc_teq_f = {
                'What controls the cell\'s operations?': 'nucleus',
                'What controls what comes into and out of the cell?': 'cell membrane',
                'What is the fluid inside a cell surrounding the nucleus?': 'cytoplasm',
                'What is a rigid layer outside of the plasma membrane?': 'cell wall',
                'What is a watery fluid that maintains the life of a cell?': 'central vacuole',
                'What produces proteins with ribonucleic acid?': 'ribosome',
                'What contains digestive enzymes?': 'lysosome',
                'What makes energy for a cell?': 'chloroplast',
                'What is in animals only and is used for support?': 'cytoskeleton',
                'What helps in cell division in animals?': 'centrioles'
            }
```

## STEP 22: Rename Script Name To sb_poc
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Study_Buddy/blob/main/STEP%2022.png?raw=true)

## STEP 23: Populate Our Parts Of A Cell Database
Go into the Python Web Editor and delete our `sc_ted` database and replace it with the following database.
```python
# Parts of a cell educational database
poc_ted = {
            'nucleus': 'The nucleus controls the cell\'s operations.',
            'cell membrane': 'The cell membrane controls what comes into and out of the cell.',
            'cytoplasm': 'Cytoplasm is the fluid inside a cell surrounding the nucleus.',
            'cell wall': 'A cell wall is a rigid layer outside of the plasma membrane.',
            'central vacuole': 'A central vacuole is a watery fluid that maintains the life of a cell.',
            'endoplasmic reticulum': 'Endoplasmic reticulum is the transportation system of a cell.',
            'ribosome': 'A ribosome produces proteins with ribonucleic acid.',
            'golgi body': 'A golgi body packages proteins into vesicles.',
            'lysosome': 'A lysosome contains digestive enzymes.',
            'chloroplast': 'A chloroplast makes energy for a cell.',
            'mitochondria': 'Mitochondria provides energy that cells need to divide, move and contract.',
            'cytoskeleton': 'A cytoskeleton is in animals only and is used for support.',
            'centrioles': 'Centrioles helps in cell division in animals.'
          }
```

## STEP 24: Populate Our Parts Of A Cell Fill In The Blank Quiz
Go into the Python Web Editor and delete our `sc_teq_f` database and replace it with the following database.
```python
# Parts of a cell talking educational fill in the blank quiz database
poc_teq_f = {
                'What controls the cell\'s operations?': 'nucleus',
                'What controls what comes into and out of the cell?': 'cell membrane',
                'What is the fluid inside a cell surrounding the nucleus?': 'cytoplasm',
                'What is a rigid layer outside of the plasma membrane?': 'cell wall',
                'What is a watery fluid that maintains the life of a cell?': 'central vacuole',
                'What produces proteins with ribonucleic acid?': 'ribosome',
                'What contains digestive enzymes?': 'lysosome',
                'What makes energy for a cell?': 'chloroplast',
                'What is in animals only and is used for support?': 'cytoskeleton',
                'What helps in cell division in animals?': 'centrioles'
            }
```

## STEP 25: Populate Our Parts Of A Cell Multiple Choice Quiz
Go into the Python Web Editor and delete our `sc_teq_m` database and replace it with the following database.
```python
# Parts of a cell talking educational multiple choice quiz database
poc_teq_m = {
                'What controls the cell\'s operations?':
                [
                    'nucleus',
                    'ribosome',
                    'lysosome',
                    0
                ],
                'What controls what comes into and out of the cell?':
                [
                    'cytoplasm',
                    'cell membrane',
                    'cytoskeleton',
                    1
                ],
                'What is the fluid inside a cell surrounding the nucleus?':
                [
                    'central vacuole',
                    'centrioles',
                    'cytoplasm',
                    2
                ],
                'What is a rigid layer outside of the plasma membrane?':
                [
                    'cell wall',
                    'cytoskeleton',
                    'cell membrane',
                    0
                ],
                'What is a watery fluid that maintains the life of a cell?':
                [
                    'chloroplast',
                    'central vacuole',
                    'chloroplast',
                    1
                ],
                'What produces proteins with ribonucleic acid?':
                [
                    'lysosome',
                    'centrioles',
                    'ribosome',
                    2
                ],
                'What contains digestive enzymes?':
                [
                    'lysosome',
                    'nucleus',
                    'chloroplast',
                    0
                ],
                'What makes energy for a cell?':
                [
                    'ribosome',
                    'chloroplast',
                    'cytoplasm',
                    1
                ],
                'What is in animals only and is used for support?':
                [
                    'cytoskeleton',
                    'cell wall',
                    'cell membrane',
                    0
                ],
                'What helps in cell division in animals?': 
                [
                    'central vacuole',
                    'chloroplast',
                    'centrioles',
                    2
                ]
            }
```

## STEP 26: Repeat Steps 9-12

## STEP 27: Communicate With The micro:bit poc TED Bot & Take The Fill In The Blank Quiz, Multiple-Choice Quiz
```
>>> import main
>>> main.bot(poc_ted, 'What is a nucleus?')
BOT: The nucleus controls the cell's operations.
>>> main.bot(poc_ted, 'What is a lysosome?')
BOT: A lysosome contains digestive enzymes.
>>> main.bot(poc_ted, 'What is a ribosome?')
BOT: A ribosome produces proteins with ribonucleic acid.
>>> 
>>> main.quiz_f(poc_teq_f)
What helps in cell division in animals?
ANSWER: centrioles
CORRECT!
What is a rigid layer outside of the plasma membrane?
ANSWER: lysosome
The correct answer is cell wall.
What controls what comes into and out of the cell?
ANSWER: cell membrane
CORRECT!
What makes energy for a cell?
ANSWER: chloroplast
CORRECT!
What contains digestive enzymes?
ANSWER: lysosome
CORRECT!
What is in animals only and is used for support?
ANSWER: centrioles
The correct answer is cytoskeleton.
What is the fluid inside a cell surrounding the nucleus?
ANSWER: cytoplasm
CORRECT!
What controls the cell's operations?
ANSWER: nucleus
CORRECT!
What is a watery fluid that maintains the life of a cell?
ANSWER: central vacuole
CORRECT!
What produces proteins with ribonucleic acid?
ANSWER: ribosome
CORRECT!
You got 8 out of 10 correct!
You are doing a great job!
I would LOVE for you to try again!
>>>
>>> main.quiz_m(poc_teq_m)
What helps in cell division in animals?
Press A for central vacuole.
Touch the logo for chloroplast.
Press B for centrioles.
You selected centrioles.
CORRECT!
What is a rigid layer outside of the plasma membrane?
Press A for cell wall.
Touch the logo for cytoskeleton.
Press B for cell membrane.
You selected cell wall.
CORRECT!
What controls what comes into and out of the cell?
Press A for cytoplasm.
Touch the logo for cell membrane.
Press B for cytoskeleton.
You selected cytoplasm.
The correct answer is cell membrane.
What makes energy for a cell?
Press A for ribosome.
Touch the logo for chloroplast.
Press B for cytoplasm.
You selected chloroplast.
CORRECT!
What contains digestive enzymes?
Press A for lysosome.
Touch the logo for nucleus.
Press B for chloroplast.
You selected lysosome.
CORRECT!
What is in animals only and is used for support?
Press A for cytoskeleton.
Touch the logo for cell wall.
Press B for cell membrane.
You selected cytoskeleton.
CORRECT!
What is the fluid inside a cell surroudning the nucleus?
Press A for central vacuole.
Touch the logo for centrioles.
Press B for cytoplasm.
You selected cytoplasm.
CORRECT!
What controls the cell's operations?
Press A for nucleus.
Touch the logo for ribosome.
Press B for lysosome.
You selected nucleus.
CORRECT!
What is a watery fluid that maintains the life of a cell?
Press A for chloroplast.
Touch the logo for central vacuole.
Press B for chloroplast.
You selected central vacuole.
CORRECT!
What produces proteins with ribonucleic acid?
Press A for lysosome.
Touch the logo for centrioles.
Press B for ribosome.
You selected ribosome.
CORRECT!
You got 9 out of 10 correct!
You are doing a great job!
I would LOVE for you to try again!
>>> 
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
