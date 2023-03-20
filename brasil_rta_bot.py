from urllib.request import urlopen

import tweepy
import json
import urllib.parse
import array as arr
import re
import time

api_key = "*****"
api_secret = "*****"
bearer_token = r"*****"
access_token = "*****"
access_token_secret = "*****"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)

api = tweepy.API(auth)

runs = []

def check_runs():

    #pega as runs mais recentes que foram verificadas no site
    url = "https://www.speedrun.com/api/v1/runs?status=verified&orderby=verify-date&direction=desc"

    response = urlopen(url)
    data_json = json.loads(response.read())

    all_runs = []

    for i in data_json['data']:

        with open('last_tweet.txt') as myfile:

            if (i['weblink']) not in myfile.read():

                sample_str = str (i['level'])

                if sample_str == 'None':

                    runs.append(i['weblink'])

                    url2 = i['players'][0]['uri']
                    urllib.parse.quote(url2)
                    response2 = urlopen(url2)
                    data_json = json.loads(response2.read())

                    if 'guests' not in url2:

                        #Evita de dar erro se o código do país for "None"
                        try:
                            if data_json['data']['location']['country']['code'] == 'br':

                                url3 = "https://www.speedrun.com/api/v1/games/"+i['game']
                                response3 = urlopen(url3)
                                data_json_game = json.loads(response3.read())

                                url4 = "https://www.speedrun.com/api/v1/categories/"+i['category']
                                response4 = urlopen(url4)
                                data_json_category = json.loads(response4.read())

                                values_ids = str(i['values'])
                                values_lenght = len(i['values'])

                                url5 = "https://www.speedrun.com/api/v1/categories/"+i['category']+"/variables?orderby=mandatory&direction=desc"
                                response5 = urlopen(url5)
                                data_json_variable = json.loads(response5.read())

                                url6 = "https://www.speedrun.com/api/v1/runs?status=verified&orderby=verify-date&direction=desc"
                                response6 = urlopen(url6)
                                data_json_user = json.loads(response6.read())

                                values = []

                                if values_lenght == 1:

                                    if data_json_variable['data'][0]['is-subcategory'] == True:

                                        if data_json_variable['data'][0]['id'] == values_ids[2:10]:
                                            random_value1 = values_ids[14:22]
                                            subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                if values_lenght == 2:

                                    if data_json_variable['data'][0]['is-subcategory'] == True:

                                        if data_json_variable['data'][0]['id'] == values_ids[2:10]:
                                            random_value1 = values_ids[14:22]
                                            subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                        if data_json_variable['data'][0]['id'] == values_ids[26:34]:
                                            random_value1 = values_ids[38:46]
                                            subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][1]['is-subcategory'] == True:

                                        if data_json_variable['data'][1]['id'] == values_ids[2:10]:
                                            random_value2 = values_ids[14:22]
                                            subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                        if data_json_variable['data'][1]['id'] == values_ids[26:34]:
                                            random_value2 = values_ids[38:46]
                                            subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                if values_lenght == 3:

                                    if data_json_variable['data'][0]['is-subcategory'] == True:

                                        if data_json_variable['data'][0]['id'] == values_ids[2:10]:
                                            random_value1 = values_ids[14:22]
                                            subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                        if data_json_variable['data'][0]['id'] == values_ids[26:34]:
                                            random_value1 = values_ids[38:46]
                                            subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                        if data_json_variable['data'][0]['id'] == values_ids[50:58]:
                                            random_value1 = values_ids[62:70]
                                            subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][1]['is-subcategory'] == True:

                                        if data_json_variable['data'][1]['id'] == values_ids[2:10]:
                                            random_value2 = values_ids[14:22]
                                            subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                        if data_json_variable['data'][1]['id'] == values_ids[26:34]:
                                            random_value2 = values_ids[38:46]
                                            subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                        if data_json_variable['data'][1]['id'] == values_ids[50:58]:
                                            random_value2 = values_ids[62:70]
                                            subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][2]['is-subcategory'] == True:

                                        if data_json_variable['data'][2]['id'] == values_ids[2:10]:
                                            random_value3 = values_ids[14:22]
                                            subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                        if data_json_variable['data'][2]['id'] == values_ids[26:34]:
                                            random_value3 = values_ids[38:46]
                                            subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                        if data_json_variable['data'][2]['id'] == values_ids[50:58]:
                                            random_value3 = values_ids[62:70]
                                            subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                if values_lenght == 4:

                                    if data_json_variable['data'][0]['id'] == values_ids[2:10]:
                                        random_value1 = values_ids[14:22]
                                        subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][0]['id'] == values_ids[26:34]:
                                        random_value1 = values_ids[38:46]
                                        subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][0]['id'] == values_ids[50:58]:
                                        random_value1 = values_ids[62:70]
                                        subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][0]['id'] == values_ids[74:82]:
                                        random_value1 = values_ids[86:94]
                                        subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][1]['id'] == values_ids[2:10]:
                                        random_value2 = values_ids[14:22]
                                        subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][1]['id'] == values_ids[26:34]:
                                        random_value2 = values_ids[38:46]
                                        subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][1]['id'] == values_ids[50:58]:
                                        random_value2 = values_ids[62:70]
                                        subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][1]['id'] == values_ids[74:82]:
                                        random_value2 = values_ids[86:94]
                                        subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][2]['id'] == values_ids[2:10]:
                                        random_value3 = values_ids[14:22]
                                        subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                    if data_json_variable['data'][2]['id'] == values_ids[26:34]:
                                        random_value3 = values_ids[38:46]
                                        subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                    if data_json_variable['data'][2]['id'] == values_ids[50:58]:
                                        random_value3 = values_ids[62:70]
                                        subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                    if data_json_variable['data'][2]['id'] == values_ids[74:82]:
                                        random_value3 = values_ids[86:94]
                                        subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                    if data_json_variable['data'][3]['id'] == values_ids[2:10]:
                                        random_value4 = values_ids[14:22]
                                        subcat4 = data_json_variable['data'][3]['values']['values'][random_value4]['label']

                                    if data_json_variable['data'][3]['id'] == values_ids[26:34]:
                                        random_value4 = values_ids[38:46]
                                        subcat4 = data_json_variable['data'][3]['values']['values'][random_value4]['label']

                                    if data_json_variable['data'][3]['id'] == values_ids[50:58]:
                                        random_value4 = values_ids[62:70]
                                        subcat4 = data_json_variable['data'][3]['values']['values'][random_value4]['label']

                                    if data_json_variable['data'][3]['id'] == values_ids[74:82]:
                                        random_value4 = values_ids[86:94]
                                        subcat4 = data_json_variable['data'][3]['values']['values'][random_value4]['label']

                                if values_lenght == 5:

                                    if data_json_variable['data'][0]['id'] == values_ids[2:10]:
                                        random_value1 = values_ids[14:22]
                                        subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][0]['id'] == values_ids[26:34]:
                                        random_value1 = values_ids[38:46]
                                        subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][0]['id'] == values_ids[50:58]:
                                        random_value1 = values_ids[62:70]
                                        subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][0]['id'] == values_ids[74:82]:
                                        random_value1 = values_ids[86:94]
                                        subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][0]['id'] == values_ids[98:106]:
                                        random_value1 = values_ids[110:118]
                                        subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][1]['id'] == values_ids[2:10]:
                                        random_value2 = values_ids[14:22]
                                        subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][1]['id'] == values_ids[26:34]:
                                        random_value2 = values_ids[38:46]
                                        subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][1]['id'] == values_ids[50:58]:
                                        random_value2 = values_ids[62:70]
                                        subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][1]['id'] == values_ids[74:82]:
                                        random_value2 = values_ids[86:94]
                                        subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][1]['id'] == values_ids[98:106]:
                                        random_value2 = values_ids[110:118]
                                        subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][2]['id'] == values_ids[2:10]:
                                        random_value3 = values_ids[14:22]
                                        subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                    if data_json_variable['data'][2]['id'] == values_ids[26:34]:
                                        random_value3 = values_ids[38:46]
                                        subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                    if data_json_variable['data'][2]['id'] == values_ids[50:58]:
                                        random_value3 = values_ids[62:70]
                                        subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                    if data_json_variable['data'][2]['id'] == values_ids[74:82]:
                                        random_value3 = values_ids[86:94]
                                        subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                    if data_json_variable['data'][2]['id'] == values_ids[98:106]:
                                        random_value3 = values_ids[110:118]
                                        subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                    if data_json_variable['data'][3]['id'] == values_ids[2:10]:
                                        random_value4 = values_ids[14:22]
                                        subcat4 = data_json_variable['data'][3]['values']['values'][random_value4]['label']

                                    if data_json_variable['data'][3]['id'] == values_ids[26:34]:
                                        random_value4 = values_ids[38:46]
                                        subcat4 = data_json_variable['data'][3]['values']['values'][random_value4]['label']

                                    if data_json_variable['data'][3]['id'] == values_ids[50:58]:
                                        random_value4 = values_ids[62:70]
                                        subcat4 = data_json_variable['data'][3]['values']['values'][random_value4]['label']

                                    if data_json_variable['data'][3]['id'] == values_ids[74:82]:
                                        random_value4 = values_ids[86:94]
                                        subcat4 = data_json_variable['data'][3]['values']['values'][random_value4]['label']

                                    if data_json_variable['data'][3]['id'] == values_ids[98:106]:
                                        random_value4 = values_ids[110:118]
                                        subcat4 = data_json_variable['data'][3]['values']['values'][random_value4]['label']

                                    if data_json_variable['data'][4]['id'] == values_ids[2:10]:
                                        random_value5 = values_ids[14:22]
                                        subcat5 = data_json_variable['data'][4]['values']['values'][random_value5]['label']

                                    if data_json_variable['data'][4]['id'] == values_ids[26:34]:
                                        random_value5 = values_ids[38:46]
                                        subcat5 = data_json_variable['data'][4]['values']['values'][random_value5]['label']

                                    if data_json_variable['data'][4]['id'] == values_ids[50:58]:
                                        random_value5 = values_ids[62:70]
                                        subcat5 = data_json_variable['data'][4]['values']['values'][random_value5]['label']

                                    if data_json_variable['data'][4]['id'] == values_ids[74:82]:
                                        random_value5 = values_ids[86:94]
                                        subcat5 = data_json_variable['data'][4]['values']['values'][random_value5]['label']

                                    if data_json_variable['data'][4]['id'] == values_ids[98:106]:
                                        random_value5 = values_ids[110:118]
                                        subcat5 = data_json_variable['data'][4]['values']['values'][random_value5]['label']

                                if values_lenght == 6:

                                    if data_json_variable['data'][0]['id'] == values_ids[2:10]:
                                        random_value1 = values_ids[14:22]
                                        subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][0]['id'] == values_ids[26:34]:
                                        random_value1 = values_ids[38:46]
                                        subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][0]['id'] == values_ids[50:58]:
                                        random_value1 = values_ids[62:70]
                                        subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][0]['id'] == values_ids[74:82]:
                                        random_value1 = values_ids[86:94]
                                        subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][0]['id'] == values_ids[98:106]:
                                        random_value1 = values_ids[110:118]
                                        subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][0]['id'] == values_ids[122:130]:
                                        random_value1 = values_ids[134:142]
                                        subcat1 = data_json_variable['data'][0]['values']['values'][random_value1]['label']

                                    if data_json_variable['data'][1]['id'] == values_ids[2:10]:
                                        random_value2 = values_ids[14:22]
                                        subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][1]['id'] == values_ids[26:34]:
                                        random_value2 = values_ids[38:46]
                                        subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][1]['id'] == values_ids[50:58]:
                                        random_value2 = values_ids[62:70]
                                        subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][1]['id'] == values_ids[74:82]:
                                        random_value2 = values_ids[86:94]
                                        subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][1]['id'] == values_ids[98:106]:
                                        random_value2 = values_ids[110:118]
                                        subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][1]['id'] == values_ids[122:130]:
                                        random_value2 = values_ids[134:142]
                                        subcat2 = data_json_variable['data'][1]['values']['values'][random_value2]['label']

                                    if data_json_variable['data'][2]['id'] == values_ids[2:10]:
                                        random_value3 = values_ids[14:22]
                                        subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                    if data_json_variable['data'][2]['id'] == values_ids[26:34]:
                                        random_value3 = values_ids[38:46]
                                        subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                    if data_json_variable['data'][2]['id'] == values_ids[50:58]:
                                        random_value3 = values_ids[62:70]
                                        subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                    if data_json_variable['data'][2]['id'] == values_ids[74:82]:
                                        random_value3 = values_ids[86:94]
                                        subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                    if data_json_variable['data'][2]['id'] == values_ids[98:106]:
                                        random_value3 = values_ids[110:118]
                                        subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                    if data_json_variable['data'][2]['id'] == values_ids[122:130]:
                                        random_value3 = values_ids[134:142]
                                        subcat3 = data_json_variable['data'][2]['values']['values'][random_value3]['label']

                                    if data_json_variable['data'][3]['id'] == values_ids[2:10]:
                                        random_value4 = values_ids[14:22]
                                        subcat4 = data_json_variable['data'][3]['values']['values'][random_value4]['label']

                                    if data_json_variable['data'][3]['id'] == values_ids[26:34]:
                                        random_value4 = values_ids[38:46]
                                        subcat4 = data_json_variable['data'][3]['values']['values'][random_value4]['label']

                                    if data_json_variable['data'][3]['id'] == values_ids[50:58]:
                                        random_value4 = values_ids[62:70]
                                        subcat4 = data_json_variable['data'][3]['values']['values'][random_value4]['label']

                                    if data_json_variable['data'][3]['id'] == values_ids[74:82]:
                                        random_value4 = values_ids[86:94]
                                        subcat4 = data_json_variable['data'][3]['values']['values'][random_value4]['label']

                                    if data_json_variable['data'][3]['id'] == values_ids[98:106]:
                                        random_value4 = values_ids[110:118]
                                        subcat4 = data_json_variable['data'][3]['values']['values'][random_value4]['label']

                                    if data_json_variable['data'][3]['id'] == values_ids[122:130]:
                                        random_value4 = values_ids[134:142]
                                        subcat4 = data_json_variable['data'][3]['values']['values'][random_value4]['label']

                                    if data_json_variable['data'][4]['id'] == values_ids[2:10]:
                                        random_value5 = values_ids[14:22]
                                        subcat5 = data_json_variable['data'][4]['values']['values'][random_value5]['label']

                                    if data_json_variable['data'][4]['id'] == values_ids[26:34]:
                                        random_value5 = values_ids[38:46]
                                        subcat5 = data_json_variable['data'][4]['values']['values'][random_value5]['label']

                                    if data_json_variable['data'][4]['id'] == values_ids[50:58]:
                                        random_value5 = values_ids[62:70]
                                        subcat5 = data_json_variable['data'][4]['values']['values'][random_value5]['label']

                                    if data_json_variable['data'][4]['id'] == values_ids[74:82]:
                                        random_value5 = values_ids[86:94]
                                        subcat5 = data_json_variable['data'][4]['values']['values'][random_value5]['label']

                                    if data_json_variable['data'][4]['id'] == values_ids[98:106]:
                                        random_value5 = values_ids[110:118]
                                        subcat5 = data_json_variable['data'][4]['values']['values'][random_value5]['label']

                                    if data_json_variable['data'][4]['id'] == values_ids[122:130]:
                                        random_value5 = values_ids[134:142]
                                        subcat5 = data_json_variable['data'][4]['values']['values'][random_value5]['label']

                                    if data_json_variable['data'][5]['id'] == values_ids[2:10]:
                                        random_value6 = values_ids[14:22]
                                        subcat6 = data_json_variable['data'][5]['values']['values'][random_value6]['label']

                                    if data_json_variable['data'][5]['id'] == values_ids[26:34]:
                                        random_value6 = values_ids[38:46]
                                        subcat6 = data_json_variable['data'][5]['values']['values'][random_value6]['label']

                                    if data_json_variable['data'][5]['id'] == values_ids[50:58]:
                                        random_value6 = values_ids[62:70]
                                        subcat6 = data_json_variable['data'][5]['values']['values'][random_value6]['label']

                                    if data_json_variable['data'][5]['id'] == values_ids[74:82]:
                                        random_value6 = values_ids[86:94]
                                        subcat6 = data_json_variable['data'][5]['values']['values'][random_value6]['label']

                                    if data_json_variable['data'][5]['id'] == values_ids[98:106]:
                                        random_value6 = values_ids[110:118]
                                        subcat6 = data_json_variable['data'][5]['values']['values'][random_value6]['label']

                                    if data_json_variable['data'][5]['id'] == values_ids[122:130]:
                                        random_value6 = values_ids[134:142]
                                        subcat6 = data_json_variable['data'][5]['values']['values'][random_value6]['label']

                                values_size = values_lenght

                                #verifica se a string tem . para milisegudos
                                def has_special_char(s):
                                    for c in s:
                                        if not (c.isalpha() or c.isdigit() or c == ' '):
                                            return True
                                    return False

                                s = i['times']['primary']

                                #Tempo em RTA e sem subcategoria
                                time_string = i['times']['primary']
                                temp = re.findall(r'\d+', time_string)
                                time_convert = list(map(int, temp))
                                time_size = len(time_convert)

                                if values_size == 0:

                                    values_convert = ''

                                if values_size == 1:

                                    if data_json_variable['data'][0]['is-subcategory'] == False:
                                        values_convert = ''

                                    if data_json_variable['data'][0]['is-subcategory'] == True:
                                        values_convert = ("["+subcat1+"]")

                                if values_size == 2:

                                    if data_json_variable['data'][0]['is-subcategory'] == True and data_json_variable['data'][1]['is-subcategory'] == False:
                                        values_convert = ("["+subcat1+"]")

                                    if data_json_variable['data'][0]['is-subcategory'] == False and data_json_variable['data'][1]['is-subcategory'] == True:
                                        values_convert = ("["+subcat2+"]")

                                    if data_json_variable['data'][0]['is-subcategory'] == True and data_json_variable['data'][1]['is-subcategory'] == True:
                                        values_convert = ("["+subcat1+"] "+"["+subcat2+"]")

                                    if data_json_variable['data'][0]['is-subcategory'] == False and data_json_variable['data'][1]['is-subcategory'] == False:
                                        values_convert = ''

                                if values_size == 3:

                                    if data_json_variable['data'][0]['is-subcategory'] == True:

                                        if data_json_variable['data'][1]['is-subcategory'] == True and data_json_variable['data'][2]['is-subcategory'] == False:
                                            values_convert = ("["+subcat1+"] "+"["+subcat2+"]")

                                        if data_json_variable['data'][1]['is-subcategory'] == False and data_json_variable['data'][2]['is-subcategory'] == True:
                                            values_convert = ("["+subcat1+"] "+"["+subcat3+"]")

                                        if data_json_variable['data'][1]['is-subcategory'] == True and data_json_variable['data'][2]['is-subcategory'] == True:
                                            values_convert = ("["+subcat1+"] "+"["+subcat2+"] "+"["+subcat3+"]")

                                        if data_json_variable['data'][1]['is-subcategory'] == False and data_json_variable['data'][2]['is-subcategory'] == False:
                                            values_convert = ("["+subcat1+"]")

                                    if data_json_variable['data'][0]['is-subcategory'] == False:

                                        if data_json_variable['data'][1]['is-subcategory'] == True and data_json_variable['data'][2]['is-subcategory'] == False:
                                            values_convert = ("["+subcat2+"]")

                                        if data_json_variable['data'][1]['is-subcategory'] == False and data_json_variable['data'][2]['is-subcategory'] == True:
                                            values_convert = ("["+subcat3+"]")

                                        if data_json_variable['data'][1]['is-subcategory'] == True and data_json_variable['data'][2]['is-subcategory'] == True:
                                            values_convert = ("["+subcat2+"] "+"["+subcat3+"]")

                                        if data_json_variable['data'][1]['is-subcategory'] == False and data_json_variable['data'][2]['is-subcategory'] == False:
                                            values_convert = ''

                                if values_size == 4:

                                    values_convert = ("["+subcat1+"] "+"["+subcat2+"] "+"["+subcat3+"] "+"["+subcat4+"]")

                                if values_size == 5:

                                    values_convert = ("["+subcat1+"] "+"["+subcat2+"] "+"["+subcat3+"] "+"["+subcat4+"] "+"["+subcat5+"]")

                                if values_size == 6:

                                    values_convert = ("["+subcat1+"] "+"["+subcat2+"] "+"["+subcat3+"] "+"["+subcat4+"] "+"["+subcat5+"] "+"["+subcat6+"]")

                                #Tempo em RTA e sem subcategoria e 1 objeto de tempo
                                if time_size == 1:

                                    time_convert_size = len(str(time_convert[0]))

                                    if has_special_char(s) == True:
                                        if time_convert_size == 3:
                                            time_run = ("0."+str(time_convert[0]))
                                            if i['times']['realtime_noloads']:
                                                print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                all_runs.append(run)
                                            if i['times']['ingame']:
                                                print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                all_runs.append(run)
                                            if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                all_runs.append(run)

                                        if time_convert_size == 2:
                                            time_run = ("0.0"+str(time_convert[0]))
                                            if i['times']['realtime_noloads']:
                                                print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                all_runs.append(run)
                                            if i['times']['ingame']:
                                                print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                all_runs.append(run)
                                            if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                all_runs.append(run)

                                        if time_convert_size == 1:
                                            time_run = ("0.00"+str(time_convert[0]))
                                            if i['times']['realtime_noloads']:
                                                print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                all_runs.append(run)
                                            if i['times']['ingame']:
                                                print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                all_runs.append(run)
                                            if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                all_runs.append(run)

                                    else:
                                        if time_convert_size == 2:
                                            time_run = ("0:"+str(time_convert[0]))
                                            if i['times']['realtime_noloads']:
                                                print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                all_runs.append(run)
                                            if i['times']['ingame']:
                                                print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                all_runs.append(run)
                                            if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                all_runs.append(run)

                                        if time_convert_size == 1:
                                            time_run = ("0:0"+str(time_convert[0]))
                                            if i['times']['realtime_noloads']:
                                                print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                all_runs.append(run)
                                            if i['times']['ingame']:
                                                print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                all_runs.append(run)
                                            if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                all_runs.append(run)

                                #Tempo em RTA e sem subcategoria e 2 objetos de tempo
                                if time_size == 2:

                                    time_convert_size = len(str(time_convert[1]))
                                    time_convert_size2 = len(str(time_convert[0]))

                                    #Se o primeiro objeto de tempo tiver 2 dígitos
                                    if time_convert_size2 == 2:

                                        if has_special_char(s) == True:
                                            if time_convert_size == 3:
                                                time_run = ("0:"+str(time_convert[0])+"."+str(time_convert[1]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 2:
                                                time_run = ("0:"+str(time_convert[0])+".0"+str(time_convert[1]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 1:
                                                time_run = ("0:"+str(time_convert[0])+".00"+str(time_convert[1]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                        else:
                                            if time_convert_size == 2:
                                                time_run = (str(time_convert[0])+":"+str(time_convert[1]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 1:
                                                time_run = (str(time_convert[0])+":"+"0"+str(time_convert[1]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                    #Se o primeiro objeto de tempo tiver 1 dígito
                                    if time_convert_size2 == 1:

                                        if has_special_char(s) == True:
                                            if time_convert_size == 3:
                                                time_run = ("0"+str(time_convert[0])+"."+str(time_convert[1]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 2:
                                                time_run = ("0"+str(time_convert[0])+".0"+str(time_convert[1]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 1:
                                                time_run = ("0"+str(time_convert[0])+".00"+str(time_convert[1]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                        else:
                                            if time_convert_size == 2:
                                                time_run = (str(time_convert[0])+":"+str(time_convert[1]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 1:
                                                time_run = (str(time_convert[0])+":0"+str(time_convert[1]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                #Tempo em RTA e sem subcategoria e 3 objetos de tempo
                                if time_size == 3:

                                    time_convert_size = len(str(time_convert[2]))
                                    time_convert_size2 = len(str(time_convert[1]))

                                    #Se o segundo objeto de tempo tiver 2 dígitos
                                    if time_convert_size2 == 2:

                                        if has_special_char(s) == True:
                                            if time_convert_size == 3:
                                                time_run = (str(time_convert[0])+":"+str(time_convert[1])+"."+str(time_convert[2]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 2:
                                                time_run = (str(time_convert[0])+":"+str(time_convert[1])+".0"+str(time_convert[2]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 1:
                                                time_run = (str(time_convert[0])+":"+str(time_convert[1])+".00"+str(time_convert[2]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                        else:
                                            if time_convert_size == 2:
                                                time_run = (str(time_convert[0])+":"+str(time_convert[1])+":"+str(time_convert[2]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 1:
                                                time_run = (str(time_convert[0])+":"+str(time_convert[1])+":0"+str(time_convert[2]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                    #Se o segundo objeto de tempo tiver 1 dígitos
                                    if time_convert_size2 == 1:

                                        if has_special_char(s) == True:
                                            if time_convert_size == 3:
                                                time_run = (str(time_convert[0])+":0"+str(time_convert[1])+"."+str(time_convert[2]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 2:
                                                time_run = (str(time_convert[0])+":0"+str(time_convert[1])+".0"+str(time_convert[2]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 1:
                                                time_run = (str(time_convert[0])+":0"+str(time_convert[1])+".00"+str(time_convert[2]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                        else:
                                            if time_convert_size == 2:
                                                time_run = (str(time_convert[0])+":0"+str(time_convert[1])+":"+str(time_convert[2]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 1:
                                                time_run = (str(time_convert[0])+":0"+str(time_convert[1])+":0"+str(time_convert[2]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                #Tempo em RTA e sem subcategoria e 4 objetos de tempo
                                if time_size == 4:

                                    time_convert_size = len(str(time_convert[3]))
                                    time_convert_size2 = len(str(time_convert[2]))
                                    time_convert_size3 = len(str(time_convert[1]))

                                    #Se o segundo objeto de tempo tiver 2 dígitos
                                    if time_convert_size3 == 2:
                                        #Se o terceiro objeto de tempo tiver 2 dígitos
                                        if time_convert_size2 == 2:
                                            if time_convert_size == 3:
                                                time_run = (str(time_convert[0])+":"+str(time_convert[1])+":"+str(time_convert[2])+"."+str(time_convert[3]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 2:
                                                time_run = (str(time_convert[0])+":"+str(time_convert[1])+":"+str(time_convert[2])+".0"+str(time_convert[3]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 1:
                                                time_run = (str(time_convert[0])+":"+str(time_convert[1])+":"+str(time_convert[2])+".00"+str(time_convert[3]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                        #Se o terceiro objeto de tempo tiver 1 dígito
                                        if time_convert_size2 == 1:
                                            if time_convert_size == 3:
                                                time_run = (str(time_convert[0])+":"+str(time_convert[1])+":0"+str(time_convert[2])+"."+str(time_convert[3]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 2:
                                                time_run = (str(time_convert[0])+":"+str(time_convert[1])+":0"+str(time_convert[2])+".0"+str(time_convert[3]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 1:
                                                time_run = (str(time_convert[0])+":"+str(time_convert[1])+":0"+str(time_convert[2])+".00"+str(time_convert[3]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                    #Se o segundo objeto de tempo tiver 1 dígito
                                    if time_convert_size3 == 1:
                                        #Se o terceiro objeto de tempo tiver 2 dígitos
                                        if time_convert_size2 == 2:
                                            if time_convert_size == 3:
                                                time_run = (str(time_convert[0])+":0"+str(time_convert[1])+":"+str(time_convert[2])+"."+str(time_convert[3]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 2:
                                                time_run = (str(time_convert[0])+":0"+str(time_convert[1])+":"+str(time_convert[2])+".0"+str(time_convert[3]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 1:
                                                time_run = (str(time_convert[0])+":0"+str(time_convert[1])+":"+str(time_convert[2])+".00"+str(time_convert[3]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                        #Se o terceiro objeto de tempo tiver 1 dígito
                                        if time_convert_size2 == 1:
                                            if time_convert_size == 3:
                                                time_run = (str(time_convert[0])+":0"+str(time_convert[1])+":0"+str(time_convert[2])+"."+str(time_convert[3]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 2:
                                                time_run = (str(time_convert[0])+":0"+str(time_convert[1])+":0"+str(time_convert[2])+".0"+str(time_convert[3]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                                            if time_convert_size == 1:
                                                time_run = (str(time_convert[0])+":0"+str(time_convert[1])+":0"+str(time_convert[2])+".00"+str(time_convert[3]))
                                                if i['times']['realtime_noloads']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(Real time no loads) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (Real time no loads) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"(IGT) por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" (IGT) por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)
                                                if not i['times']['realtime_noloads'] and not i['times']['ingame']:
                                                    print(data_json_game['data']['names']['international']+" -", data_json_category['data']['name'],values_convert,"em",time_run,"por "+data_json['data']['names']['international']+" "+i['weblink'])
                                                    run = (str(data_json_game['data']['names']['international'])+" - "+str(data_json_category['data']['name'])+" "+str(values_convert)+" em "+str(time_run)+" por "+str(data_json['data']['names']['international'])+" "+i['weblink'])
                                                    all_runs.append(run)

                        except TypeError as e:
                            pass
            else:
                time.sleep(15)
                print("Procurando novas runs...")

    print()

    with open(r'/home/BetoKos/last_run.txt', 'w') as fp:
        for item in all_runs:
            #Escreve cada item em uma linha nova
            fp.write("%s\n" % item)
        print('Done')

    with open(r'/home/BetoKos/last_tweet.txt', 'w') as fp:
        for item in runs:
            #Escreve cada item em uma linha nova
            fp.write("%s\n" % item)
        print('Check')

def post_run():
    
    names = []

    #Acessa o arquivo e lê o conteúdo em uma lista
    with open(r'/home/BetoKos/last_run.txt', 'r') as fp:
        for line in fp:
            #Remove a quebra de linha            
            x = line[:-1]

            #Adiciona o item atual na lista
            names.append(x)

    for item in names:
        client.create_tweet(text=item)
        print("Run postada...")
        print(item)

while True:
    try:
        check_runs()
        post_run()
        time.sleep(15)

    except TypeError as e:
        print(e)
        time.sleep(15)