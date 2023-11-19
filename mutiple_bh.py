from functionsimportsvars import *


frequency = (9**15)
# Creating the x and y values of the plot
x_vals = np.array([i * frequency for i in np.arange(10, 15**4, .1)])
x_vals_plots = [plank_h * x_val for x_val in x_vals]

#Plotting the spectra for 10 different mass black holes
for m_bh in range(1, 11):
        #Defining different masses for each black hole
        m = 2**m_bh
        #Changed radius calculations to constants for simplification
        y_vals = np.array([find_spectral_radiance(find_temp_of_acretion((12.5 * m)), i * frequency) for i in np.arange(10, 15**4, .1)])
        y_vals_plot = [plank_h * y_val for y_val in y_vals]
        plt.plot(x_vals_plots, y_vals_plot, label = "mass: " + str(2**m_bh) + " solar masses")


#Plotting the grpah
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Energy of photon(Ev)")
plt.ylabel("Spectral Radiance Intensity(Bv(t))")
plt.legend()
plt.show()