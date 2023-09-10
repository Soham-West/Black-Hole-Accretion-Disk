from functionsimportsvars import *


# Creating the x and y values of the plot
x_vals = np.array([i * (10 ** 13) for i in np.arange(10, 10**4, .1)])

#Creating a new function so that we can change the mass accretion rate
def new_find_temp_of_acretion(radius_from_center, m_as):
        return ((3 * G * bh_grams * m_as)/(8 * math.pi * (radius_from_center ** 3) * sigma_sb)) ** (1/4)

#Plotting the spectra for 10 different black holes
for r in range(1, 11):
        m_s = (10 ** 28) * (0.1* r) #Defining the new mass accretion rate
        y_vals = np.array([find_spectral_radiance(new_find_temp_of_acretion((12.5 * radius_schwarz) + 3 * radius_schwarz, m_s), i * (10 ** 14)) for i in np.arange(10, 10**4, .1)])
        #Plotting with the new mass accretion rates
        plt.plot(x_vals, y_vals, label = "mass acretion rate: " + str((10 ** 28) * (0.1* r)) + " grams/second")

#Using the trapz function to find the area under the curve which is the flux
y_vals2 = [find_spectral_radiance(find_temp_of_acretion(50 * (.25 * radius_schwarz) + 3 * radius_schwarz), i * (10 ** 13)) for i in np.arange(10, 10**4, .1)]
y = np.array(y_vals2)
flux = trapz(y, dx = .1)
print(flux)

#Plotting the grpah
plt.xscale("log")
plt.xlabel("Frequency(hertz)")
plt.ylabel("Spectral Radiance Intensity(Bv(t))")
plt.legend()
plt.show()