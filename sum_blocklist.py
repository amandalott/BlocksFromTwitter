#Code for counting blocked accounts by my profile

#    ATENSAOO 
#tem q criar um arquivo sum_blocklist.txt no mesmo diretorio q tá rodando esse
#pode ser vazio mas eh q eu não sabia criar ele direto pelo codigo fiquei preguiçakkkkk

import tweepy
import time
import json
from datetime import datetime
from pathlib import Path


#   ATENSAOR 2
# muda o que tá nesses auth e auth set token
# o twitter dev vai te fornecer as chave binitinho
auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("key", "secret")
api = tweepy.API(auth)

#sem arroba amigos não bote o arroba junto
to_check = input("Hey babes tell me just the username (@user_name) ")

print('Yo today we will be checking if')
print(to_check + ' followers are blocking u')
print('LEGGO')


# Creates variables for listing accounts
count = 0
users = tweepy.Cursor(api.friends, screen_name=to_check).items()


with open("sum_blocklist.txt") as json_file:
    data = json.load(json_file)

#fetches all followers
while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        time.sleep(60*15)
        user = next(users)
    except StopIteration:
        break

    # ATENSAO !!
    #Muda aqui o nome do seu perfil ali oh em source screen name se não vai buga tudo
    friendship = api.show_friendship(source_screen_name='YOUR PROFILE HERE', target_id=user.id)

    if friendship[0].blocked_by == True:
        print("Blocked by: @" + friendship[1].screen_name)
        data['blocks'].append(
            {'id':  friendship[1].id,
            'Name': friendship[1].screen_name,
            'Time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        count = count+1
        with open('sum_blocklist.txt', 'w') as outfile:
            json.dump(data, outfile)
    else:
        print(friendship[1].screen_name + " is not blocking you")

print("There are")
print("{} profiles blocking u".format(count))
