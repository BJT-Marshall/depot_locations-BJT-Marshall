from __future__ import annotations

import numpy

import matplotlib

from typing import TYPE_CHECKING, List, Optional

from plotting_utilities import plot_country, plot_path

if TYPE_CHECKING:
    from pathlib import Path

    from matplotlib.figure import Figure


def travel_time(
    distance,
    different_regions,
    locations_in_dest_region,
    speed=4.75,
):
    """
    Computes the time taken to travel between two locations, seperated by 'distance' meters, travelling at 'speed' meters per second. 
    Taking into account delays due to interregional border control by the factor (1+('different_regions'*'locations_in_dest_region')/10).
    """
    #Function represents the equation 't = (D/3600S)(1+RN/10)'.
    #Note: 'speed' has a default value of 4.75 m/s.
    #Where D is 'distance' [m, float], S is 'speed' [m/s, float], R is 'different_regions' [N/A, bool] and N is 'locations_in_dest_region' [N/A, int].
    
    #If 'distance' or 'speed' are integer values, convert them into floats
    if type(distance) is int:
        distance = float(distance)
    if type(speed) is int:
        speed = float(speed)

    #Check input types
    if type(distance) is not float:
        print(type(distance))
        raise TypeError("'distance' should be a float or integer value.")
    if type(speed) is not float:
        raise TypeError("'speed' should be a float or integer value.")
    if type(different_regions) is not bool:
        raise TypeError("'different_regions' should he a boolean value.")
    if type(locations_in_dest_region) is not int:
        raise TypeError("'locations_in_dest_region' should be an integer value.")

    #Check input values
    if distance<0:
        raise ValueError("'distance' should be a positive value.")
    if distance==0 and different_regions is True:
        raise ValueError("If 'different regions' is True, then distance cannot be zero and visa versa.")
    if distance==0 and different_regions is False and locations_in_dest_region !=1:
        raise ValueError("If 'distance' is zero and 'different_regions' is false, then 'locations_in_dest_region' must be one.")
    if distance!=0 and different_regions is False and locations_in_dest_region ==1:
        raise ValueError("If 'locations_in_dest_region' is one and 'different_regions' is false, then 'distance' must be zero.")
    if distance==0 and different_regions is True and locations_in_dest_region ==1:
        raise ValueError("If 'distance' is zero and 'locations_in_dest_region' is one, then 'locations_in_dest_region' must be one.")    
    if speed<=0:
        raise ValueError("'speed' should be a positive, non-zero value for a finite time to be calculated.")
    if locations_in_dest_region<1:
        raise ValueError("'locations_in_dest_region' should be a positive value, greater than or equal to 1.")
    
    #Implementation of travel time function
    one_hour_distance = 3600*speed
    optimal_time = distance/(one_hour_distance)
    time=optimal_time*(1+(different_regions*locations_in_dest_region)/10)
    
    #Check the final value of 'time' is greater than or equal to zero and therefore a valid travel time
    if time<0:
        raise ValueError("'time' has returned as a negative value")
    
    return time


class Location:
    def __repr__(self):
        """
        Do not edit this function.
        You are NOT required to document or test this function.

        Not all methods of printing variable values delegate to the
        __str__ method. This implementation ensures that they do,
        so you don't have to worry about Locations not being formatted
        correctly due to these internal Python caveats.
        """
        return self.__str__()

    def __str__(self):
        raise NotImplementedError

    def distance_to(self, other):
        raise NotImplementedError


class Country:

    def travel_time(self, start_location, end_location):
        raise NotImplementedError

    def fastest_trip_from(
        self,
        current_location,
        potential_locations,
    ):
        raise NotImplementedError

    def nn_tour(self, starting_depot):
        raise NotImplementedError

    def best_depot_site(self, display):
        raise NotImplementedError

    def plot_country(
        self,
        distinguish_regions: bool = True,
        distinguish_depots: bool = True,
        location_names: bool = True,
        polar_projection: bool = True,
        save_to: Optional[Path | str] = None,
    ) -> Figure:
        """

        Plots the locations that make up the Country instance on a
        scale diagram, either displaying or saving the figure that is
        generated.

        Use the optional arguments to change the way the plot displays
        the information.

        Attention
        ---------
        You are NOT required to write tests or documentation for this
        function; and you are free to remove it from your final
        submission if you wish.

        You should remove this function from your submission if you
        choose to delete the plotting_utilities.py file.

        Parameters
        ----------
        distinguish_regions : bool, default: True
            If True, locations in different regions will use different
            marker colours.
        distinguish_depots bool, default: True
            If True, depot locations will be marked with crosses
            rather than circles.  Their labels will also be in
            CAPITALS, and underneath their markers, if not toggled
            off.
        location_names : bool, default: True
            If True, all locations will be annotated with their names.
        polar_projection : bool, default: True
            If True, the plot will display as a polar
            projection. Disable this if you would prefer the plot to
            be displayed in Cartesian (x,y) space.
        save_to : Path, str
            Providing a file name or path will result in the diagram
            being saved to that location. NOTE: This will suppress the
            display of the figure via matplotlib.
        """
        return plot_country(
            self,
            distinguish_regions=distinguish_regions,
            distinguish_depots=distinguish_depots,
            location_names=location_names,
            polar_projection=polar_projection,
            save_to=save_to,
        )

    def plot_path(
        self,
        path: List[Location],
        distinguish_regions: bool = True,
        distinguish_depots: bool = True,
        location_names: bool = True,
        polar_projection: bool = True,
        save_to: Optional[Path | str] = None,
    ) -> Figure:
        """
        Plots the path provided on top of a diagram of the country,
        in order to visualise the path.

        Use the optional arguments to change the way the plot displays
        the information. Refer to the plot_country method for an
        explanation of the optional arguments.

        Attention
        ---------
        You are NOT required to write tests or documentation for this
        function; and you are free to remove it from your final
        submission if you wish.

        You should remove this function from your submission if you
        choose to delete the plotting_utilities.py file.

        Parameters
        ----------
        path : list
            A list of Locations in the country, where consecutive
            pairs are taken to mean journeys from the earlier location to
            the following one.
        distinguish_regions : bool, default: True,
        distinguish_depots : bool, default: True,
        location_names : bool, default: True,
        polar_projection : bool, default: True,
        save_to : Path, str

        See Also
        --------
        self.plot_path for a detailed description of the parameters
        """
        return plot_path(
            self,
            path,
            distinguish_regions=distinguish_regions,
            distinguish_depots=distinguish_depots,
            location_names=location_names,
            polar_projection=polar_projection,
            save_to=save_to,
        )
