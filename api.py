import requests
from pprint import pprint as pp
from datetime import date, datetime
import vk
import plotly
plotly.tools.set_credentials_file(username='EkaterinaVes', api_key='lYDN8kBhunhSshF1zrCk')
def get_friends(user_id, fields):
    """ Returns a list of user IDs or detailed information about a user's friends """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"
    domain = "https://api.vk.com/method"
    access_token = '861c2db3cb46c58dd69ee4779223146fbefc710e7ec15b2a37248fa6861fb3f9e5c95fc2eb02468a0c5b8'

    query_params = {
        'domain' : domain,
        'access_token': access_token,
        'user_id': user_id,
        'fields': 'bdate'
    }


    query = "{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v=5.53".format(**query_params)
    response = requests.get(query)
    m = response.json()
    return m
def main_element(lst):
    c = 0
    element = 0
    for n in range(len(lst)):
        c1 = 0
        for m in range(len(lst)):
            if lst[n] == lst[m]:
                c1 +=1
        if c1>c:
            c = c1
            element = n
    return lst[element]
def age_predict(user_id):
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    info = get_friends(user_id, 'bdate')
    count = info['response']['count']
    l_with_year = []
    l_with_data = []
    friends_list = info['response']['items']
    for i in range(count):
	    if 'bdate' in friends_list[i]: l_with_data.append(friends_list[i]['bdate'])
    for i in range(len(l_with_data)):
	    if len(l_with_data[i])>5 : l_with_year.append(l_with_data[i])
    for i in range(len(l_with_year)):
	    l_with_year[i] = int(l_with_year[i][-4:])
    birth = main_element(l_with_year)
    now = int(str(date.today())[:4])
    age = now - birth
    return age

def inf(user_id):
    session = vk.Session()
    api = vk.API(session)
    sp = api.users.get(user_ids=user_id, fields = 'first_name')
    name = sp[0]['first_name']
    return name
user_id = int(input('Введите ID пользователя: '))
print(inf(user_id), ': ', age_predict(user_id),)


dates=[]
def messages_get_history(peer_id, user_id, offset, count=200):
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    assert isinstance(offset, int), "offset must be positive integer"
    assert offset >= 0, "user_id must be positive integer"
    assert count >= 0, "user_id must be positive integer"
    domain = "https://api.vk.com/method"
    access_token = '861c2db3cb46c58dd69ee4779223146fbefc710e7ec15b2a37248fa6861fb3f9e5c95fc2eb02468a0c5b8'

    query_params = {
        'domain' : domain,
        'access_token' : access_token,
        'offset': offset,
        'count' : count,
        'user_id': user_id,
        'peer_id': peer_id,
        'rev' : 0

    }
    try:
        query = "{domain}/messages.getHistory?access_token={access_token}&offset={offset}&count={count}&user_id={user_id}&peer_id={peer_id}&rev=0&v=5.53".format(**query_params) 
        response = requests.get(query)
        m = response.json()
        r = len(m['response']['items'])
    except Exception:
        return dates
    else:
        for i in range(0,r):
            date = datetime.fromtimestamp(m['response']['items'][i]['date']).strftime("%Y-%m-%d")
            dates.append(date)
        offset += 200
        messages_get_history(peer_id, user_id, offset, count=200)
        return dates
dates = messages_get_history(145883808, 131539414, 0, 200)
def count_dates_from_messages(dates):
    dates_list = []
    frequency = []
    for n in range(len(dates)):
        if not dates[n] in dates_list: 
            dates_list.append(dates[n])
            c = 0
            for m in range(len(dates)):
                if dates[n] == dates[m]:
                    c +=1
            frequency.append(c)
    return dates_list, frequency

import plotly
plotly.tools.set_credentials_file(username='EkaterinaVes', api_key='YXuLANRS7ZA8lbFaGmm9')
import plotly.plotly as py
import plotly.graph_objs as go
def visual(dates_list,frequency):
    dates = []
    for i in range(len(dates_list)):
        stryear, strmonth, strday = dates_list[i].split('-')
        if strmonth[0] == '0': strmonth = strmonth[-1]
        year, month, day = int(stryear), int(strmonth), int(strday)
        date = datetime(year=year, month= month,day = day)
        dates.append(date)
    data = [go.Scatter(x=dates,y=frequency)]
    py.plot(data)
m = count_dates_from_messages(dates)[0]
g = count_dates_from_messages(dates)[1]
visual(m,g)