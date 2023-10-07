from functionsimportsvars import *
import random


frequency = (10 ** 16)
# Creating the x and y values of the plot
x_vals = np.array([i * frequency for i in np.arange(10, 10**4, .1)])

#Plotting the spectra for 100 rings from inner to outer
for r in range(1, 15):
        #Finding the spectral radiance for each frequency
        #Changed radius calculations to constants for simplification
        y_vals = np.array([find_spectral_radiance(find_temp_of_acretion(r * (outer_acretion_disk - inner_acretion_disk)), i * frequency) for i in np.arange(10, 10**4, .1)])
        y_vals_plot = [plank_h*y_val for y_val in y_vals]
        plt.plot(x_vals, y_vals_plot, label = "ring " + str(r))


#Using the trapz function to find the area under the curve which is the flux
y_vals2 = [find_spectral_radiance(find_temp_of_acretion(outer_acretion_disk - inner_acretion_disk), i * frequency) for i in np.arange(10, 10**4, .1)]
y = np.array(y_vals2)
flux = trapz(y, dx = .1)
print(flux)

#Plotting the grpah
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Energy of photon(Ev)")
plt.ylabel("Spectral Radiance Intensity(Bv(t))")
plt.legend()
plt.show()