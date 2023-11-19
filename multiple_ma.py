from functionsimportsvars import *

mass_acc = 10**28
frequency = 10 ** 17 
# Creating the x and y values of the plot
x_vals = np.array([i * frequency for i in np.arange(10, 10**4, .1)])
x_vals_plots = [plank_h * x_val for x_val in x_vals]
#Creating a new function so that we can change the mass accretion rate
def new_find_temp_of_acretion(radius_from_center, m_as):
        return ((3 * G * bh_grams * m_as)/(8 * math.pi * (radius_from_center ** 3) * sigma_sb)) ** (1/4)

#Plotting the spectra for 10 different black holes
for r in range(1, 11):
        m_s = (mass_acc * (0.1* r)) #Defining the new mass accretion rate
        #Changed radius calculations to constants for simplification
        y_vals = np.array([find_spectral_radiance(new_find_temp_of_acretion(outer_acretion_disk - inner_acretion_disk, m_s), i * frequency) for i in np.arange(10, 10**4, .1)])
        y_vals_plot = [plank_h * y_val for y_val in y_vals]
        #Plotting with the new mass accretion rates
        plt.plot(x_vals_plots, y_vals_plot, label = "mass acretion rate: " + str(mass_acc * (0.1* r)) + " grams/second")

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
plt.ylim(10**-24, 10**-14)
plt.tight_layout()
plt.show()