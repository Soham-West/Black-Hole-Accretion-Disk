from functionsimportsvars import *
import random



# Creating the x values of the plot
x_vals = np.array([i * (10 ** 13) for i in np.arange(10, 10**4, .1)])

#Plotting the spectra for 7 different angles
for r in range(0, 7):
        y_vals = np.array([find_spectral_radiance(find_temp_of_acretion(r * (.25 * radius_schwarz) + 3 * radius_schwarz), i * (10 ** 13)) for i in np.arange(10, 10**4, .1)]) #Defining y values (spectral radiancs)
        observer_angle = r * 15 #creating the different angles
        angle_in_radians = (math.pi/180) * observer_angle #converting to radians
        #Plotting with the added cos(angle) factor
        plt.plot(x_vals, math.cos(angle_in_radians) * y_vals, label = "incliniation angle " + str(observer_angle) + " degrees") 

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