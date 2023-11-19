from functionsimportsvars import *

frequency = (10 ** 15)
#Defining the width of each ring in cm
width_ring = ((outer_acretion_disk - inner_acretion_disk)//radius_schwarz + 1)/num_of_rings

#Defining the x-values(frequencies)
x_vals = np.array([i * frequency * plank_h for i in np.arange(10, 10**4, .1)])
x_vals_plots = [plank_h*x_val for x_val in x_vals]
#Creating sublpots to see how the observer angle changes spectra
fig, axs = plt.subplots(2)

#Creating 2 different angles 0 degrees and 90 degrees
for i in range(0, 2):
        #defining the angle for each plot
        angle = (math.pi/2)*i
        for t in range(1, 10): #plotting spectra for 10 rings
                distance_from_ring = 3 * radius_schwarz + .25 * width_ring * (t) * radius_schwarz
                observer_angle = 360/num_of_slices #Getting the azimuth angle of velocity
                angle_in_radians = math.radians(observer_angle) # Converting to radiancs
                y_vals = ([find_spectral_radiance(find_temp_of_acretion(outer_acretion_disk - inner_acretion_disk), i * frequency) for i in np.arange(10, 10**4, .1)])
                #Adding redshift factor and altitude angle factor to the y_vals(spectral radiance)
                y_val_ans = [abs((get_redshift(find_keplerian_velocity(distance_from_ring, bh_grams), t * frequency, optimal_angle_of_velocity(distance_from_ring, distance_from_center_to_observe_cm)) ** 4) * math.cos(angle) * x) for x in y_vals]
                axs[i].plot(x_vals, y_val_ans, label = "ring: " + str(i))



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
