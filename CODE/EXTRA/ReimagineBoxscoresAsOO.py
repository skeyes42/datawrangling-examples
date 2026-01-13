# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: ReimagineBoxscoresAsOO.py
# DATE 2025-10-26
# DESCRIPTION: 
# This Python program uses object-oriented programming (OOP) 
# and data classes to structure basketball game data, moving 
# from a flat, table-based format (using pandas DataFrames) 
# into nested, interconnected objects (Player, Team, Game).

"""
NBA Boxscore Data - Object-Oriented Structure with Python
Using dataclasses and pandas for data manipulation
"""

from dataclasses import dataclass, field
from typing import List
from datetime import date
import pandas as pd


# Define Classes using dataclasses ----

@dataclass
class Player:
    """Represents a player's stats for one game"""
    player_id: str
    name: str
    minutes: float
    field_goals_made: int
    field_goals_attempted: int
    three_pointers_made: int
    three_pointers_attempted: int
    free_throws_made: int
    free_throws_attempted: int
    rebounds: int
    assists: int
    steals: int
    blocks: int
    turnovers: int
    points: int
    
    def __post_init__(self):
        """Validate data after initialization"""
        if self.minutes < 0:
            raise ValueError("minutes must be non-negative")
        if self.points < 0:
            raise ValueError("points must be non-negative")
    
    def __repr__(self):
        return f"Player({self.name}: {self.points} pts, {self.rebounds} reb, {self.assists} ast)"


@dataclass
class Team:
    """Represents a team's performance in one game"""
    team_id: str
    team_name: str
    players: List[Player] = field(default_factory=list)
    total_points: int = 0
    
    def __post_init__(self):
        """Calculate total points from players"""
        if self.players:
            self.total_points = sum(p.points for p in self.players)
    
    def __repr__(self):
        return f"Team({self.team_name}: {self.total_points} pts, {len(self.players)} players)"


@dataclass
class Game:
    """Represents a complete game with two teams"""
    game_id: str
    game_date: date
    home_team: Team
    away_team: Team
    home_score: int = 0
    away_score: int = 0
    
    def __post_init__(self):
        """Set scores from team totals"""
        self.home_score = self.home_team.total_points
        self.away_score = self.away_team.total_points
    
    def __repr__(self):
        return (f"Game({self.game_id} on {self.game_date}: "
                f"{self.home_team.team_name} {self.home_score} - "
                f"{self.away_team.team_name} {self.away_score})")


# Helper Functions ----

def create_game_from_boxscore(boxscore_df: pd.DataFrame, game_id: str) -> Game:
    """Convert flat boxscore DataFrame to OO structure"""
    game_data = boxscore_df[boxscore_df['game_id'] == game_id].copy()
    
    if game_data.empty:
        raise ValueError(f"No data found for game_id: {game_id}")
    
    # Get unique teams
    teams = game_data['team_id'].unique()
    if len(teams) != 2:
        raise ValueError("Game must have exactly 2 teams")
    
    def create_players(team_data: pd.DataFrame) -> List[Player]:
        """Create Player objects from team data"""
        players = []
        for _, row in team_data.iterrows():
            player = Player(
                player_id=row['player_id'],
                name=row['player_name'],
                minutes=float(row['minutes']),
                field_goals_made=int(row['field_goals_made']),
                field_goals_attempted=int(row['field_goals_attempted']),
                three_pointers_made=int(row['three_pointers_made']),
                three_pointers_attempted=int(row['three_pointers_attempted']),
                free_throws_made=int(row['free_throws_made']),
                free_throws_attempted=int(row['free_throws_attempted']),
                rebounds=int(row['rebounds']),
                assists=int(row['assists']),
                steals=int(row['steals']),
                blocks=int(row['blocks']),
                turnovers=int(row['turnovers']),
                points=int(row['points'])
            )
            players.append(player)
        return players
    
    # Create team objects
    team1_data = game_data[game_data['team_id'] == teams[0]]
    team2_data = game_data[game_data['team_id'] == teams[1]]
    
    team1_players = create_players(team1_data)
    team2_players = create_players(team2_data)
    
    team1 = Team(
        team_id=teams[0],
        team_name=team1_data['team_name'].iloc[0],
        players=team1_players
    )
    
    team2 = Team(
        team_id=teams[1],
        team_name=team2_data['team_name'].iloc[0],
        players=team2_players
    )
    
    # Determine home/away (assuming first team alphabetically is home)
    if team1.team_name < team2.team_name:
        home_team, away_team = team1, team2
    else:
        home_team, away_team = team2, team1
    
    # Create game object
    game = Game(
        game_id=game_id,
        game_date=pd.to_datetime(game_data['game_date'].iloc[0]).date(),
        home_team=home_team,
        away_team=away_team
    )
    
    return game


# Example: Create sample boxscore data ----
def create_sample_data() -> pd.DataFrame:
    """Create sample NBA boxscore data"""
    return pd.DataFrame({
        'game_id': ['G001'] * 10,
        'game_date': ['2024-11-07'] * 10,
        'team_id': ['LAL'] * 5 + ['GSW'] * 5,
        'team_name': ['Lakers'] * 5 + ['Warriors'] * 5,
        'player_id': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10'],
        'player_name': [
            'LeBron James', 'Anthony Davis', "D'Angelo Russell",
            'Rui Hachimura', 'Austin Reaves',
            'Stephen Curry', 'Klay Thompson', 'Draymond Green',
            'Andrew Wiggins', 'Chris Paul'
        ],
        'minutes': [36, 34, 28, 26, 24, 35, 32, 30, 28, 22],
        'field_goals_made': [10, 12, 6, 5, 4, 11, 8, 3, 6, 3],
        'field_goals_attempted': [20, 22, 14, 10, 9, 20, 16, 8, 13, 7],
        'three_pointers_made': [2, 0, 3, 2, 1, 5, 4, 1, 2, 2],
        'three_pointers_attempted': [6, 1, 8, 5, 4, 11, 10, 3, 6, 5],
        'free_throws_made': [4, 6, 2, 0, 3, 3, 2, 4, 0, 1],
        'free_throws_attempted': [5, 7, 2, 0, 4, 3, 2, 6, 0, 2],
        'rebounds': [8, 13, 3, 6, 4, 4, 5, 10, 6, 3],
        'assists': [9, 3, 6, 2, 5, 8, 3, 7, 2, 6],
        'steals': [2, 1, 1, 0, 2, 3, 1, 2, 1, 2],
        'blocks': [1, 3, 0, 1, 0, 0, 0, 2, 1, 0],
        'turnovers': [3, 2, 2, 1, 1, 2, 1, 3, 1, 2],
        'points': [26, 30, 17, 12, 12, 30, 22, 11, 14, 9]
    })


def main():
    """Main execution function"""
    # Create sample data and game object
    sample_boxscore = create_sample_data()
    game = create_game_from_boxscore(sample_boxscore, 'G001')
    
    # Display game information
    print("=== Game Summary ===")
    print(f"Game ID: {game.game_id}")
    print(f"Date: {game.game_date}")
    print(f"Final Score: {game.home_team.team_name} {game.home_score} - "
          f"{game.away_team.team_name} {game.away_score}\n")
    
    print(f"=== Home Team: {game.home_team.team_name} ===")
    for player in game.home_team.players:
        print(f"{player.name:<20}: {player.points:2d} pts, "
              f"{player.rebounds:2d} reb, {player.assists:2d} ast")
    
    print(f"\n=== Away Team: {game.away_team.team_name} ===")
    for player in game.away_team.players:
        print(f"{player.name:<20}: {player.points:2d} pts, "
              f"{player.rebounds:2d} reb, {player.assists:2d} ast")
    
    # Working with the OO structure using pandas-style operations
    print("\n=== Analysis Examples ===")
    
    # Top scorers in the game
    all_players = game.home_team.players + game.away_team.players
    players_df = pd.DataFrame([
        {'name': p.name, 'points': p.points} for p in all_players
    ])
    top_scorers = players_df.sort_values('points', ascending=False).head(3)
    
    print("\nTop 3 Scorers:")
    print(top_scorers.to_string(index=False))
    
    # Team shooting percentages
    home_fg_made = sum(p.field_goals_made for p in game.home_team.players)
    home_fg_attempted = sum(p.field_goals_attempted for p in game.home_team.players)
    home_fg_pct = home_fg_made / home_fg_attempted if home_fg_attempted > 0 else 0
    
    away_fg_made = sum(p.field_goals_made for p in game.away_team.players)
    away_fg_attempted = sum(p.field_goals_attempted for p in game.away_team.players)
    away_fg_pct = away_fg_made / away_fg_attempted if away_fg_attempted > 0 else 0
    
    print("\nTeam Shooting %:")
    print(f"{game.home_team.team_name}: {home_fg_pct * 100:.1f}%")
    print(f"{game.away_team.team_name}: {away_fg_pct * 100:.1f}%")


if __name__ == "__main__":
    main()