from functionsimportsvars import *

def new_find_temp_of_acretion(radius_from_center, grams, mass_acc):
        return ((3 * G * grams * mass_acc)/(8 * math.pi * (radius_from_center ** 3) * sigma_sb)) ** (1/4)

def find_rad_diff(grams):
    r_s = (2*G*grams)/(c**2)
    return 25*r_s
x_vals = [1.0 * r for r in np.arange((bh_grams/10), bh_grams * (10**3), bh_grams/10)]
#Changed radius calculations to constants for simplification
y_vals = [new_find_temp_of_acretion(find_rad_diff(t),t, mass_acc_grams_second) for t in x_vals]
print(bh_grams)
print(mass_acc_grams_second)
print(mass_acc_solarmass_year)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("mass")
plt.ylabel("temperature(kelvins)")
plt.plot(x_vals, y_vals)
plt.show()
