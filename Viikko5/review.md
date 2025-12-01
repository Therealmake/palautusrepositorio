Copilot huomiot: 
This PR refactors the TennisGame class to improve code readability and maintainability through better variable naming, method extraction, and the use of class-level constants. The refactoring maintains all existing functionality while making the code cleaner and more modular.

Renamed variables from Hungarian notation (m_score1, m_score2) to more descriptive names (player1_score, player2_score)
Extracted complex get_score() logic into three focused helper methods: _equal_score(), _end_score(), and _score()
Introduced a class-level constant score_names to eliminate repetitive score-to-string conversions
Ei tehnyt mitään muutoehdotuksia, tai en ainakaan huomannut niitä.
