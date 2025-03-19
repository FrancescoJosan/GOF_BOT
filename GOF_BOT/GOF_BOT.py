import requests
import json
import schedule
import time

# Docs
# https://core.telegram.org/bots/API#sendpoll
# There you can find some info about what you need
# to set in parameters

while 2:
    def dopost():

	# Here you need to put the api key from botfather
	# "https://api.telegram.org/ API KEY /sendPoll"

        base_url = "https://api.telegram.org/API"
        parameters = {
            "chat_id": '-[PLACE HERE ID]',
            "question": 'Chi c\'è oggi per la missione o addestramento? Per le 21',
            "is_anonymous": False,
            "options": json.dumps(["Io", "Arrivo dopo", "No", "Forse"]),
        }
	    
        resp = requests.get(base_url, data=parameters)
        print(resp.text)

    # schedule.every(). SET THE DAY HERE .at('HOUR OF POST, IT DEPENDS OF TIME OF THE SERVER 
    # WHERE IS RUNNING, AND THE FORMAT IS 24H, Like below)').do(dopost)

    schedule.every().monday.at('12:00').do(dopost)
    schedule.every().thursday.at('12:00').do(dopost)

    #Debug, this can send every second a poll to help you to debug
    #schedule.every(1).seconds.do(dopost)

    while 1:
        schedule.run_pending()
        time.sleep(1)