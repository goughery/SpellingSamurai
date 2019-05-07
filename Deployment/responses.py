#not all of the responses are in here yet

class responses():
    def welcome(phase):
        if phase == 0:
            response = """Welcome to Spelling Samurai. <break/> This is a real-time spelling quiz. <break/> Since it's your first time, let's add five words to your first list. <break/> When you're ready just say <break/> add words."""
        elif phase == 1:
            response = """Welcome back to Spelling Samurai. Remember, we need to set up your list. This time, <break/> let's just add five words. <break/> Grab your spelling list, and when you're ready, please say: <break/> add words.
                        If you need help, just say I need help."""
        else:
            response = """Welcome back to Spelling Samurai. Do you want to add words <break/> or start the quiz? <break/> Remember <break/> if you need help, say <break/>I need help."""
        return response
        
    def help(phase):
        if phase == 0:
            response = """This skill is a real-time spelling quiz. <break/>
                        First, create a word list by saying <break/> add words. Then, say each word <break/> while I listen. Once we have a list, you can say <break/> quiz me.
                        I'll say the word, and you spell it after the chime. <break/>
                        You can also have multiple lists. <break/> If you want to add words to a different list, say <break/> add words to list two. Then, to be tested on that list, say <break/> quiz me on list two.
                        At the end of each test, I tell you your score.<break/> 
    
                        <break/> You can also delete words from lists by saying <break/> delete words. <break/> Or you can delete or clear entire lists buy saying <break/> delete list. <break/>"""
        #reprompt
        else:
            response = "So please tell me what you'd like to do: add words <break/>, delete words, <break/> delete list, <break/> or<break/> start quiz."
        return response
    
    def bogey(phase):
        response = """Please don't start spelling until after the chime. Let's try again."""
        return reponse
    
    def listNotExist(phase):
        if phase == 0:
            response = "That list doesn't exist. <break/> Please tell me to quiz you on a list that does exist <break/> or start buy saying <break/> add words <break/> to list one."
        #reprompt
        else:
            response = "Sorry. You can tell me to start a quiz and add words to lists. <break/> You can also say help to ask for help."
        return response
    
    def sessionEnd(phase):
        if phase == 0:
            response = "Something went wrong with the skill. If you'd like to provide helpful feedback, please email the developer using the address in the skill description. Thank you in advance."
        else:
            response = "Thank you for using Spelling Samurai. Have a nice day!"
            
        return response
