import sys
'''
Compound interest formula
A = (1 + r)**n
where: 
A = compoud factor (interest)
r = rate per period (as a decimal divided by 100)
n = number of periods
'''
compounding_freq = {
    1: "annually",
    2: "semi-annually",
    4: "quarterly",
    6: "bi-annually", # Every other month
    12: "monthly",
    24: "bi-monthly", # twice in a month
    26: "bi-weekly", # every other week
    52: "weekly",
    365: "daily"
}

INITIAL_BALANCE = 0
balance = INITIAL_BALANCE
print(f"Opening balance: N{balance: ,.2f}")
try:
    PRINCIPAL =  float(input("Enter amount to deposit today: "))
except Exception as e:
    print(e)
balance += PRINCIPAL
print(f"balance: N{balance: ,.2f}")
try:
    YEARS = float(input("Enter number of years in future: "))
except Exception as e:
    print(e)

try:
    ANNUAL_INTEREST_RATE = float(input("Enter the annual interest rate (%): "))
except Exception as e:
    print(e)

try:
    COMPOUNDING_PERIOD = int(input("Enter the compounding period per year (number): "))
except Exception as e:
    print(e)
    sys.exit(f"try again!")


if COMPOUNDING_PERIOD not in compounding_freq:
    raise Exception("Not acceptable compounding parameter")


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


print(f"Rate per period: {periodic_rate: .2f}%")
print(f"Total number of periods: {periods:,}")
print(f"Compounding factor: {factor: .4f}")
print(f"Future account Balance: N{future_account_total:,.2f}")
print(f"Interest gained: N{interest:,.2f}")
print()
print(f"{compounding_freq[COMPOUNDING_PERIOD]} interests")
print("__________________________________________")


# Calculate interest happening daily on account
aer = ANNUAL_INTEREST_RATE / 100

def compound_over_range(initial_balance, aer, start_day, end_day):
    balance = initial_balance
    daily_rate = ((1 + aer) ** (1/365)) - 1

    results = []

    for day in range(1, end_day + 1):
        interest = balance * daily_rate
        balance += interest

        if day >= start_day:
            results.append({
                "day": str(day),
                "interest": interest,
                "balance": balance
            })
    return results

print("Select period to check interests...")
start = int(input("from: "))
if start > periods:
    raise ValueError("start must less than number of periods.")
end = int(input("to: "))
if end > periods or end < start:
    raise ValueError("end value is greater than number of periods or less than start.")

data = compound_over_range(balance, aer, start, end)
formatted_data = {}
for d in data:
    for key, value in d.items():
        if isinstance(value, (int, float)):
            formatted_data[key] = f"N{value:,.2f}"
        else:
            formatted_data[key] = value
            
    print(formatted_data)


days = int(input("Enter number of days to calculate compounded balance: "))
def balance_at_day(initial_balance, aer, days):
    daily_rate = (1 + aer) ** (1/365) - 1
    return initial_balance * (1 + daily_rate) ** days
balance_today = balance_at_day(balance, aer, days)
print(f"Balance at day {days}: N{balance_today:,.2f}")

# Try to Calculate the number of days to achieve a target interest
def balance_for_interest(day_interest, aer):
    # daily_rate = (1 + aer) ** (1/365) - 1
    # return day_interest / daily_rate
    # TODO
    return NotImplementedError