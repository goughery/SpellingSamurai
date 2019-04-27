
from __future__ import print_function
import random, re
import logging
import json
from data_handler import add_increment_userDB, add_wordsDB, get_wordsDB, check_listDB, check_userSessionsDB, get_paidDB, set_paidDB, set_gradeDB, get_GradewordsDB, delete_wordsDB, delete_listDB
from getSpelled import getSpelled
import logging, traceback

_wordList = ["polymorphous", "mouse"]
spB = "<speak>"
spE = "</speak>"
maxWordsNumber = 8
maxWordsWord = "eight"
# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session, directives=[]):
    content = output.replace("\\n","")
    content = re.sub('<.*?>','',content, flags=re.DOTALL)
    
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': content
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': reprompt_text
            }
        },
        'shouldEndSession': should_end_session,
        'directives': directives
        
    }


def build_response(session_attributes, speechlet_response): #, directives = {}
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
    #,'directives': [directives]

def create_word_attributes(correctWord, wordSpelled, wordsLeftList, nuCorrect, nuTotal, timedelay):
    return {"correctWord": correctWord, "wordSpelled": wordSpelled, "wordsLeft": wordsLeftList, "nuCorrect": nuCorrect, "nuTotal": nuTotal, "timedelay": timedelay}
    
    
def continue_dialog(state, intentname = "", slotname="", slotvalue=""):
    message = {}
    message['shouldEndSession'] = False
    message['directives'] = [{'type': 'Dialog.Delegate'}]
    sessionAttributes = {}
    return build_response(sessionAttributes, message)
    
    
    
#-------match regex-----------
def getMatchRegX(correctWord):
    word = correctWord.replace(" ", "")
    
    lettersCombos = ['[zc]', '[cz]', '[mn]', '[nm]', '[bd]', '[db]', '[td]', '[dt]', '[bp]', '[pb]']
    
    match = word
    
    replaceDict = {}
    for i in range(len(word)):
        replaceDict[i] = []
        for combo in lettersCombos:
            if word[i] in combo[1]:
                replaceDict[i].append(combo)
    
    for key in replaceDict:
        if not replaceDict[key]:
            replaceDict[key] = word[key]
    
    #print(replaceDict)
    regExL = []
    for key in replaceDict:
        multCombo = ""
        for combo in replaceDict[key]:
            if replaceDict[key].index(combo) == 0 and len(replaceDict[key])>1:
                combo = combo.replace("]", "")
            elif replaceDict[key].index(combo) != 0 and combo != replaceDict[key][-1]:
                combo = combo.replace("[", "")
                combo = combo.replace("]", "")
            elif len(replaceDict[key]) > 1:
                combo = combo.replace("[", "")
            multCombo += combo
        multComboDD = ""
        for letter in multCombo:
            if letter not in multComboDD:
                multComboDD += letter
        regExL.append(multComboDD)
     
    
    #print(regExL)
    
    regExS = ""
    for item in regExL:
        regExS += item
    #print(regExS)
    
    rX = re.compile(regExS)
    return rX
    
def set_word_in_session():
    correctWord = random.choice(_wordList)
    return correctWord

def makeWordSpellable(wordSpelled,time):
    output = ""
    for letter in wordSpelled:
        output += letter + "<break time='"+str(time)+"ms'/>"
    return output

# --------------- Functions that control the skill's behavior ------------------
def error_response(where):
    output = 'App died in ' + where
    should_end_session = 'True'
    title = 'Error'
    reprompt_text = 'blank reprompt'
    return build_speechlet_response(title, output, reprompt_text, should_end_session)


def welcome_text(sessionCount, listCount):
    if sessionCount == 1 and len(listCount) == 0:
        speech_output = """Welcome to the Spelling Samurai skill.
        I can help you become a better speller <break/> and prepare for school tests by spelling words in real-time <break/> using your own spelling lists. 
        Let's start by adding your very first list of words. This time, <break/> let's just add five words. <break/> Grab your spelling list, and when you're ready and I'm listening, please say: <break/> add words to <break/> list one. <break/>
        Afterwords, you can delete these words by saying <break/> delete words. <break/> If you need help, just say I need help."""
    elif sessionCount > 1 and len(listCount) == 0:
        speech_output = """Welcome back to the Spelling Samurai skill.
        I can help you become a better speller <break/> and prepare for school tests by spelling words in real-time <break/> using your own spelling lists. 
        Remember, we need to set up your first list. This time, <break/> let's just add five words. <break/> Grab your spelling list, and when you're ready and I'm listening, please say: <break/> add words to <break/> list one.
        If you need help, just say I need help."""
    else:
        speech_output = """Welcome back to the Spelling Samurai skill. Please say start quiz <break/>, <break/> add words, <break/> delete list, <break/> or delete words. Remember <break/> if you need help, say <break/>I need help."""
        
        
    speech_output = spB + speech_output + spE
    return speech_output
    
def get_help_response():
    session_attributes = {"startingtest": 1}
    card_title = "Help"
    should_end_session = False
    
    speech_output = """Help is here. I'm going to explain how this skill works so that you can better use it.
    This skill is a real-time spelling quiz which tests you on how to spell words as if somebody were helping you <break/>, perhaps using flash cards.
    First, you must create a spelling words list by saying <break/> add words. Then, say your words in one go <break/> one after another in succession. Once we have a list, you can say <break/> quiz me. 
    You can also have multiple lists. If you want to add words to a different list you would say <break/> add words to list two. Then, to be tested on that list, you would say <break/> quiz me on list two.
    At the end of each test, I tell you your score.<break/> 
    At the end of each word prompt is a small delay so that you are able to think before spelling. Please start spelling after the chime.<break/>
    <break/> You can also delete words from lists by saying <break/> delete words. <break/> Or you can delete or clear entire lists buy saying <break/> delete list. <break/>"""
    reprompt_text = "So please tell me what you'd like to do: add words <break/>, delete words, <break/> delete list, <break/> or<break/> start quiz."
    
    speech_output = speech_output + reprompt_text
    speech_output = spB + speech_output + spE
    reprompt_text = spB + reprompt_text + spE
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
    
def get_welcome_response(session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    
    sessionCount = check_userSessionsDB(session)
    listCount = check_listDB(session)
    speech_output = welcome_text(sessionCount, listCount)
    
    session_attributes = {"startingtest": 1}
    card_title = "Welcome"
    
    reprompt_text = welcome_text(sessionCount, listCount)
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
def bogey():
    speech_output = """Please don't start spelling until after the chime. Let's try again."""
    card_title = "Bogey"
    should_end_session = False 
    speech_output  = spB + speech_output + spE
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))
        
def listNotExist():
    session_attributes = ""
    card_title = "List Doesn't Exist"
    speech_output = "That list doesn't exist. <break/> "
    speech_output += "Please tell me to quiz you on a list that does exist <break/> or start buy saying <break/> add words <break/> to list one."

    reprompt_text = "Sorry. You can tell me to start a quiz and add words to lists."
    reprompt_text += "You can also say help to ask for help. "
    should_end_session = False
    reprompt_text = spB + reprompt_text + spE
    speech_output = spB + speech_output + spE
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request(error = 0):
    card_title = "Session Ended"
    if error == 1:
        speech_output = "Something went wrong with the skill. If you'd like to provide helpful feedback, please email the developer using the address in the skill description. Thank you in advance."
    else:
        speech_output = "Thank you for using the Spelling Samurai skill. " \
                        "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    speech_output  = spB + speech_output + spE
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def purchase_intent(session):
    #set_paidDB(session, 1)
    sessionAttributes = {}
    userID = session['user']['userId']
    speech_output  = spB + "Purchasing Unlimited words." + spE
    reprompt_text = spB + "Purchase Unlimited words." + spE
    card_title = "Purchasing."
    should_end_session = True
    
    
    directive = [{
					'type': "Connections.SendRequest",
            'name': "Buy",
            'payload': {
                'InSkillProduct': {
                    'productId': "amzn1.adg.product.834d41d5-e3f3-4ad8-8c4f-115a47c11364",
                }
            
            },
            'token': userID
				}
				]
    sessionAttributes = {}
    #return build_response(sessionAttributes, message)
    return build_response(sessionAttributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session, directive))
  
def refund_intent(session):
    #set_paidDB(session, 1)
    sessionAttributes = {}
    userID = session['user']['userId']
    speech_output  = spB + "Refunding Unlimited words." + spE
    reprompt_text = spB + "Refunding Unlimited words." + spE
    card_title = "Refunding."
    should_end_session = True
    
    message = {}
    directive = [{
					'type': "Connections.SendRequest",
            'name': "Cancel",
            'payload': {
                'InSkillProduct': {
                    'productId': "amzn1.adg.product.834d41d5-e3f3-4ad8-8c4f-115a47c11364",
                }
            
            },
            'token': userID
				}
				]
    sessionAttributes = {}
    return build_response(sessionAttributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session, directive))


def delete_words(session, intent_request={'dialogState':'In_Progress'}):
    add_increment_userDB(session, 0)
    speech_output = ""
    dialog_state = intent_request['dialogState']
    if dialog_state != "COMPLETED":
        return continue_dialog(dialog_state)
    else:
        listChoice = intent_request['intent']['slots']['ListNumber']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
        listsUsed = check_listDB(session)
        if len(listsUsed) == 0 and listChoice.lower() != "one":
            listChoice = "one"
            speech_output = "Cannot delete from that list yet. "
        else:
            listChoice = intent_request['intent']['slots']['ListNumber']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
            
        wordsSpoken = intent_request['intent']['slots']['Words']['value']
        wordList = []
        wordString = ""
        for word in wordsSpoken.split(" "):
            wordList.append(word)
            wordString += word + ", "
        wordString = wordString[:-2]
        #delete the words from the database
        delete_wordsDB(session, wordList, listNum = listChoice)
        speech_output = "Words deleted from list. Those words are <break/> %s. "%(wordString)
        reprompt_text = "<break/>If you'd like to delete more words, <break/> just say delete words. <break/> Otherwise you can say add words, delete list, or start quiz. <break/>"
        speech_output += reprompt_text
        reprompt_text = speech_output
        
        speech_output  = spB + speech_output + spE
        reprompt_text = spB + reprompt_text + spE
        card_title = "Delete Words"
        should_end_session = False
        return build_response({}, build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))
            
def delete_list(session, intent_request={'dialogState':'In_Progress'}):
    add_increment_userDB(session, 0)
    speech_output = ""
    dialog_state = intent_request['dialogState']
    if dialog_state != "COMPLETED":
        return continue_dialog(dialog_state)
    else:
        listChoice = intent_request['intent']['slots']['ListNumber']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
        listsUsed = check_listDB(session)
        if len(listsUsed) == 0 and listChoice.lower() != "one":
            listChoice = "one"
            speech_output = "Cannot delete that list yet. "
        else:
            listChoice = intent_request['intent']['slots']['ListNumber']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
            
        #delete the list from the database
        delete_listDB(session, listNum = listChoice)
        speech_output = "List %s cleared. <break/> "%(listChoice)
        reprompt_text = "If you'd like to delete more lists, <break/> just say delete list. <break/> Otherwise you can say add words, delete words, or start quiz. <break/>"
        speech_output += reprompt_text
        reprompt_text = speech_output
        
        speech_output  = spB + speech_output + spE
        reprompt_text = spB + reprompt_text + spE
        card_title = "Delete List"
        should_end_session = False
        return build_response({}, build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))



def add_words(session, intent_request={'dialogState':'In_Progress'}):
    add_increment_userDB(session, 0)
    speech_output = ""
    dialog_state = intent_request['dialogState']
    if dialog_state != "COMPLETED":
        return continue_dialog(dialog_state)
    else:
        listChoice = intent_request['intent']['slots']['ListNumber']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
        listsUsed = check_listDB(session)
        if len(listsUsed) == 0 and listChoice.lower() != "one":
            listChoice = "one"
            speech_output = "Cannot add to that list yet. List one created. "
        else:
            listChoice = intent_request['intent']['slots']['ListNumber']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
            
        wordsSpoken = intent_request['intent']['slots']['Words']['value']
        wordList = []
        wordString = ""
        for word in wordsSpoken.split(" "):
            wordList.append(word)
            wordString += word + ", "
        wordString = wordString[:-2]
        #add the words to the database
        if get_paidDB(session) == 1:
            #if user paid
            add_wordsDB(session, wordList, listNum = listChoice)
            speech_output += "Words added to list %s. " %(listChoice)
            speech_output += "Those words are: %s. " %(wordString)
            reprompt_text = "Now you can say <break/> add more words, <break/> delete words, delete list, <break/> or say start quiz."
            speech_output += reprompt_text
        else: 
            #if user not paid, check nu of words in list
            
            if len(get_wordsDB(session, listChoice)) >= maxWordsNumber:
                #if the words in the db equals the max, cut them off right away
                speech_output += "You already have %s words in this list. <break/> <break/>"%(maxWordsWord)
                reprompt_text = "To support the developer, please consider purchasing the full version of this skill, <break/> in which there is no limit on word count. If you'd like more details, <break/> please say <break/> purchase unlimited words. <break/>"
                reprompt_text += "Otherwise <break/> say <break/> delete words, delete list, <break/> or start quiz."
                speech_output += reprompt_text
            else:
                #if the number of words in the db is less than the max, allow them to add just to the max
                numToAdd = maxWordsNumber-len(get_wordsDB(session, listChoice))
                if numToAdd < 0:
                    numToAdd = 0
                #if words to add is shorter than original wordlist
                if len(wordList) > len(wordList[:numToAdd]):
                    cutOff = 1
                else:
                    cutOff = 0
                wordList = wordList[:numToAdd]
                add_wordsDB(session, wordList, listNum = listChoice)
                wordString = ""
                if len(wordList) > 0:
                    wordString = ""
                    for word in wordList:
                        wordString += word + ", "
                    wordString = wordString[:-2]
                
                speech_output += "Words added to list %s. " %(listChoice)
                speech_output += "Those words are: %s. " %(wordString)
                if cutOff != 1:
                    reprompt_text = "If you'd like to add more words, just say add more words, or you can delete words, delete list, <break/> otherwise <break/> say start quiz."
                    speech_output += reprompt_text
                    reprompt_text = speech_output
                elif cutOff == 1:
                    reprompt_text = "The free version of this skill only supports adding a total of %s words to a list <break/>. To support the developer, please consider purchasing the full version of the skill, in which there is no limit. <break/> If you'd like more details before you buy <break/> please say <break/> learn more about unlimited words. <break/>"%(maxWordsWord)
                    reprompt_text += "Otherwise <break/> say <break/> delete words, delete list, <break/> or start quiz."
                    speech_output += reprompt_text
                
    
        speech_output  = spB + speech_output + spE
        reprompt_text = spB + reprompt_text + spE
        card_title = "Add Words"
        should_end_session = False
        return build_response({}, build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))



def spelling_quiz(intent_request, intent, session, startVar):
    try:
        dialog_state = intent_request['dialogState']
    except:
        dialog_state = "IN_PROGRESS"
    if dialog_state != "COMPLETED":
        return continue_dialog(dialog_state)
    else:
        card_title = "Spelling Test" #intent['name']
        should_end_session = False
        speech_output = ""
        reprompt_text = "I'm sorry. I didn't quite get that. Please spell it again."
        try:
            listChoice = intent['slots']['ListNumber']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
        except:
            listChoice = 'one'
        try:
            timedelay = intent['slots']['timedelay']['value']
        except:
            timedelay = "1"
        #if starting quiz 
        if startVar == 1:
            #on first go, set up session attributes and ask for first word
            try:
                wordList = get_wordsDB(session, listChoice)
                nuTotal = len(wordList)
                correctWord = random.choice(wordList)
                wordList.remove(correctWord)
                
            #if the above list is empty
            except:
                return listNotExist()
            
            session_attributes = create_word_attributes(correctWord, "", wordList, 0, nuTotal, timedelay)
            letsstartS = random.choice(["Ok, let's get started on the right foot. ", "Let's begin. ", "Good luck, and happy spelling. ", "Let's spell some words! "])
            speech_output = letsstartS + "How do you spell " + correctWord + "?<break time = '%ss'/><audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_neutral_response_01'/>"%(timedelay)
            
        else:
            #after spelling a word
            correctWord = session['attributes']['correctWord'].lower()
            wordSpelled = getSpelled(intent)
            # try:
            #     wordSpelled = intent['slots']['lettera']['value'].lower().replace(" ", "").replace(".","")
            #     wordSpelled += intent['slots']['letterb']['value'].lower().replace(" ", "").replace(".","")
            # except:
            #     wordSpelled = intent['slots']['lettera']['value'].lower().replace(" ", "").replace(".","")
                
            wordList = session['attributes']['wordsLeft']
            nuCorrect = session['attributes']['nuCorrect']
            nuTotal = session['attributes']['nuTotal']
            timedelay = session['attributes']['timedelay']
            
            #try to match word with similar sounds
            rX = getMatchRegX(correctWord)
            #check if word matches
            if rX.match(wordSpelled):
                good = random.choice(["Good job!", "Way to go!", "Not bad!", "Keep it up!", "You're a spelling guru!", "Great!", "You might be better than me!", "Fantastic!", "Superb!", "Awesome!"])
                speech_output += good   # + " You spelled " + correctWord + ". "
                nuCorrect += 1
            else:
                #if the starting letter isn't the same, they probably started spelling before the chime
                if correctWord[0] != wordSpelled[0]:
                    speech_output = "Please don't start spelling until after the chime. I'm going to add this word back into the shuffle."
                    wordList.append(correctWord)
                else:
                    letDownEasy = random.choice(["Better luck next time. ", "Ah. Not this time. ", "Incorrect. ", "Darn it. ", "Nope. Not this time. "])
                    speech_output += letDownEasy + "You spelled " + makeWordSpellable(wordSpelled,10) + ". "
                    speech_output += correctWord + " is spelled " + makeWordSpellable(correctWord,50) + ". "
            
            if len(wordList) > 0:
                #if there are still more words to spell
                correctWord = random.choice(wordList)
                wordList.remove(correctWord)
                newS = random.choice(["Alright. ", "Here's another. ", "Ok. " ])
                howS = random.choice(["Please spell: ", "Spell: ", "How do you spell: ", "How does one spell: ", "How would I spell: "])
                speech_output += "<break time='1s'/>" + newS + howS + correctWord + "?<break time = '%ss'/><audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_neutral_response_01'/>"%(timedelay)
                session_attributes = create_word_attributes(correctWord, "", wordList, nuCorrect, nuTotal, timedelay)
            else:
                if nuCorrect > 1:
                    ps = 'words'
                else:
                    ps = 'word'
                speech_output += ' Quiz complete. You got %s %s correct out of %s.'%(nuCorrect, ps, nuTotal)
                speech_output += '<break/>Did you enjoy the Spelling Samurai skill?<break/> Do you have any feedback?<break/> Please take a moment to rate the skill in the skill store, <break/> or email us for ways to better the experience. <break/> Thank you.'
                should_end_session = True
                session_attributes = create_word_attributes("", "", [], 0, 0, 1)
            
        speech_output = spB + speech_output + spE
        reprompt_text = spB + reprompt_text + spE
        
        return build_response(session_attributes, build_speechlet_response(
            card_title, speech_output, reprompt_text , should_end_session))


def getMatchRegX(correctWord):
    word = correctWord
    
    lettersCombos = ['[zc]', '[cz]', '[mn]', '[nm]', '[bd]', '[db]', '[td]', '[dt]', '[bp]', '[pb]']
    
    match = word
    
    replaceDict = {}
    for i in range(len(word)):
        replaceDict[i] = []
        for combo in lettersCombos:
            if word[i] in combo[1]:
                replaceDict[i].append(combo)
    
    for key in replaceDict:
        if not replaceDict[key]:
            replaceDict[key] = word[key]
    
    #print(replaceDict)
    regExL = []
    for key in replaceDict:
        multCombo = ""
        for combo in replaceDict[key]:
            if replaceDict[key].index(combo) == 0 and len(replaceDict[key])>1:
                combo = combo.replace("]", "")
            elif replaceDict[key].index(combo) != 0 and combo != replaceDict[key][-1]:
                combo = combo.replace("[", "")
                combo = combo.replace("]", "")
            elif len(replaceDict[key]) > 1:
                combo = combo.replace("[", "")
            multCombo += combo
        multComboDD = ""
        for letter in multCombo:
            if letter not in multComboDD:
                multComboDD += letter
        regExL.append(multComboDD)
     
    
    #print(regExL)
    
    regExS = ""
    for item in regExL:
        regExS += item
    #print(regExS)
    
    rX = re.compile(regExS)
    return rX


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(event, launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    add_increment_userDB(session, 1)
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response(session)


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])


    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']


    # Dispatch to your skill's intent handlers
    if intent_name == "StartTestIntent":
        return spelling_quiz(intent_request, intent, session, 1)
    elif intent_name == "SpellingIntent":
        return spelling_quiz(intent_request, intent, session, 0)
    elif intent_name == "AddWordsIntent":
        return add_words(session,intent_request)
    elif intent_name == "DeleteWordsIntent":
        return delete_words(session, intent_request)
    elif intent_name == "DeleteListIntent":
        return delete_list(session, intent_request)
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "PurchaseIntent":
        return purchase_intent(session)
    elif intent_name == "RefundIntent":
        return refund_intent(session)
    elif intent_name == "WhatCanIBuyIntent":
        return WhatCanIBuyIntent()
    elif intent_name == "WhatDidIBuyIntent":
        return WhatDidIBuyIntent(session)
    else:
        return handle_session_end_request()
        #raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

def afterPurchase(session):
    set_paidDB(session, 1)
    card_title = "Thank you."
    speech_output = "Thank you for your purchase. What would you like to do next?"
    speech_output = spB + speech_output + spE
    reprompt_text = speech_output
    should_end_session = False
        
    return build_response({}, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def afterNotPurchase():
    card_title = "Not purchased."
    speech_output = "Nothing was purchased. What would you like to do next?"
    speech_output = spB + speech_output + spE
    reprompt_text = speech_output
    should_end_session = False
        
    return build_response({}, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def afterRefund(session):
    #set_paidDB(session, 0)
    card_title = "Refund information sent."
    speech_output = "What would you like to do next?"
    speech_output = spB + speech_output + spE
    reprompt_text = speech_output
    should_end_session = False
        
    return build_response({}, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def WhatCanIBuyIntent():
    card_title = "What Can I Buy?"
    speech_output = "This skill offers a paid feature that offers adding an unlimited number of words to lists. <break/> To learn more, say: <break/> learn more about unlimited words."
    speech_output = spB + speech_output + spE
    reprompt_text = speech_output
    should_end_session = False
        
    return build_response({}, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def WhatDidIBuyIntent(session):
    card_title = "What Did I Buy?"
    if get_paidDB(session) == 1:
        speech_output = "Congrats! You purchased a paid feature that offers adding an unlimited number of words to lists. "
        speech_output += "<break/> What would you like to do next? You can say add words, start quiz, delete words, or delete list. "
        speech_output = spB + speech_output + spE
        reprompt_text = speech_output
        
    else:
        speech_output = "You haven't purchased anything! <break/> However, this skill offers a paid feature that boasts adding an unlimited number of words to lists. <break/> To learn more, say: <break/> learn more about unlimited words. "
        speech_output += "<break/> Otherwise you can say add words, start quiz, delete words, or delete list. "
        speech_output = spB + speech_output + spE
        reprompt_text = speech_output
    should_end_session = False
        
    return build_response({}, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    # print("event.session.application.applicationId=" +
    #       event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")
    
    

    # if event['session']['new']:
    #     on_session_started({'requestId': event['request']['requestId']},
    #                       event['session'])
    
    session = event['session']
    
    # # if "session" in event:
    # #     session = event['session']
    # else:
    #     if "payload" in event:
    #         if "purchaseResult" in event["payload"] and event["payload"]["purchaseResult"] == "ACCEPTED":
    #             return afterPurchase()
    #         elif "purchaseResult" in event["payload"] and event["payload"]["purchaseResult"] != "ACCEPTED":
    #             return afterNotPurchase()
    #         else:
    #             return afterRefund()
    
    try:            
    
        if event['request']['type'] == "LaunchRequest":
            return on_launch(event, event['request'], event['session'])
        elif event['request']['type'] == "IntentRequest":
            return on_intent(event['request'], event['session'])
    
        elif event['request']['type'] == "SessionEndedRequest":
            return on_session_ended(event['request'], event['session'])
        elif event['request']['type'] == "Connections.Response":
            if event['request']['name'] == "Buy":
                if event['request']['payload']['purchaseResult'] == "ACCEPTED":
                    return afterPurchase(session)
                else:
                    return afterNotPurchase()
            else:
                return afterRefund(session)
        else:
            return handle_session_end_request()
            
            
    except Exception as error:
        #print(error)
        logger = logging.getLogger()
        logger.setLevel(logging.ERROR)
        errorText = traceback.format_exc()
        logger.error(errorText)
        #logger.error(traceback.print_exc())
        #logger.error(error)
        return handle_session_end_request(error = 1)
