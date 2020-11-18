import argparse
import scrapping_basket.get_nba_csv as gc
import scrapping_basket.list_to_string as lts
import scrapping_basket.get_analysis as ga


def main(url):
    url = lts.listToString(url)
    gc.get_nba_csv(url)

    path = "/Users/Stephi/Documents/academic/UOC/tercer_semestre/tipologia/PRAC1/skobsar_jordiba90_prac1/output_csv/nba_stats.csv"
    csv = gc.get_data(path=path)
    ga.get_analysis(csv=csv)

def parse_args(parser):
    parser.add_argument('-url', '--url', nargs="+", help="URL of the basketball data you want to scrap", default=[])


if __name__ == "__main__":
    ###########
    parser = argparse.ArgumentParser(description='Basketball Automated Data Analysis')
    parse_args(parser)
    args = parser.parse_args()
    ###########
    #url_nba_data = "https://www.basketball-reference.com/leagues/NBA_2019_per_game.html"

    main(args.url)





