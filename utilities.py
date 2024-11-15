from __future__ import annotations

import string

import numpy as np

from country import Country, Location

import pathlib

def fileline_to_tuple(line):
    """Converts a line in a .csv file to a tuple of the lines comma seperated elements."""
    
    list_of_data = line.split(",")
    last_catagory = list_of_data[-1]
    last_data = last_catagory[:-1]
    list_of_data[-1] = last_data
    for i in range(len(list_of_data)):
        list_of_data[i] = list_of_data[i].strip()
    data_tuple = tuple(list_of_data)
    return data_tuple

def read_country_data(filepath):
    """Creates an instance of the 'Country' class using the 'Location' class data held in an external .csv file passed as a 'Path' object as the argument to this function."""
    data_file = open(filepath)
    num_lines = sum(1 for line in data_file)
    data_file.seek(0)
    headings_data = data_file.readline()
    tuple_of_headings = fileline_to_tuple(headings_data)

    #Mapping between the ordering of the headings in the location file to the ordering of arguments of the intialisation of a 'Location' object.
    #Example index_map = (2,1,4,5,3) meaning the data in the csv file is ordered 'region','locaiton','theta',','depot','r'.
    index_map = []
    ordered_headings = ("location", "region", "r", "theta", "depot")
    for catagory in ordered_headings:
        i=0
        for element in tuple_of_headings:
            if element == catagory:
                index_map.append(i)
            else:
                i +=1         
    index_map = tuple(index_map)
    
    #for each line, use readline, create a location object with parameters from that data.
    data_list_of_locations = []
    for line in range(1,num_lines):
        next_line = data_file.readline()
        next_data = fileline_to_tuple(next_line)
        if next_data[index_map[4]] == "True":
            bool_depot = True
        elif next_data[index_map[4]] == "False":
            bool_depot = False
        data_list_of_locations.append(Location(str(next_data[index_map[0]]),str(next_data[index_map[1]]),float(next_data[index_map[2]]),float(next_data[index_map[3]]),bool_depot))

    country_object = Country(data_list_of_locations)
    data_file.close()
    return country_object


def regular_n_gon(number_of_settlements: int) -> Country:
    """
    Returns a Country that has a single depot and number_of_settlements settlements.
    The settlements are arranged as the vertex points in a regular n-gon, each point
    of which is a distance 1.0 from the origin.

    The settlements are named alphabetically, starting from the settlement at the point
    (1.0, 0.0) and proceeding COUNTER-CLOCKWISE.
    Settlement names are generated as
        A, B, C, D, ... X, Y, Z, Za, Zb, Zc, ..., Zx, Zy, Zz, Zza, Zzb, ... etc.
    The depot at the origin is always named Origin. All settlements and the origin belong
    to a single region, named "Region".

    If you are still unsure about the arrangement of settlements within the Country that
    this function produces, we recommend you run the plot_country method on the output of
    this function for different input arguments. The assignment test also contains an
    illustration.

    SPECIAL CASES:
    - If the number of settlements is 0, there will be no settlements.
    - If the number of settlements is 1, a single settlement at (1.0, 0.0) will be placed.
    - If the number of settlements is 2, two settlements at (1.0, 0.0) and (1.0, pi) will be placed.

    Attention
    ---------
    You are not required to document or test THIS function, but you are welcome
    to use this function within your testing framework (to generate data, for example).
    Do not remove this function from your final submission.
    Do not make edits to this function.

    Parameters
    ----------
    number_of_settlement : int
        Number of settlement to be created

    Returns
    -------
    Country
        A Country that has a single depot and number_of_settlements settlements.
    """
    # Set region name
    region_name = "Region"
    # Origin is a depot
    origin = Location("Origin", region_name, 0.0, 0.0, True)

    if number_of_settlements == 0:
        settlements = []
    else:
        polar_angles = np.linspace(
            0.0, 2 * np.pi, endpoint=False, num=number_of_settlements
        )
        polar_angles[polar_angles > np.pi] -= 2 * np.pi

        settlements = [
            Location(
                (("z" * (i // 26)) + string.ascii_lowercase[i % 26]).capitalize(),
                region_name,
                1.0,
                theta,
                False,
            )
            for i, theta in enumerate(polar_angles)
        ]
    return Country(settlements + [origin])
