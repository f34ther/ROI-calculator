# ROI = (current_value - cost_of_investment)/ cost_of_investment
# Income:Types(RentalIncome = 2,000/month, LaundryIncome,StorageIncome)
# Total month income= 2,000
# Purchase: 200,000
# expenses: tax, insurance, utilities = [electric, water, sewer, garbage, gas], HOA, lawn, vacancy, repairs, mortgage
# Total month expense: 1610
# CashFlow (income-expense): 390
# total monthly cashflow: 390
# Cash on Cash ROI: Down_payment+ Closing_costs+ rehab_budget+ misc = total investment
# ROI: 40,000 + 3,000 + 7,000 + 0 => 50,000 = initial investment
# annual cash flow= 390x12 = 4680
# ROI: 4680/50000 => ROI = 9.36

class ROI:
    def __init__(self, initial_investment, monthly_income, monthly_expense):
        self.initial_investment = initial_investment
        self.monthly_income = monthly_income
        self.monthly_expense = monthly_expense

    def net_percent(self):
        return f"{(((self.monthly_income-self.monthly_expense)*12)/self.initial_investment)*100} percent investment return"


beach = ROI(50000, 2000, 1000)

print(beach.net_percent())
