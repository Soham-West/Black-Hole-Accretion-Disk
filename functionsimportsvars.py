from constants import *
import math
import matplotlib.pyplot as plt 
import numpy as np
from scipy.integrate import simpson
from numpy import trapz
import csv

#Defining the mass of black hole in solar masses and grams
bh_solar_mass = 4100000 #This is for the Sigitarus A* which is in the center of the Milky Way
bh_grams = bh_solar_mass * 1.989 * (10 ** 33)

#Mass Accretion rate in solar masses/year and grams/second
mass_acc_solarmass_year = 8 * (10 ** -5)
mass_acc_grams_second = (mass_acc_solarmass_year * 1.989 * (10 ** 33)) / 31536000

#Defining the inner and outer radii of the acretion disk
radius_schwarz = (2*G*bh_grams)/(c*c)
inner_acretion_disk = 3*radius_schwarz
outer_acretion_disk = 28*radius_schwarz


#Function to find the temperature of the accretion ring given the radius from the center of the black hole
def find_temp_of_acretion(radius_from_center):
        return ((3 * G * bh_grams * mass_acc_grams_second)/(8 * math.pi * (radius_from_center ** 3) * sigma_sb)) ** (1/4)

#test for one ring
temp_inner = find_temp_of_acretion(inner_acretion_disk)
temp_outer = find_temp_of_acretion(outer_acretion_disk)
average_acretion_temp = (temp_inner + temp_outer)/2 
#end of lest for one ring

#Finding the spectral radiance of the accretion disk given the temperature and the frequency
def find_spectral_radiance(temperature, frequency):
        first_part = (2 * plank_h * (frequency ** 3))/(c ** 2)
        second_part = 1/((math.e ** ((plank_h * frequency)/(k_b * temperature))) - 1)
        return first_part * second_part

num_of_rings = 100