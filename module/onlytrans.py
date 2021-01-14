import os
from sys import exit
from googletrans import Translator as tt

class gotrans(object):
    col = ["\033[92m","\033[97m"]

    def __init__(self,prefix=[">>> ",">>> "]):
        print ("enter ':q' for exit \n")
        self.prefix = prefix
        while True:
              self.msg = input(f"{self.prefix[0]}")
              exit() if self.msg == ":q" else True
              self.resp = tt().translate(text=self.msg,dest='id')
              print (f"{self.prefix[1]}{self.col[0]}{self.resp.text}{self.col[1]}")
