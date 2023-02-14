import os, time, requests, random
# from lib_1 import TOKEN

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
print("TOKEN: ", TOKEN) # github

CHAT_ID = -1001670463029 # twitch_clipz (от Самой Аманды) https://t.me/c/1670463029/22766 + -100
text_for_send = "человек слаб"

random_time_list1 = [5, 6, 7, 8]
random_time_list2 = [11, 12, 13, 14]
random_time_list3 = [18, 19, 20, 22, 23]
choice1 = random.choice(random_time_list1)
choice2 = random.choice(random_time_list2)
choice3 = random.choice(random_time_list3)

def Send_to_zazerkalie():
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text_for_send}")
    # responce = req.json() # print(responce)

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

if __name__ == '__main__':
    run()
