from dataclasses import dataclass


@dataclass
class DataGamesResult:
    games_played: int
    players_winnings: dict
