# Sample Python code to run the fit_black_box Python code relatively easily
import fit_black_box as bb
import math

# First, define the function you want to fit. Here it's a linear function.
# It is critical that the independant variable ("t") is first in the list of function variables.

def linear(t, m, b):
    return m*t + b

# Here's an exponential function where a is theta0 and b is tau

def expon(t, a, b, c):
    return a*bb.np.exp(-t/b)+c

def expon2(t, a, b):
    return a*bb.np.exp(-t/b)

def quadratic(t, a, b, c):
    return a*t**2 + b*t + c

def power(t, a, b):
    return a*t**b

filename="C:/Users/Pranav/Desktop/pendulum lab/data scrubbing v3/tau.txt"
x, y, xerr, yerr = bb.load_data(filename)

# This time, let's use every single possible option available to bb.plot_fit()

init_guess = (-0.5, 0, +0.5) # guess for the best fit parameters
font_size = 15
title = "Using Amplitude with Time to Calculate Tau"
xlabel = "Time (s)"
ylabel = "Amplitude (m)"
'''
bb.plot_fit(linear, x, y, xerr, yerr, font_size=font_size,
            xlabel=xlabel, ylabel=ylabel, title=title)
'''
'''
bb.plot_fit(power, x, y, xerr, yerr, font_size=font_size,
            xlabel=xlabel, ylabel=ylabel, title=title)
# bb.plot_fit(expon, x, y, xerr, yerr, font_size=font_size,
            #xlabel=xlabel, ylabel=ylabel, title=title, init_guess = (1,1,0.5))
# Now we make the plot, displayed on screen and saved in the directory, and print the best fit values
'''
bb.plot_fit(expon, x, y, xerr, yerr)
bb.plot_fit(expon2, x, y, xerr, yerr)
bb.plot_fit(quadratic, x, y, xerr, yerr, init_guess=init_guess, font_size=font_size,
            xlabel=xlabel, ylabel=ylabel, title=title)
bb.plot_fit(expon2, x, y, xerr, yerr, init_guess=(1,1), font_size=font_size,
            xlabel=xlabel, ylabel=ylabel, title=title)
'''

bb.plot_fit(expon, x, y, xerr, yerr, font_size=font_size,
            xlabel=xlabel, ylabel=ylabel, title=title)
# Note: for sinusoidal functions, guessing the period correctly with init_guess is critical

# Fit the same data with an exponential function

# bb.plot_fit(expon, x, y, xerr, yerr)
'''
