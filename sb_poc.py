import gc
import time

from microbit import display, Image, pin_logo, button_a, button_b
from music import play, POWER_UP
from speech import say

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
                
def bot(ted, question):
    """Bot function

    Parameters
    ----------
    ted : dict
        Talking educational database to utilize
    question : str
        Question to parse for trigger words

    Returns
    -------
    None
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
            say(str(response[0]))
            display.show(Image.HAPPY)
        else:
            display.show(Image.SURPRISED)
            print('BOT: That is not something I am familiar with.')
            say('That is not something I am familiar with.')
            display.show(Image.HAPPY)
            
    gc.collect()
        
        
def quiz_f(teq):
    """Fill in the blank quiz function

    Parameters
    ----------
    teq : dict
        Talking educational quiz to utilize

    Returns
    -------
    None
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
        say(str(key))
        response = input('ANSWER: ')
        response = response.lower()
        correct_answer = teq[key].lower()
        if response == correct_answer:
            display.show(Image.SURPRISED)
            print('CORRECT!')
            say('CORRECT!')
            display.show(Image.HAPPY)
            score += 1
        else:
            display.show(Image.SURPRISED)
            print('The correct answer is {0}.'.format(teq[key]))
            say('The correct answer is')
            say(str(teq[key]))
            display.show(Image.HAPPY)
        time.sleep(1)
        gc.collect()
    
    # Here we reply to the student their score
    display.show(Image.SURPRISED)
    print('You got {0} out of {1} correct!'.format(score, len(teq)))
    say('You got')
    say(str(score))
    say('out of')
    say(str(len(teq)))
    say('correct!')
    
    # If student got a perfect score respond appropriately
    # or provide an encouring message to retry the quiz
    if score == len(teq):
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
    
    gc.collect()
    
    
def quiz_m(teq):
    """Multiple choice quiz function

    Parameters
    ----------
    teq : dict
        Talking educational quiz to utilize

    Returns
    -------
    None
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
        say(str(key))
        print('Press A for {0}.'.format(teq[key][0]))
        say('Press A for')
        say(str(teq[key][0]))
        print('Touch the logo for {0}.'.format(teq[key][1]))
        say('Touch the logo for')
        say(str(teq[key][1]))
        print('Press B for {0}.'.format(teq[key][2]))
        say('Press B for')
        say(str(teq[key][2]))
        display.show(Image.HAPPY)
        #response = ''
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
        say('You selected')
        say(str(teq[key][response]))
        display.show(Image.HAPPY)
        if response == correct_answer:
            display.show(Image.SURPRISED)
            print('CORRECT!')
            say('CORRECT!')
            display.show(Image.HAPPY)
            score += 1
        else:
            display.show(Image.SURPRISED)
            print('The correct answer is {0}.'.format(teq[key][correct_answer]))
            say('The correct answer is')
            say(str(teq[key][correct_answer]))
            display.show(Image.HAPPY)
        time.sleep(1)
        gc.collect()
    
    # Here we reply to the student their score
    display.show(Image.SURPRISED)
    print('You got {0} out of {1} correct!'.format(score, len(teq)))
    say('You got')
    say(str(score))
    say('out of')
    say(str(len(teq)))
    say('correct!')
    
    # If student got a perfect score respond appropriately
    # or provide an encouring message to retry the quiz
    if score == len(teq):
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
    
    gc.collect()
