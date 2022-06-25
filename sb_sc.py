import gc
import time

from microbit import display, Image, pin_logo, button_a, button_b
from music import play, POWER_UP
from speech import say

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
    Function to handle fill in the blank quiz

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

    Parames:
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
