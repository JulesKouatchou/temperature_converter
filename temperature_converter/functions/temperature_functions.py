#!/usr/bin/env python

"""
   Module containing utility functions for converting temperatures
   from one unit to another. It has the following functions:

      - convert_celcius_to_kelvin
      - convert_celcius_to_fahrenheit
      - convert_kelvin_to_celcius
      - convert_kelvin_to_fahrenheit
      - convert_fahrenheit_to_celcius
      - convert_fahrenheit_to_kelvin
"""

# Local modules
from shared import constants
#import constants

#--------------------------------------------------------------------------

def convert_celcius_to_kelvin(temperatureC):
    """
       Convert temperature from Celcius to Kelvin.
       
       Parameters
       ----------
       temperatureC : float
            Temperature in degree Celcius

       Returns
       -------
       temperatureK : float
            Temperature in degree Kelvin
    """
    return temperatureC + constants.zeroCelcius

#--------------------------------------------------------------------------

def convert_celcius_to_fahrenheit(temperatureC):
    """
       Convert temperature from Celcius to Fahrenheit.

       Parameters
       ----------
       temperatureC : float
            Temperature in degree Celcius

       Returns
       -------
       temperatureF : float
            Temperature in degree Fahrenheit
    """
    return (9.0/5.0)*temperatureC + 32.0

#--------------------------------------------------------------------------

def convert_kelvin_to_celcius(temperatureK):
    """
       Convert temperature from Kelvin to Celcius.
       
       Parameters
       ----------
       temperatureK : float
            Temperature in degree Kelvin

       Returns
       -------
       temperatureC : float
            Temperature in degree Celcius
    """
    return temperatureK - constants.zeroCelcius

#--------------------------------------------------------------------------

def convert_kelvin_to_fahrenheit(temperatureK):
    """
       Convert temperature from Kelvin to Fahrenheit.

       Parameters
       ----------
       temperatureK : float
            Temperature in degree Kelvin

       Returns
       -------
       temperatureF : float
            Temperature in degree Fahrenheit
    """
    return (9.0/5.0)*(temperatureK - constants.zeroCelcius) + 32.0

#--------------------------------------------------------------------------

def convert_fahrenheit_to_celcius(temperatureF):
    """
       Convert temperature from Fahrenheit to Celcius.

       Parameters
       ----------
       temperatureF : float
            Temperature in degree Fahrenheit

       Returns
       -------
       temperatureC : float
            Temperature in degree Celcius
    """
    return (5.0/9.0)*(temperatureF - 32.0)

#--------------------------------------------------------------------------

def convert_fahrenheit_to_kelvin(temperatureF):
    """
       Convert temperature from Fahrenheit to Kelvin

       Parameters
       ----------
       temperatureF : float
            Temperature in degree Fahrenheit

       Returns
       -------
       temperatureK : float
            Temperature in degree Kelvin
    """
    return (5.0/9.0)*(temperatureF - 32.0) +  constants.zeroCelcius


#--------------------------------------------------------------------------

if __name__ == '__main__':
   print (convert_celcius_to_kelvin(15.7))
   print (convert_kelvin_to_celcius(302.9))
