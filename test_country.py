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



