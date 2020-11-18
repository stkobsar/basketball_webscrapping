
# PRAC 1 asignatura tipología de datos, Master Degree Data Science, UOC. Semestre 1 curso 20/21. <h1> 

## Extracción de datos estadísticos sobre el rendimiento de los jugadores de la NBA para determinar las relaciones que hay entre las diferentes métricas, el rendimiento y las victorias de un equipo en una temporada. <h2>

## Initial hypothesis: Dispense with the medium distance shot can give more points, and therefore more games to a team? <h2>

Hipótesis inicial: ¿Prescindir del tiro de media distancia puede dar mas puntos, y por tanto más partidos a un equipo? <h4>

Extracción de la información en forma de csv <h4>

How to use: <h3>

**USE DATA FROM https://www.basketball-reference.com**
```
export PYTHONPATH=/path/to/your/machine/here

python scraping_basket/main.py -url "https://www.url_of_your_basketball_data_here.html"
open ouput_csv/nba_stats.csv
```

Example: <h3>

```
export PYTHONPATH=/Users/Stephi/Documents/academic/UOC/tercer_semestre/tipologia/PRAC1/skobsar_jordiba90_prac1
python scrapping_basket/main.py -url "https://www.basketball-reference.com/leagues/NBA_2019_per_game.html"
open ouput_csv/nba_stats.csv
```

Output csv description: <h3>

| Campo | Descripción |
| :---: |   :---:     |
| Player  | Name of the player |
| Pos  | Position of the player |
|Age| Age|
|Tm| Team|
|G| Games|
|GS| Games Started|
|MP| Minutes Played Per Game|
|FG| field goals per game|
|FGA| Field goals attempts per game|
|FG%| field goal %|
|3P'| 3 points fg per gam|
|3PA| 3 points attempts per game|
|3P%| 3 point %|
|2P'| 2 points fg per game|
|2PA| 2 points attempts per game|
|2P%'| 2 point %|
|eFG%  |Effective field goal % (This statistic adjusts for the fact that a 3-point field goal is worth one more point than a 2-point field goal.)|
|FT  | free throws per game|
|FTA  |free throws attempts per game|
|FT%  |free throws %|
|ORB  | offensive rebounds per game|
|DRB| defensive rebounds per game|
|TRB| total rebounds per game|
|AST| Assists per game|
|STL| Steals per game|
|BLK| blocks per game|
|TOV| turnovers per game|
|PF| Personal Fouls per game|
|PTS| points per game|

Preprocessing the data automation: <h3>

Automate generation of all variable histograms to preprocess the data: <h4>

- [X] Missing value treatment: eliminate blanck players
- [X] Treatment of the missing values as 0 values
- [X] Number of NaNs csv
```
open analysis/number_of_nans.csv 
```
- [X] Histogram of all variables in the dataset

Example to open the histogram showing the Age of the players in that year.
```
open analysis/Age.png 
```
- [X] Description of the data (count, mean, sd, min, 25%, 50%, 75%, min, max). See analysis file. 
```
open analysis/description_data.csv 
```
- [X] Type of variables in csv
```
open analysis/type_of_variables.csv 
```


# Current status and future prospects <h1>


- [X] Web Scrapping to extract the nba stats and convert it to a csv file
- [X] Preprocessing of data: Missing value treatment
- [X] Get first metrics 

- [ ] Answer the initial hypothesis relating the FG data off al players, then related it with the team data for a given year and correlate if a lower %2FG in mid distance throw turns in higher victories to a team in a season. 
- [ ] Unit testing


