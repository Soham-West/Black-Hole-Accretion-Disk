from functionsimportsvars import *



# Creating the x and y values of the plot
x_vals = np.array([i * (10 ** 13) for i in np.arange(10, 10**4, .1)])


#Plotting the spectra for 10 different mass black holes
for r in range(1, 11):
        #Defining different masses for each black hole
        m = 2**r
        y_vals = np.array([find_spectral_radiance(find_temp_of_acretion((12.5 * m) + 3 * m), i * (10 ** 17)) for i in np.arange(10, 10**4, .1)])
        plt.plot(x_vals, y_vals, label = "mass: " + str(2**r) + " solar masses")

#Using the trapz function to find the area under the curve which is the flux
y_vals2 = [find_spectral_radiance(find_temp_of_acretion(50 * (.25 * radius_schwarz) + 3 * radius_schwarz), i * (10 ** 13)) for i in np.arange(10, 10**4, .1)]
y = np.array(y_vals2)
flux = trapz(y, dx = .1)
print(flux)

#Plotting the grpah
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Frequency(hertz)")
plt.ylabel("Spectral Radiance Intensity(Bv(t))")
plt.legend()
plt.show()