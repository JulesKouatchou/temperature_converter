'''
   Parameterizing a test
'''
import pytest
from functions.temperature_functions import *


@pytest.mark.parametrize("temperatureC, temperatureK", [(0, 273.5), (-3, 270.5), (10, 283.5), (26.5, 300.0)])
def test_convert_celsius_to_kelvin(temperatureC, temperatureK):
    assert convert_celsius_to_kelvin(temperatureC) == temperatureK

@pytest.mark.parametrize("temperatureC, temperatureF", [(0, 32.0), (-5, 23.0), (10, 50), (5, 41.0)])
def test_convert_celsius_to_fahrenheit(temperatureC, temperatureF):
    assert convert_celsius_to_fahrenheit(temperatureC) == temperatureF

@pytest.mark.parametrize("temperatureK, temperatureC", [(0, -273.5), (3.5, -270.0), (10, -263.5), (273.5, 0.0)])
def test_convert_kelvin_to_celsius(temperatureK, temperatureC):
    assert convert_kelvin_to_celsius(temperatureK) == temperatureC

@pytest.mark.parametrize("temperatureK, temperatureF", [(273.5, 32.0), (268.5, 23.0), (283.5, 50), (278.5, 41.0)])
def test_convert_kelvin_to_fahrenheit(temperatureK, temperatureF):
    assert convert_kelvin_to_fahrenheit(temperatureK) == temperatureF

@pytest.mark.parametrize("temperatureF, temperatureC", [(32.0, 0), (23.0, -5.0), (50, 10), (41.0, 5.0)])
def test_convert_fahrenheit_to_celsius(temperatureF, temperatureC):
    assert convert_fahrenheit_to_celsius(temperatureF) == temperatureC

@pytest.mark.parametrize("temperatureF, temperatureK", [(32.0, 273.5), (23.0, 268.5), (50.0, 283.5), (41.0, 278.5)])
def test_convert_fahrenheit_to_kelvin(temperatureF, temperatureK):
    assert convert_fahrenheit_to_kelvin(temperatureF) == temperatureK



