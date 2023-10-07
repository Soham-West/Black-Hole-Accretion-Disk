from functionsimportsvars import *

def new_find_temp_of_acretion(radius_from_center, grams, mass_acc):
        return ((3 * G * grams * mass_acc)/(8 * math.pi * (radius_from_center ** 3) * sigma_sb)) ** (1/4)

x_vals = [1.0 * r for r in np.arange((10**21), 10**28, 10**21)]
#Changed radius calculations to constants for simplification
y_vals = [new_find_temp_of_acretion(outer_acretion_disk - inner_acretion_disk,bh_grams, t) for t in x_vals]


plt.xscale("log")
plt.yscale("log")
plt.xlabel("mass accretion rate(grams/second)")
plt.ylabel("temperature(kelvins)")
plt.plot(x_vals, y_vals)
plt.show()
