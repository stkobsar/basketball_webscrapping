##Classes for future implementation

def stats_player(name_player, data_df):
    condition = data_df["Player" == name_player]
    df_single_player = data_df[condition]


class Player():

    def __init__(self, three_shot, two_shot, one_shot):
        self.three_shot = three_shot
        self.two_shot = two_shot
        self.one_shot = one_shot