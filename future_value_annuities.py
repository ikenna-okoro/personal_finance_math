import sys
'''
Future Value Annuities formula
FVA = PMT * (((1 + r)**n) - 1) / r  OR PMT * Future value factor
where: 
FVA = Future Value Annuities
PMT = Payment per period
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
    PAYMENT_PER_PERIOD =  float(input("Enter amount you wish to PAY PER PERIOD: "))
except Exception as e:
    print(e)
# balance += PAYMENT_PER_PERIOD
# print(f"balance: N{balance: ,.2f}")
try:
    YEARS = int(input("Enter number of years in future: "))
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


def future_value_factor(rate_per_period, periods):
    r = rate_per_period / 100 # convert % to decimal
    return (((1 + r) ** periods) - 1) / r

def rate_per_period(annual_rate, yearly_compounding_period):
    return annual_rate / yearly_compounding_period

def total_periods(yearly_compounding_period, duration): # duration in years
    return yearly_compounding_period * duration

def future_account_annuity(payment_per_period, factor):
    return payment_per_period * factor


# Annuity Due (Payment made at the begining of each period)
def future_value_due(rate_per_period, periods, payment_per_period):
    r = rate_per_period / 100 # convert % to decimal
    factor = 0
    periodic_payments = []
    for period in range(periods):
        factor = ((((1 + r) ** (period)) - 1) / r) * (1 + r)
        account = (payment_per_period * factor) + payment_per_period
        periodic_payments.append((payment_per_period * factor) + payment_per_period)
        factor = 0
    return periodic_payments




periodic_rate = rate_per_period(ANNUAL_INTEREST_RATE, COMPOUNDING_PERIOD)
periods = total_periods(COMPOUNDING_PERIOD, YEARS)
factor = future_value_factor(periodic_rate, periods)
future_account_total = future_account_annuity(PAYMENT_PER_PERIOD, factor)
interest = future_account_total - (PAYMENT_PER_PERIOD * periods)

fvd = future_value_due(periodic_rate, periods, PAYMENT_PER_PERIOD) # Future value due factor

print()
print("__________________________________________")
print(f"Rate per period: {periodic_rate: .2f}% {compounding_freq[COMPOUNDING_PERIOD]}")
print(f"Total number of periods: {periods:,}")
print(f"Compounding factor: {factor: .4f}")
print(f"Future Value: N{future_account_total:,.2f}")
print(f"Interest gained: N{interest:,.2f}")
print("__________________________________________")
print()
print(f"Payment made at the begining of each period: ")
# print(f"{fvd}")

for n in range(len(fvd)):
        print(f"Future value for period {n + 1}: N{fvd[n]:,.2f}")


