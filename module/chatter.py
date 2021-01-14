from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer as ct
from googletrans import Translator as tt


class chat(object):

    def __init__(self):
        print ("enter ':q' for exit \n")
        self.bot = ChatBot("My Bot")
        print("")

        while True:
            self.msg = input(">>> ")
            exit() if self.msg == ":q" else True
            self.response = self.bot.get_response(self.msg)
            self.id = tt().translate(text=self.response,dest='id',src="en").text
            print (">>>\033[92m",self.response,"\033[97m"+f"({self.id})")
