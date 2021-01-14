from sys import argv
from module.onlytrans import gotrans
from module.chatter import chat
from module.banner import banner,options,arg_list

def main():
    print (banner)
    try:
       if argv[1] not in arg_list:
          raise IndexError
       gotrans() if argv[1] == "translate" else False
       chat() if argv[1] == "training" else False
    except IndexError:
       return print (options)

if __name__=="__main__":
   main()
