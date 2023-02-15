import os, time, requests, random
from lib_1 import * # в конце - поменять!!!

# import configparser
import json
from telethon import TelegramClient, events
# from telethon.errors import SessionPasswordNeededError

# from telethon.tl.functions.messages import (GetHistoryRequest)
# from telethon.tl.types import (
# PeerChannel
# )

# TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN") # print("TOKEN: ", TOKEN)

# CHAT_ID = -1001670463029 # work
CHAT_ID = -1001744761688 # test
text_for_send = "man is weak" # человек слаб

random_time_list1 = [5, 6, 7, 8]
random_time_list2 = [11, 12, 13, 14]
random_time_list3 = [18, 19, 20, 22, 23]
choice1 = random.choice(random_time_list1)
choice2 = random.choice(random_time_list2)
choice3 = random.choice(random_time_list3)

def Send_to_zazerkalie():
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text_for_send}")
    # responce = req.json() # print(responce)

# chat gpt
# def Get_text_of_last_message():
#     last_message = Bot.get_updates(offset=-1, limit=1, timeout=10)[0] 
#     print(last_message.message.text)

def run():
    while True:
        current_time = time.localtime()
        h, m, s = current_time.tm_hour, current_time.tm_min, current_time.tm_sec

        # task
        if (h == choice1 and m == 0 and s == 0):
            Send_to_zazerkalie()

        if (h == choice2 and m == 0 and s == 0):
            Send_to_zazerkalie()

        if (h == choice3 and m == 0 and s == 0):
            Send_to_zazerkalie()

        # test
        # if (h == 21 and m == 9 and s == 0):
            # Send_to_zazerkalie()

        time.sleep(1)


# Create the client and connect
# client = TelegramClient(username, api_id, api_hash)
# client.start()
# print("1 Client Created")



client = TelegramClient('kapec', API_ID, API_HASH).start(bot_token=TOKEN)

@client.on(events.NewMessage(chats=CHAT_ID))
async def normal_handler(event):

    # # a = event.message.to_dict()["date"]
    # id = event.message.to_dict()["id"]
    message = event.message.to_dict()["message"]
    if "миша" in message.lower():
        await event.reply('Но я не Миша!')

# @client.on(events.NewMessage(pattern="123"))
# @client.on(events.NewMessage(pattern="[М|м][И|и][Ш|ш][а|а]"))
# async def start (event):
    # await event.respond("456")
    # requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={4456}")
    # await event.reply('Но я не Миша!')
    
client.run_until_disconnected()

# if __name__ == '__main__':
    # run()
