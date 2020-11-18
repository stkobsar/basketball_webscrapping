from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
import os


def get_data(path):
    path_absoluto = os.path.abspath(__file__)
    root_folder = os.path.dirname(os.path.dirname(path_absoluto))
    file1 = os.path.join(root_folder, path)
    return file1

file1 = get_data("output_csv/nbd_satats_2.csv")

def get_nba_csv(url, several = True):

        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        # use findALL() to get the column headers
        soup.findAll('tr', limit=2)

        # use getText()to extract the text we need into a list
        headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

        # exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
        headers = headers[1:]

        # avoid the first header row
        rows = soup.findAll('tr')[1:]
        player_stats = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]

        player_stats = [stats for stats in player_stats if set(stats)]


        stats = pd.DataFrame(player_stats, columns = headers)
        csv_file = stats.to_csv(f"/Users/Stephi/Documents/academic/UOC/tercer_semestre/tipologia/PRAC1/skobsar_jordiba90_prac1/output_csv/nba_stats.csv")






