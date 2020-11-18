### Future implementations

def preprocessing_dataset(csv):

    df_nba = pd.read_csv(csv)

# 1 Query for player --> Player --> (1/2/3% numericos 1 jugador)  !!
# 2 Query for team --> Team --> for player in team: Query Player (numericos todos los jugadores, wins)
# 3 Visualization --> for team in teams --> Query Team --> numerico teams--> all teams (1,2,3, barplot)

