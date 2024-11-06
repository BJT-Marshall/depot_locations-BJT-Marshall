#Test file for functions from 'utilities.py' as well as the 'Location' and 'Country' classes.
#Tests are made using the pytest framework.
from pytest import raises
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

    #Test 'settlement' remains consitent with 'depot'

    l1.depot = False
    assert l1.settlement != l1.depot
    l2.depot = True
    assert l2.settlement != l2.depot