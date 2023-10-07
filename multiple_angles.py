from functionsimportsvars import *
import random


frequecny = 10**15
# Creating the x values of the plot
x_vals = np.array([i * (frequecny) for i in np.arange(10, 10**4, .1)])

#Plotting the spectra for 7 different angles
for r in range(0, 6):
        #Changed radius calculations to constants for simplification
        observer_angle = r * 15 #creating the different angles
        angle_in_radians = (math.pi/180) * observer_angle #converting to radians
        y_vals = np.array([find_spectral_radiance(find_temp_of_acretion(outer_acretion_disk - inner_acretion_disk), i * frequecny) for i in np.arange(10, 10**4, .1)]) #Defining y values (spectral radiancs)
        y_vals_plot = [math.cos(angle_in_radians)*plank_h*y_val for y_val in y_vals]
        #Plotting with the added cos(angle) factor
        plt.plot(x_vals, y_vals_plot, label = "incliniation angle " + str(observer_angle) + " degrees") 

#Using the trapz function to find the area under the curve which is the flux
y_vals2 = [find_spectral_radiance(find_temp_of_acretion(outer_acretion_disk - inner_acretion_disk), i * frequecny) for i in np.arange(10, 10**4, .1)]
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