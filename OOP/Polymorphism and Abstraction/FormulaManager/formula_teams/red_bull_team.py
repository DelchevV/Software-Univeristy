from FormulaManager.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self,budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self,race_pos):
        oracle=[[1,1_500_000],[2,800_000]]
        honda=[[8,20_000],[10,10_000]]
        revenue=0

        for orac in oracle:
            pos, price=orac
            if pos>=race_pos:
                revenue+=price
                break

        for hond in honda:
            pos, price=hond
            if pos >= race_pos:
                revenue+=price
                break

        revenue-=250_000

        self.budget+=revenue
        return f"The revenue after the race is { revenue }$. Current budget { self.budget }$"


