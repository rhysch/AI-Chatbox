# Rule based AI Python ChatBox
import datetime
import time

name = input("wlcm sir, enter your name : ")
present_hour = datetime.datetime.now().hour

if 5 <= present_hour <=11:
    print("Good mrng",name)

elif 11 <= present_hour <=17:
    print("Good Noon", name)

elif 17 <= present_hour <= 20:
    print("Gud evng",name)

else:
    print("Good night", name)

print("Namaste! welcome to Your  RhysChatBot")
print("You can ask me basic question, OR Type 'bye' to exit from the bot")

# Chatbot memory Creation [ dictionary of response ]

response = {
      "hello":"Hi , welcome.How can I help you?",
      "how are you": "I am fine . Thankyou" ,
      "who are you": "I am smart Ai Chatbot",
      "motivate me": "Keep going. Every bug of the project makes you a better developer best programmer",
      "happy": "Great to hear that",
      " What is the Function?" : "Go to the claud"
    
    }
# Method/Function to get response of Chatbot
def getresponse_Bot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in response:
        if eachkey in userQuestion:
            return response[eachkey]
        

    return "Right now , I am not able to tell you. I Am still analysing and learning"


# Take user input

while True:
    UserInput = input("please ask me something:")
    reply = getresponse_Bot (UserInput)
    print("Bot Response:", reply)

    if "bye" in UserInput.lower():
        break
