"""Write a program that makes use of trigonometric functions available in math module."""

import math

angle_degrees = 45
angle_radians = math.radians(angle_degrees) #converts the angle from degrees to radian

sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)

calculated_rad = math.asin(sin_value)
calculated_deg = math.degrees(calculated_rad)

print(f'sin({angle_degrees}) is: {sin_value}')
print(f'cos({angle_degrees}) is : {cos_value}')
print(f'Arc sine back to degrees: {calculated_deg}')


