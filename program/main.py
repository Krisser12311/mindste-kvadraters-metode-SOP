from sympy import symbols, solve, Eq, diff
import matplotlib.pyplot as plt
import numpy as np 

def leastSquaresMethod(data_points):
    a, b = symbols('a b')
    sumA2 = 0 # Sum of a^2 
    sumB2 = 0 # Sum of b^2
    sumAB = 0 # Sum of 2ab
    sumA = 0 # Sum of 2ax
    sumB = 0 # Sum of 2by
    sumConstant = 0
    n = len(data_points) # Gets the number of data points

    for i in range(n): # Loops through all data points and calculates the sums
        x = data_points[i][0] # Gets the x value of the data point
        y = data_points[i][1] # Gets the y value of the data point
        print(f"Data point {i}: x = {x}, y = {y}") # Prints what data point is being calculated
        sumA2 += a**2 * x**2 # Adds the sum of a^2
        sumB2 += b**2      # Adds the sum of b^2
        sumAB += 2*a*b*x   # Adds the sum of 2ab
        sumA += 2*a*x*y   # Adds the sum of 2ax
        sumB += 2*b*y    # Adds the sum of 2by
        sumConstant += 2*y # Adds the sum of 2c

    # Defines the function of two variabel containing the sum of squared errors
    f = sumA2 + sumB2 + sumAB - sumA - sumB + sumConstant 

    # Solve for a and b
    diffA = diff(f, a) # Differentiates f to a
    diffB = diff(f, b) # Differentiates f to b
    solutions = solve([diffA, diffB], (a, b)) # Solves the equations
    return solutions[a], solutions[b] # Returns the solutions as a tuple containing a and b [a, b]

def main(dataPoints):
    line = leastSquaresMethod(dataPoints) # Calls the leastSquaresMethod function and stores the result in line
    slope = float(line[0])  # Gets the slope of the line
    intercept = float(line[1])  # Gets the intercept of the line
    
    for point in dataPoints: # Loops through all data points and plots them
        plt.plot(point[0], point[1], 'ro')
    
    # Defince x values for the line
    x = np.linspace(-10, 100, 100)  # Creates a interval of the line. The line will be drawn from -10 to 100
    y = slope * x + intercept # Calculates the y values for the line
    
    # Plot linjen
    plt.plot(x, y, label=f"y = {slope:.3f}x + {intercept:.3f}", color='blue') # Plots the line
    
    # Tilføj pile for at indikere forlængelse
    plt.quiver(x[0], y[0], -1, -slope, angles='xy', scale_units='xy', scale=1, color='blue', width=0.003) # Adds an arrow to the start of the line
    plt.quiver(x[-1], y[-1], 1, slope, angles='xy', scale_units='xy', scale=1, color='blue', width=0.003) # Adds an arrow to the end of the line
    
    # Akse og grid
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--') # Adds a horizontal line at y = 0
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--') # Adds a vertical line at x = 0
    plt.title('Mindste Kvadraters Metode med uendelig forlængelse') # Adds a title to the plot
    plt.xlabel('x - axis') # Adds a label to the x-axis
    plt.ylabel('y - axis') # Adds a label to the y-axis
    plt.legend() # Adds a legend to the plot
    plt.grid() # Adds a grid to the plot
    plt.show() # Shows the plot

dataPoints = [(1, 6), (5, 6), (6, 12), (10,10)]
main(dataPoints)