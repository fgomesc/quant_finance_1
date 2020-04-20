import numpy as np
import math
import time

class OptionPricing:

    def __init__(self, S0, E, T, rf, sigma, interations):
        self.S0 = S0
        self.E = E
        self.T = T
        self.rf = rf
        self.sigma = sigma
        self.interations = interations


    def call_option_simulation(self):

        # We have 2 columns first with 0s the second columns will store the payoff
        # We need the first column of 0s: payoff function is max(0, S - E) for call option
        option_data = np.zeros([self.interations, 2])

        # Dimensions: 1 dimensional array with as many items as the itrations
        rand = np.random.normal(0, 1, [1, self.interations])

        # Equation for the S(t) stock price
        stock_price = self.S0 * np.exp(self.T * (self.rf - 0.5 * self.sigma ** 2) + self.sigma * np.sqrt(self.T) * rand)

        # We need S-E because we have to calculate the ma(S - E, 0)
        option_data[:, 1] = stock_price - self.E

        # avarage for the Monte-Carlo method
        # np.amax() returns the max(0, S - E) according to the formula
        avarage = np.sum(np.amax(option_data, axis=1)) / float(self.interations)

        # Have to use exp(-rt) discount factor
        return np.exp(-1.0 * self.rf * self.T) * avarage

    def put_option_simulation(self):
        # We have 2 columns first with 0s the second columns will store the payoff
        # We need the first column of 0s: payoff function is max(0, S - E) for call option
        option_data = np.zeros([self.interations, 2])

        # Dimensions: 1 dimensional array with as many items as the itrations
        rand = np.random.normal(0, 1, [1, self.interations])

        # Equation for the S(t) stock price
        stock_price = self.S0 * np.exp(self.T * (self.rf - 0.5 * self.sigma ** 2) + self.sigma * np.sqrt(self.T) * rand)

        # We need S-E because we have to calculate the ma(S - E, 0)
        option_data[:, 1] = self.E - stock_price

        # avarage for the Monte-Carlo method
        # np.amax() returns the max(0, S - E) according to the formula
        avarage = np.sum(np.amax(option_data, axis=1)) / float(self.interations)

        # Have to use exp(-rt) discount factor
        return np.exp(-1.0 * self.rf * self.T) * avarage

if __name__ == '__main__':

    S0 = 100                # Underlying stock price ar t = 0
    E = 100                 # Strike price
    T = 1                   # Expiry
    rf = 0.05               # risk-free rate
    sigma = 0.2             # Volatility of the underlying stock
    interations = 10000000  # number of interations in the Monte-Carlo simulation

    model = OptionPricing(S0, E, T, rf, sigma, interations)
    print('Call option price with Monte-Carlo approach', model.call_option_simulation())
    print('Put option price with Monte-Carlo approach', model.put_option_simulation())