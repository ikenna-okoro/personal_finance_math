'''
Compound interest formula
A = (1 + r)**n
where: 
A = compoud factor (interest)
r = rate per period (as a decimal divided by 100)
n = number of periods
'''
PRINCIPAL =  float(input("Enter amount to deposit today: "))
YEARS = float(input("Enter number of years in future: "))
ANNUAL_INTEREST_RATE = float(input("Enter the annual interest rate (%): "))
COMPOUNDING_PERIOD = int(input("Enter the compounding period per year (number): "))
def compound_factor(rate_percent, periods):
    r = rate_percent / 100 # convert % to decimal
    return (1 + r) ** periods

def rate_per_period(annual_rate, yearly_compounding_period):
    return annual_rate / yearly_compounding_period

def total_periods(yearly_compounding_period, duration): # duration in years
    return yearly_compounding_period * duration

def future_account_bal(principal, factor):
    return principal * factor

periodic_rate = rate_per_period(ANNUAL_INTEREST_RATE, COMPOUNDING_PERIOD)
periods = total_periods(COMPOUNDING_PERIOD, YEARS)
factor = compound_factor(periodic_rate, periods)
future_account_total = future_account_bal(PRINCIPAL, factor)
interest = future_account_total - PRINCIPAL
print(f"Rate per period: {periodic_rate}%")
print(f"Total number of periods: {periods}")
print(f"Compounding factor: {factor: .4f}")
print(f"Future account Balance: ${future_account_total:.2f}")
print(f"Interest gained: ${interest:.2f}")