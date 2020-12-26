#!/usr/bin/env python3
################################################
# The purpose of this function is to calculate
# how close I am to retirement
################################################
# Imports
import math

################################################
# PORTFOLIO
################################################
# Equities
equity_tickers = ['MSFT', 'RTX', 'T', 'FB']
equity_amounts = [45, 82, 78, 3]

# Crypto
crypto_tickers = ['BTC', 'ETH', 'ADA']
crypto_amounts = [0.86383022, 13.22599726, 1650]

################################################
# DEFINES
################################################
CURRENT_AGE = 22
GOAL_AGE = 35 #age I want to retire at
GOAL_INCOME = 100000 #yearly income I want at retirement
RETIREMENT_AGE = 65 #national retirement age
AVERAGE_RETURNS = 0.07 #benchmark annual returns

################################################
# FUNCTIONS
################################################
def when_can_i_retire(principal):
    # Get time to goal & national retirement
    years_to_goal_age = GOAL_AGE - CURRENT_AGE
    years_to_national_age = RETIREMENT_AGE - CURRENT_AGE

    # GOAL
    average_compound = principal * ((1+AVERAGE_RETURNS)**years_to_goal_age)
    print("At an average annual growth rate of {}%, by age {} I will have ${}".format((AVERAGE_RETURNS*100), GOAL_AGE, average_compound))
    print("A 3% draw provides an annual income of ${}".format(average_compound * 0.03))
    print("A 4% draw provides an annual income of ${}".format(average_compound * 0.04))

    needed_principal_safe = GOAL_INCOME/0.03
    needed_principal_aggr = GOAL_INCOME/0.04
    print("I need ${} to have and annual income of ${} by drawing 3%".format(needed_principal_safe, GOAL_INCOME))
    print("I need ${} to have and annual income of ${} by drawing 4%".format(needed_principal_aggr, GOAL_INCOME))
   
    safe_growth_rate = 1 - math.exp(math.log((needed_principal_safe/principal), math.e)/years_to_goal_age)
    aggr_growth_rate = 1 - math.exp(math.log((needed_principal_aggr/principal), math.e)/years_to_goal_age)
    print("To get ${} in {} years, my ${}, must grow {}% annually".format(needed_principal_safe, years_to_goal_age, principal, safe_growth_rate))
    print("To get ${} in {} years, my ${}, must grow {}% annually".format(needed_principal_aggr, years_to_goal_age, principal, aggr_growth_rate)) 


    # NATIONAL
    national_compound = principal * ((1+AVERAGE_RETURNS)**years_to_national_age)
    print("At an average annual growth rate of {}%, by age {} I will have ${}".format(national_compound))
    print("A 3% draw provides an annual income of ${}".format(national_compound * 0.03))
    print("A 4% draw provides an annual income of ${}".format(national_compound * 0.04))

def get_crypto_principal(tickers, amounts):
    principal = 0
    return principal

def get_equity_principal(tickers, amounts):
    principal = 0
    return principal


if __name__ == "__main__":
    # Get principal of assets
    crypto_principal = get_crypto_principal(crypto_tickers, crypto_amounts)
    equity_principal = get_equity_principal(equity_tickers, equity_amounts)
    total_principal = crypto_principal + equity_principal

    # Do retirement
    #when_can_i_retire(total_principal)
    when_can_i_retire(41936)
