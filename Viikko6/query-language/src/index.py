from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or, QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    matcher = (
        query
        .oneOf(
            query.playsIn("PHI")
                 .hasAtLeast(10, "assists")
                 .hasFewerThan(10, "goals"),
            query.playsIn("EDM")
                 .hasAtLeast(50, "points")
        )
        .build()
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
