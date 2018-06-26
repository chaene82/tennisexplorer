# -*- coding: utf-8 -*-

"""Main module."""
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime, timedelta, timezone
import pytz


timezone = pytz.timezone("Europe/Zurich")



def get_te_matchlist(year = '2018', month = '05', day = '07', match_type="atp-single"):
    """
    get a list if events on a given day
    
    """

    url = 'http://www.tennisexplorer.com/matches/?type=' + match_type + '&year' + year + '&month=' + month + '&day=' + day
    
    req = urllib.request.Request(url)
    #http://live-tennis.eu/en/official-atp-ranking
    response = urllib.request.urlopen(req)

    html = response.read()

    soup = BeautifulSoup(html, "html.parser")
    
    soup.unicode
    
    table = soup.find("table", attrs={"class": "result"})
    
    trs = table.findAll('tr')
    
    result = []
          
    for tr in trs :
        #print(row)

        
        ## searching for match link
        
        if 'bott' in tr['class'] :   
            match_link = tr.find("td", text="info").a.attrs['href'].strip()
            result.append(match_link)
            continue
        
    return result


def get_te_player(player_url = "/player/laaksonen/"):

    url = 'http://www.tennisexplorer.com/' + player_url 
    
    req = urllib.request.Request(url)
    #http://live-tennis.eu/en/official-atp-ranking
    response = urllib.request.urlopen(req)

    html = response.read()

    soup = BeautifulSoup(html, "html.parser")
    
    soup.unicode
    
    table = soup.find("table", attrs={"class": "plDetail"})
    
    if table is None:
        return pd.DataFrame()
    

    tds = table.findAll('td')
    #divs = tds[1].findAll('div')
    
    player_name =  tds[1].h3.text
    if  soup.find('div', text=re.compile(r'Country')):                   
        player_country = soup.find('div', text=re.compile(r'Country')).text.replace('Country: ', '')
    else :
        player_country = ""
    if  soup.find('div', text=re.compile(r'Born')) :
        player_dob =  soup.find('div', text=re.compile(r'Born')).text.replace('Born: ', '') 
    else :
        player_dob = ''
    player_sex =  soup.find('div', text=re.compile(r'Sex')).text.replace('Sex: ', '')
    if soup.find('div', text=re.compile(r'Plays')) :
        player_plays = soup.find('div', text=re.compile(r'Plays')).text.replace('Plays: ', '')
    else :
        player_plays = ''

                        

    
    result = pd.DataFrame()
    
    ## putting data together    
    dict = { 'player_name' : player_name,
             'player_country' : player_country,
             'player_dob' : player_dob,
             'player_sex' : player_sex, 
             'player_plays' : player_plays,
             'player_url' : player_url,
             'etl_date'   : datetime.now()
            }
       
    data = pd.DataFrame([dict])
        
    result = result.append(data, ignore_index=True) 
    
    
    return result