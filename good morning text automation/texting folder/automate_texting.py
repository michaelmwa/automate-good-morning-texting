import random, schedule, time

from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

GOOD_MORNING_QUOTES = [
    "Good Morning Love! Hope You Have An Amazing Day <3",
    "Good Morning Lovely! Hope you slept well <3",
    "Hope you have a great day today, my love!",
    "Love you so much, I know you will slay the day"
    "Good morning, my love. Do you remember any of your dreams?"
     "I wish I could have your period for you just once. Or, actually — no, I wish I could take it over forever. I’m sorry, baby. Have a good day."
"Good morning, baby. I thank God I’m alive to greet you with the sun."
"Good morning, baby. I know it’s raining outside, but my head is full of sunshine thinking about you."
]

GOOD_EVENING_QUOTES = [
    "Good Evening Love",
    "Sleep Tight My Love!",
    "Goodnight sweetie, dream about the beauty of our relationship!",
    "Love you! I hope you dream about me tonight <3"
   " I hope you have a great day today, baby. You deserve all the best the world has to offer."
  " Morning without you is a dwindled dawn."
]


def send_message(quotes_list=GOOD_MORNING_QUOTES):

    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]

    client.messages.create(to=cellphone,
                           from_=twilio_number,
                           body=quote
                           )


#  morning
schedule.every().day.at("11:11").do(send_message, GOOD_MORNING_QUOTES)

#  evening
schedule.every().day.at("20:00").do(send_message, GOOD_EVENING_QUOTES)

# test
schedule.every().day.at("13:55").do(send_message, GOOD_EVENING_QUOTES)

while True:

    schedule.run_pending()
    time.sleep(2)

