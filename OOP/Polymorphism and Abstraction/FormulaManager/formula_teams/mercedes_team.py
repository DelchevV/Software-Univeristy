from FormulaManager.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos):
        petronas = [[1, 1_000_000], [3, 500_000]]
        teamviewer = [[5, 100_000], [7, 50_000]]
        revenue = 0

        for petro in petronas:
            pos, price = petro
            if pos >= race_pos:
                revenue += price
                break

        for teamv in teamviewer:
            pos, price = teamv
            if pos >= race_pos:
                revenue += price
                break

        revenue-=200_000

        self.budget += revenue
        return f"The revenue after the race is { revenue }$. Current budget { self.budget }$"
