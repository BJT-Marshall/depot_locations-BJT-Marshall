#Test file for functions from 'utilities.py' as well as the 'Location' and 'Country' classes.
#Tests are made using the pytest framework.
from pytest import raises
from country import travel_time
import numpy
import matplotlib


#Testing travel_time---------------------------------------------------------------------------------------------------------------------------------

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
   