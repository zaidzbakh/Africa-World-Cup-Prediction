from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Liste des années de la Coupe d'Afrique des Nations
years = [
    1957, 1959, 1962, 1963, 1965, 1968, 1970, 1972, 1974, 1976, 1978, 
    1980, 1982, 1984, 1986, 1988, 1990, 1992, 1994, 1996, 1998, 2000, 
    2002, 2004, 2006, 2008, 2010, 2012, 2013, 2015, 2017, 2019, 2021, 2023
]  

# Utilisation de webdriver-manager pour gérer ChromeDriver automatiquement
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def get_missing_data(year):
    web = f'https://en.wikipedia.org/wiki/{year}_Africa_Cup_of_Nations'  # Correction du lien pour la CAN
    driver.get(web)

    matches = driver.find_elements(by='xpath', value='//tr[@style="font-size:90%"]')

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find_element(by='xpath', value='./td[1]').text)
        score.append(match.find_element(by='xpath', value='./td[2]').text)
        away.append(match.find_element(by='xpath', value='./td[3]').text)

    dict_football = {'home': home, 'score': score, 'away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    time.sleep(2)
    return df_football

# Récupération des données pour toutes les années
can_data = [get_missing_data(year) for year in years]

# Fermeture du navigateur
driver.quit()

# Concatenation des données et sauvegarde en CSV
df_can = pd.concat(can_data, ignore_index=True)
df_can.to_csv("africa_cup_missing_data.csv", index=False)

print("Extraction terminée. Fichier CSV généré : africa_cup_missing_data.csv")
