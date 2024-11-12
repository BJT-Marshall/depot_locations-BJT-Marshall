from utilities import regular_n_gon
import timeit
from country import Country
import numpy
import matplotlib.pyplot as plt

#Plot t_exe on the y-axis, N_loc on the x-axis
#Format as i see fit
#Save the plot to a file called nna_excecution_times.png in the report subfolder

#The desired set of 'Number of settlements' used to test execution time.
N_locations_values = numpy.unique(numpy.logspace(0,9,base=2,num=75,dtype=int))

def create_countries(N_locs:list):
    """Creates a list of 'Country' objects using the 'regular_n_gon' function provided by 'utilities.py'.
    Each 'Country' object has a single depot and the number of settlements for the different 'Country' objects are given by the elements of the argument list."""
    countries = [regular_n_gon(number) for number in N_locs]
    return countries


def excecution_times(countries):
    """Computes the excecution time of the 'nn_tour' method (nearest-neighbor algorithm) of each 'Country' object that is an element of the argument list. Returns the list of these times."""
    times =[timeit.timeit(lambda: country.nn_tour(country.depots[0])) for country in countries]
    return times

def plot_nna_exec_times(times,n_locs):
    """Plots the excecution times, passed as the first argument, against the number of settlements, passed as the second argument. 
    Saves the resulting plot to the 'report/' subfolder as 'nna_excecution_times.png'."""
    fig, ax = plt.subplots()
    ax.plot(n_locs, times)
    plt.show()

plot_nna_exec_times(N_locations_values, excecution_times(create_countries(N_locations_values)))