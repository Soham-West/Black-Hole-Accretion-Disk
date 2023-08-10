from constants import *
import math
import matplotlib as plt 

mass_solar_mass = 4100000
mass_grams = mass_solar_mass * 1.989 * (10 ** 33)

mass_acc_solarmass_year = 8 * (10 ** -5)
mass_acc_grams_second = (mass_acc_solarmass_year * 1.989 * (10 ** 33)) / 31536000

radius_schwarz = (2*G*mass_grams)/(c*c)
inner_acretion_disk = 3*radius_schwarz
outer_acretion_disk = 25*radius_schwarz

def find_temp_of_acretion(radius_from_center):
        return ((3 * G * mass_grams * mass_acc_grams_second)/(8 * math.pi * (radius_from_center ** 3) * sigma_sb)) ** (1/4)

temp_inner = find_temp_of_acretion(inner_acretion_disk)
temp_outer = find_temp_of_acretion(outer_acretion_disk)
average_acretion_temp = (temp_inner + temp_outer)/2

def find_spectral_radiance(temperature, frequency):
        first_part = (2 * plank_h * (frequency ** 3))/(c ** 2)
        second_part = 1/((math.e ** ((plank_h * frequency)/(k_b * temperature))) - 1)
        return first_part * second_part

