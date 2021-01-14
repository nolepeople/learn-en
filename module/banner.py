from json import loads

info = {
        "title":"Ayo belajar bahasa inggris!",
        "ig":"instagram : @aksiologikode",
        "opsi":"python3 main.py [options] \narguments: translate (en-id)\n           training (with chat a bot)\n",
        }

banner = f"\n{info['title']}\n{info['ig']}\n"
options = f"{info['opsi']}"
arg_list = ["translate","training","quests"]
