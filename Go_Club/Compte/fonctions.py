import requests
from math import ceil


def get_players(username,password,client_id,client_secret,token,group_id):
    dico = {}
    data={"username":username, "password":password, "client_id":client_id, "client_secret": client_secret, "grant_type": "password","Authorization" : "Bearer " + token}
    nb_url = 'http://online-go.com/api/v1/groups/{}/members'.format(group_id)
    r = requests.post(nb_url,data)
   
    nb = ceil((r.json()['count']/10))+1
    
    for j in range(1,nb):
        url = 'http://online-go.com/api/v1/groups/{}/members?page={}'.format(group_id,j)
        response = requests.post(url,data)
        
        for i in range(len(response.json()['results'])):
            user = response.json()['results'][i]['user']['username']
            ranking = response.json()['results'][i]['user']['ranking']
            dico[user]= display_rank(ranking)
    return dico

def get_token(username,password,client_id,client_secret):
    r = requests.post('https://online-go.com/oauth2/token/', data={"username":username, "password":password, "client_id":client_id, "client_secret": client_secret, "grant_type": "password"})
    return r.json()['access_token']

def display_rank(rank_val): 
    if rank_val < 30: 
        return "%d Kyu" % (30-rank_val+1)
    else: 
        return "%d Dan" % ((rank_val-30+1))

def get_rank(username,password,client_id,client_secret,token,player):

    url = 'http://online-go.com/api/v1/players/'
    response = requests.post(url,data={"username":username, "password":password, "client_id":client_id, "client_secret": client_secret, "grant_type": "password","Authorization" : "Bearer " + token},params={'username':player})
    return display_rank(response.json()['results'][0]['ranking'])



def get_href(username,password,client_id,client_secret,token,player):

    url = 'http://online-go.com/api/v1/players/'
    response = requests.post(url,data={"username":username, "password":password, "client_id":client_id, "client_secret": client_secret, "grant_type": "password","Authorization" : "Bearer " + token},params={'username':player})
    id = response.json()['results'][0]['id']
   
    return  'https://online-go.com/player/{}/'.format(id)