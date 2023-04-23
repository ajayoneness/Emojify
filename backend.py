import random
emoji = ["😀", "😁", "😂", "🤣", "😃", "😄",
         "😅", "😆", "😇", "😉", "😊", "🙂",
         "🙃", "😋", "😌", "😍", "😘", "😗",
         "😙", "😚", "🤗", "🤔", "🤐", "🤢",
         "🤧", "🤕", "🤒", "😷", "🤥", "👻",
         "💩", "👽", "👾", "🤖", "🎃", "👑",
         "💍", "🌂", "🐶", "🐱", "🐭", "🐹",
         "🐰", "🦊", "🐻", "🐼", "🐨", "🐯",
         "🦁", "🐮", "🐷", "🐸","🐵", "🙈",
         "🙉", "🙊", "🐒", "🐔", "🐧", "🐦",
         "🐤", "🐣", "🐥", "🦆", "🦅", "🦉",
         "🦇", "🐺", "🐗", "🐴", "🦄", "🐝",
         "🐛", "🦋", "🐌", "🐞", "🐜", "🕷",
         "🦂", "🦀", "🐍", "🦎", "🦖", "🦕",
         "🐢", "🐠", "🐟", "🐡", "🦈", "🐬",
         "🐳", "🐋", "🦐", "🦑", "🐙", "🦞",
         "🦐", "🦑", "🦀", "🐚", "🦪", "🐌",
         "🦋", "🦟", "🦗"]

pic1 = random.choice(emoji)
pic2 = random.choice(emoji)

temp = 0
winner = 0

while True:
    temp = temp+1
    print(f"temp : {temp}")
    print(f'''
        choose Best One (Press 1 for pic1 and press 2 for Pic2)
        pic1 = {pic1}
        pic2 = {pic2}  
        ''')

    select = int(input("Select Best One -----> "))
    if temp == 10:
        print(winner)
        exit()

    elif select == 1:
        pic2 = random.choice(emoji)
        if pic1 == pic2:
            pic2 = random.choice(emoji)
        winner = f"Winner : {pic2}"

    elif select == 2:
        pic1 = random.choice(emoji)
        if pic2 == pic1:
            pic1 = random.choice(emoji)
        winner = f"Winner : {pic1}"

    elif select == 0:
        print("thankyou for Using 😍 ")
    else:
        print("Invalid Input")
        temp = temp-1