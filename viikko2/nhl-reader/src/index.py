from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

def select_option(console, prompt, options):
    console.print(prompt, style="bold white")
    options_str = "/".join(options)
    console.print(f"[magenta]{options_str}[/magenta]")
    choice = input("Input your choice (or type 'exit' to quit): ").upper()
    if choice == "EXIT":
        return None
    if choice not in options:
        console.print("Choice not in list!", style="red")
        console.print("")
        return select_option(console, prompt, options)
    return choice

def fetch_players_by_nationality(url, nationality):
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    return stats.top_scorers_by_nationality(nationality)

def display_player_stats(players, season, nationality):
    console = Console()
    table = Table(title=f"Top scorers of {nationality} season {season}", show_lines=True)
    table.add_column("name", style="cyan", justify="left")
    table.add_column("team", style="magenta", justify="center")
    table.add_column("goals", style="green", justify="center")
    table.add_column("assists", style="green", justify="center")
    table.add_column("points", style="green", justify="center")
    for player in players:
        points = player.goals + player.assists
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(points))
    console.print(table)

def main():
    console = Console()
    url_original = "https://studies.cs.helsinki.fi/nhlstats/"
    print("NHL statistics by nationality")
    print("")
    season = select_option(console, "Select season", ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"])
    if season is None:
        return 
    print("")
    while True:
        nationality = select_option(console, "Select nationality", ["AUT", "CZE", "AUS", "SWE", "GER", "DEN", "SUI", "SVK", "NOR", "RUS",
                                                                   "CAN", "LAT", "BLR", "SLO", "USA", "FIN", "GBR"])
        if nationality is None:
            break
        url = f"{url_original}/{season}/players"
        players = fetch_players_by_nationality(url, nationality)
        print("")
        display_player_stats(players, season, nationality)
        print("")

if __name__ == "__main__":
    main()
