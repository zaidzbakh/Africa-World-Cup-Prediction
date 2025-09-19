from bs4 import BeautifulSoup
import requests
import pandas as pd

years =[
    1957, 1959, 1962, 1963, 1965, 1968, 1970, 1972, 1974, 1976, 1978, 
    1980, 1982, 1984, 1986, 1988, 1990, 1992, 1994, 1996, 1998, 2000, 
    2002, 2004, 2006, 2008, 2010, 2012, 2013, 2015, 2017, 2019, 2021, 2023
]  
#years where the africa cup were
# togo matches on 2010 were canceled also the match Ethiopia ,w/o, South Africa,1957 was a walk over 
def get_matches(year):

    link = f'https://en.wikipedia.org/wiki/{year}_Africa_Cup_of_Nations'
    response = requests.get(link)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    matches = soup.find_all('div', class_='footballbox')

    home = []
    score = []
    away = []

    for match in matches :
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        away.append(match.find('th', class_='faway').get_text())

    dict_football = {'home': home, 'score' : score, 'away' : away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    return df_football


fifa_africa = [get_matches(year) for year in years]
df_africa_cup_matches = pd.concat(fifa_africa, ignore_index = True)
df_africa_cup_matches.to_csv('Africa_cup_historical_matches.csv', index = False)


#fixture
df_prediction = get_matches(2025)
df_prediction.to_csv('Africa_Cup_2025_Fixture.csv', index = False)