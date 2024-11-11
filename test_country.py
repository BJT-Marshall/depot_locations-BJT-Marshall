#Test file for functions from 'utilities.py' as well as the 'Location' and 'Country' classes.
#Tests are made using the pytest framework.
from pytest import raises
import pytest
import numpy
import matplotlib


#--------------------------------------------------------------------------------------------------------------------------------------------------
#Testing travel_time
from country import travel_time
#Testing incorrect parameter type errors are thrown correctly
def test_travel_time_input_types():
    """Tests that each parameter has been passed as the correct type."""
    with raises(TypeError) as exception:
        travel_time(True,True,2)
    with raises(TypeError) as exception:
        travel_time(4,2,2)
    with raises(TypeError) as exception:
        travel_time(4,True,True)
    with raises(TypeError) as exception:
        travel_time(4,True,2,True)

#Testing incorrect parameter value errors are thrown correctly    
def test_travel_time_values():
    """Tests that each parameter has been passed a sensible value. i.e. that distance and time are positive values."""
    with raises(ValueError) as exception:
        travel_time(-4,True,2)
    with raises(ValueError) as exception:
        travel_time(0,True,2)
    with raises(ValueError) as exception:
        travel_time(0,False,2)
    with raises(ValueError) as exception:
        travel_time(4,False,1)
    with raises(ValueError) as exception:
        travel_time(0,True,1)
    with raises(ValueError) as exception:
        travel_time(4,True,2,0)
    with raises(ValueError) as exception:
        travel_time(4,True,2,-4)
    with raises(ValueError) as exception:
        travel_time(4,True,0)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Testing capitalisation_of_strings
from country import capitalisation_of_strings

def test_capitalisation_of_strings():
    assert capitalisation_of_strings("hello world") == "Hello World"
    assert capitalisation_of_strings("hello  world") == "Hello World"
    assert capitalisation_of_strings("hEllo WoRld") == "Hello World"
    assert capitalisation_of_strings(" hello wOrld ") == "Hello World"
    assert capitalisation_of_strings(" HelLo world   ") == "Hello World"
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Testing __init__ for the Location class
from country import Location

def test_Location___init__():
    """Tests that each attribute of a 'Location' object is of the correct type, and has been assigned a sensible value."""
    #Testing incorrect parameter type errors are passed correctly
    with raises(TypeError) as exception:
        l1 = Location(2,"Region",1,1,True)
    with raises(TypeError) as exception:
        l2 = Location("Name",2,1,1,True)
    with raises(TypeError) as exception:
        l3 = Location("Name","Region","int",1,True)
    with raises(TypeError) as exception:
        l4 = Location("Name","Region",1,"int",True)
    with raises(TypeError) as exception:
        l5 = Location("Name","Region",1,1,"true")
    
    #Testing incorrect parameter value errors are passed correctly 
    with raises(ValueError) as exception:
        l6 = Location("Name","Region",-4,1,True)
    with raises(ValueError) as exception:
        l7 = Location("Name","Region",1,5,True)
    
    #Testing numerical edge cases
    with raises(ValueError) as exception:
        l8 = Location("Name","Region",-0.0000001,1,True)
    with raises(ValueError) as exception:
        l9 = Location("Name","Region",1,numpy.pi+0.0000001,True)
    with raises(ValueError) as exception:
        l10 = Location("Name","Region",1,-numpy.pi-0.000001,True)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Testing the 'settlement' property and its helper function '_get_settlement'.
from country import Location
def test_settlement():
    """Tests that the 'settlement' property is assigned the correct value for an objects 'depot' attribute.
    Checks that the relation between the 'depot' attribute and the 'settlement' property remains consistent upon alteration of the 'depot' attribute."""
    l1 = Location("Name","Region",1,1,True)
    assert l1.settlement != l1.depot
    l2 = Location("Name","Region",1,1,False)
    assert l2.settlement != l2.depot

    #Tests 'settlement' remains consitent with 'depot'

    l1.depot = False
    assert l1.settlement != l1.depot
    l2.depot = True
    assert l2.settlement != l2.depot

    #Tests incorrect parameter type errors are thrown correctly
    l1.depot = 3
    with raises(TypeError) as exception:
        print(l1.settlement)

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Testing 'rounding_correction' function
from country import rounding_correction
def test_rounding_correction():
    """Tests that the 'rounding_correction' function returns correct values and raises paraneter type errors if the input is not a float."""
    #Testing type errors are raised correctly.
    with raises(TypeError) as exception:
        rounding_correction(True)
    with raises(TypeError) as excpetion:
        rounding_correction(4)
    with raises(TypeError) as exception:
        rounding_correction("string")
    #Testing that outputs returned are correct.

    assert rounding_correction(1.503) ==1.5
    assert rounding_correction(1.055) == 1.06
    assert rounding_correction(1.045) == 1.05
    assert rounding_correction(1.001) == 1.0

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#Testing the '__str__' method in the 'Location' class

def test_Location___str__():
    """Tests that the '__str__' method of the 'Location' class returns strings in the format desired."""
    test_theta = numpy.pi
    test_obj = Location("Name","Region",3,test_theta,True)
    assert str(test_obj) == "Name [depot] in Region @ (3.0m, 1.0pi)"
    test_obj.depot = False
    assert str(test_obj) == "Name [settlement] in Region @ (3.0m, 1.0pi)"

    #Testing that setting 'depot' to a non boolean value throws a type error
    test_obj.depot = 2
    with raises(TypeError) as exception:
        print(test_obj)
    test_obj.depot = False

    #Testing that the rounding of the attribute 'theta' is performed and displayed correctly in the output of the '__str__' method.

    test_obj.theta = 1.001*numpy.pi
    assert str(test_obj) == "Name [settlement] in Region @ (3.0m, 1.0pi)"

    test_obj.theta = 1.055*numpy.pi
    assert str(test_obj) == "Name [settlement] in Region @ (3.0m, 1.06pi)"

    test_obj.theta = 1.045*numpy.pi
    assert str(test_obj)== "Name [settlement] in Region @ (3.0m, 1.05pi)"

    test_obj.theta = 1.503*numpy.pi
    assert str(test_obj) == "Name [settlement] in Region @ (3.0m, 1.5pi)"

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#Testing the '__get_attributes_r_theta__' method.
def test___getattributes_r_theta__():
    """Testing the '__get_attributes_r_theta' getter method for the 'Location' class."""
    test_obj = Location("Name", "Region", 3,numpy.pi,True)
    assert test_obj.__getattributes_r_theta__() == (3,numpy.pi)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Testing the 'distance_to' method.
def test_distance_to():
    """Testing the 'distance_to' method of the 'Location' class."""
    test_obj = Location("Name", "Region", 3, 0, True)
    test_obj1 = Location("Name", "Region", 3, 0, True)
    
    #Testing that parameter type errors are thrown correctly.
    with raises(TypeError) as exception:
        test_obj.distance_to("string")

    #Testing that the method calculates the correct values.
    
    #Testing that parralel locations will return the difference in 'r' co-ordinates as their distance.
    assert test_obj.distance_to(test_obj1) == 0

    #Non-zero parralel distance case.
    test_obj.r = 5
    assert test_obj.distance_to(test_obj1) == 2

    #Equal non-zero 'theta' case.
    test_obj.theta = 2
    test_obj1.theta = 2
    assert test_obj.distance_to(test_obj1) == 2


    #Testing that the distance_to function is symettric. 
    assert test_obj.distance_to(test_obj1) == test_obj1.distance_to(test_obj)

    #Testing that two locations that form a right triangle with the polar origin have a distance as predicted by Pythagerous' Theorem.

    test_obj.r = 3
    test_obj.theta = 0
    test_obj1.r = 5
    test_obj1.theta = numpy.arcsin(numpy.sqrt(test_obj1.r**2 - test_obj.r**2)/test_obj1.r)

    assert test_obj.distance_to(test_obj1) == numpy.sqrt(test_obj1.r**2 - test_obj.r**2) #sqrt(5^2 - 3^2) = sqrt(16) = 4

    #Testing two locations with anti-parralel polar vectors (i.e. theta = 0, theta1 = numpy.pi)

    test_obj1.theta = numpy.pi

    assert test_obj.distance_to(test_obj1) == test_obj.r + test_obj1.r

    #Testing equilateral triangle case.

    test_obj.r = 3
    test_obj.theta = numpy.pi/6
    test_obj1.r = 3
    test_obj1.theta = -numpy.pi/6

    assert test_obj.distance_to(test_obj1) == pytest.approx(test_obj1.r,0.1)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Test the '__eq__' method from the 'Location' class.

def test___eq__():
    """Testing the '__eq__' method in the 'Location' class"""
    test_obj = Location("Name", "Region",3,3,True)
    
    #Testing that the other location parameter type error is thrown correctly.
    with raises(TypeError) as exception:
        test_obj == "String"

    test_obj1 = Location("Name", "Region1",3,3,True)
    test_obj2 = Location("Name", "Region",3,3,True)
    test_obj3 = Location("Name3", "Region3",3,3,True)
    test_obj4 = Location("Name4", "Region",3,3,True)

    assert (test_obj == test_obj1) is False
    assert (test_obj == test_obj2) is True
    assert (test_obj == test_obj3) is False
    assert (test_obj == test_obj4) is False

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
from country import Country

#Testing the initialisation method of the 'Country' class.

def test_Country___init__():
    """Testing the '__init__' method for the 'Country' class."""
    test_location1 = Location("Name", "Region", 3, 3, True)
    test_location2 = Location("Name2", "Region2", 3, 3, True)
    test_location3 = Location("Name3", "Region3", 3, 3, True)
    list1 = [test_location1, test_location2, test_location3]
    list2 = [test_location1, test_location2, test_location3,test_location1]

    #Testing that parmeter type errors are thrown correctly.
    with raises(TypeError) as exception:
        test_country = Country("string")
    
    #Testing that the '_all_locations' attribute is created correctly.
    test_country1 = Country(list1)
    assert test_country1._all_locations == (test_location1,test_location2,test_location3)

    #Testing the duplicated location error is thrown correctly.
    with raises(ValueError) as exception:
        test_country2 = Country(list2)

#------------------------------------------------------------------------------------------------------------------------------------------------------
from utilities import fileline_to_tuple
#Testing the 'fileline_to_tuple' function

def test_fileline_to_tuple():
    """Testing the 'fileline_to_tuple' function from the 'utilities.py' file."""

    #Testing that the parameter type error is thrown correctly.
    with raises(TypeError) as exception:
        fileline_to_tuple(6)

    assert fileline_to_tuple("Name, Region, r, theta, depot\n") == ("Name", "Region", "r", "theta", "depot")
    assert fileline_to_tuple("Name  , Region, r ,    theta, depot\n") == ("Name", "Region", "r", "theta", "depot")
    assert fileline_to_tuple("Name, Region\n") == ("Name", "Region")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
from utilities import read_country_data
import pathlib
#Testing the 'read_country_data' function from the 'utilities.py' file.

def test_read_country_data():
    """Testing the 'read_country_data' function from the 'utilities.py' file."""
    #Testing that the parameter type error is thrown correcttly.
    with raises(TypeError) as exception:
        read_country_data("string")

    #Testing the function produces the correct outputs    
    with raises(TypeError) as exception:
        locations_path = "locations.csv"
        data_obj=read_country_data(locations_path)
        assert str(data_obj._all_locations[0]) == "Darkwater Crossing [depot] in Eastmarch @ (125123.04863613259m, -0.09pi)"
        test_location_obj = Location("Darkwater Crossing", "Eastmarch", 125123.04863613259,-0.2748108313066159,True)
        assert data_obj._all_locations[0] == test_location_obj
    
#------------------------------------------------------------------------------------------------------------------------------------------------
#Testing the 'settlements' property of the 'Country' class.

def test_settlements():
    """Testing the 'settlements' property of the 'Country' class."""
    l1 = Location("Name", "Region", 1,1,True)
    l2 =Location("Name", "Region1",1,1,False)

    test_country = Country([l1,l2])

    #Testing that the 'settlements' property returns correctly.
    assert test_country.settlements == [l2]

    l2.depot = True
    assert test_country.settlements == []

    l1.depot = False
    l2.depot = False
    assert test_country.settlements == [l1,l2]

#--------------------------------------------------------------------------------------------------------------------------------------------
#Testing the 'depots' property of the 'Country' class.

def test_depots():
    """Testing the 'depots' property of the 'Country' class."""
    l1 = Location("Name", "Region", 1,1,True)
    l2 =Location("Name", "Region1",1,1,False)

    test_country = Country([l1,l2])

    #Testing that the 'settlements' property returns correctly.
    assert test_country.depots == [l1]

    l2.depot = True
    assert test_country.depots == [l1,l2]

    l1.depot = False
    l2.depot = False
    assert test_country.depots == []

#----------------------------------------------------------------------------------------------------------------------------------------------------
#Testing the 'n_settlements' property of the 'Country' class.

def test_n_settlements():
    """Testing the 'n_settlements' property of the 'Country' class."""
    l1 = Location("Name", "Region", 1,1,True)
    l2 =Location("Name", "Region1",1,1,False)
    test_country = Country([l1,l2])
    
    assert test_country.n_settlements == 1

    l1.depot = False
    assert test_country.n_settlements == 2

    l1.depot = True
    l2.depot = True
    assert test_country.n_settlements == 0

#----------------------------------------------------------------------------------------------------------------------------------------------------
#Testing the 'n_depots' property of the 'Country' class.

def test_n_depots():
    """Testing the 'n_settlements' property of the 'Country' class."""
    l1 = Location("Name", "Region", 1,1,True)
    l2 =Location("Name", "Region1",1,1,False)
    test_country = Country([l1,l2])
    
    assert test_country.n_depots == 1

    l1.depot = False
    assert test_country.n_depots == 0

    l1.depot = True
    l2.depot = True
    assert test_country.n_depots == 2

#----------------------------------------------------------------------------------------------------------------------------------------------------
#Testing the 'travel_time' method in the 'Country' class.
def test_travel_time():
    """Testing the 'travel_time' method in the 'Country' class."""
    l1 = Location("Name1","Region1",1,1,True)
    l2 = Location("Name2","Region2",1,1,False)
    c1 = Country([l1,l2])
    
    #Testing argument type errors are thrown correctly.
    with raises(TypeError) as exception:
        c1.travel_time(l1,3)
    with raises(TypeError) as exception:    
        c1.travel_time(3,l2)
    with raises(TypeError) as exception:
        c1.travel_time(3,3)
    
    l3 = Location("Name3","Region3",1,1,True)

    #Testing argument value errors are thrown correctly.
    with raises(ValueError) as exception:
        c1.travel_time(l1,l3)
    with raises(ValueError) as exception:
        c1.travel_time(l3,l2)

    #Test cases for 'travel_time'.
    l4 = Location("Name4","Region4",3,0,True)
    l5 = Location("Name5","Region4",3,numpy.pi,True)
    c2 = Country([l4,l5])
    assert c2.travel_time(l4,l5) == travel_time(6,False,2)

    #Test that the interregional delay factor is calculated correctly for travel_time
    l5.region = "Region5"
    c3 = Country([l4,l5])
    assert c3.travel_time(l4,l5) == travel_time(6,True,1)

    #Test if travel time returns zero when start_location = end_location
    assert c3.travel_time(l4,l4) == 0

#---------------------------------------------------------------------------------------------------------------------------------------------------
#Testing the 'fastest_trip_from' method of the 'Country' class.

def test_fastest_trip_from():

    l1 = Location("Name","Region",0,0,True)
    l2 = Location("Aname","Aregion",2,0,False)
    l3 = Location("Aname","Bregion",2,numpy.pi,False)
    l4 = Location("Bname","Aregion",2,0,False)
    l5 = Location("Bname","Bregion",4,0,False)
    c1 = Country([l1,l2,l3,l4,l5])
    l6 = Location("Name1","Region1",2,0,False)

    with raises(ValueError) as exception:
        c1.fastest_trip_from(l1,[l6])
    with raises(ValueError) as exception:
        c1.fastest_trip_from(l1, [l2,l6])

    with raises(ValueError) as exception:
        c1.fastest_trip_from(l1, [l2,3,2,8])
        c1.fastest_trip_from(l1, [l2,-1])

    #Testing the default arguments

    assert c1.fastest_trip_from(l1) == (l2,c1.travel_time(l1,l2))

    #Testing the optional argument

    assert c1.fastest_trip_from(l1,[]) == (None, None)
    #Test the tiebreaking

    assert c1.fastest_trip_from(l1, [l2]) == (l2,c1.travel_time(l1,l2))

    assert c1.fastest_trip_from(l1, [l2,l3]) == (l2,c1.travel_time(l1,l2))

    assert c1.fastest_trip_from(l1, [l2,l4]) ==  (l2,c1.travel_time(l1,l2))

    assert c1.fastest_trip_from(l1, [l2,l5]) ==  (l2,c1.travel_time(l1,l2))

