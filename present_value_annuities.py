import sys
'''
Present Value Annuities formula
PVA = PMT * (1 - (1 + r)**-n) / r  OR PMT * Present value factor
where: 
PVA = Present Value Annuities
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
    PAYMENT_PER_PERIOD =  float(input("Enter amount you wish to WITHDRAW PER PERIOD: "))
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


def present_value_factor(rate_per_period, periods):
    r = rate_per_period / 100 # convert % to decimal
    return (1 - (1 + r)**-periods) / r   # (1 - (1 + r)**-periods) / r

def rate_per_period(annual_rate, yearly_compounding_period):
    return annual_rate / yearly_compounding_period

def total_periods(yearly_compounding_period, duration): # duration in years
    return yearly_compounding_period * duration

def present_account_annuity(payment_per_period, factor):
    return payment_per_period * factor

# Annuity Due (Payment made at the begining of each period)
def present_value_due(rate_per_period, periods, payment_per_period):
    r = rate_per_period / 100 # convert % to decimal
    factor = 0
    periodic_payments = []
    for period in range(periods, 0, -1):
        factor = ((1 - (1 + r)**-period) / r ) * (1 + r)
        periodic_payments.append(payment_per_period * factor)
        factor = 0
    return periodic_payments

periodic_rate = rate_per_period(ANNUAL_INTEREST_RATE, COMPOUNDING_PERIOD)
periods = total_periods(COMPOUNDING_PERIOD, YEARS)
factor = present_value_factor(periodic_rate, periods)
present_account_total = present_account_annuity(PAYMENT_PER_PERIOD, factor)
interest = (PAYMENT_PER_PERIOD * periods) - present_account_total 

pvd = present_value_due(periodic_rate, periods, PAYMENT_PER_PERIOD) # Present value due factor
print()
print("__________________________________________")
print(f"Rate per period: {periodic_rate: .2f}% {compounding_freq[COMPOUNDING_PERIOD]}")
print(f"Total number of periods: {periods:,}")
print(f"Compounding factor: {factor: .4f}")
print(f"Present Value: N{present_account_total:,.2f}")
print(f"Interest gained: N{interest:,.2f}")
print("__________________________________________")
print()




for n in range(len(pvd)):
        print(f"Present value for period {n + 1}: N{pvd[n]:,.2f}")