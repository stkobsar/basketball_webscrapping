def listToString(s):
    """
    Description: Need to build function because argparse function returns list, not string. Called from main.
    :param s: argparse output
    :return: string of url
    """
    # initialize an empty string
    url_string = ""

    # traverse in the string
    for ele in s:
        url_string += ele

        # return string
    return url_string



if __name__ == "__main__":

    url = 'https://www.basketball-reference.com/leagues/NBA_2019_per_game.html'
    result = listToString(url)

