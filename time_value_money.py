from math import exp

def discrete_future_value(x, r, n):
    return x * (1 + r) ** n


def discrete_present_value(x, r, n):
    return x * (1 + r) ** - n

def continuous_future_value(x, r, t):
    return x * exp(r * t)

def continuous_present_value( x, r, t):
    return x * exp(-r * t)

if __name__ == '__main__':

    x = 100         # value of investiment in dollars
    r = 0.05        # interest rate
    n = 5           # years

    print('Future value of $100 in 5 years (discrete model):', discrete_future_value(x, r, n))
    print('Future value of $100 in 5 years (continuous model):', continuous_future_value(x, r, n))
    print('Present value of $100 in 5 years (discrete present):', discrete_present_value(x, r, n))
    print('Present value of $100 in 5 years (continuous mode):', continuous_present_value(x, r, n))