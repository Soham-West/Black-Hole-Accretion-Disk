from functionsimportsvars import *
import random





width_ring = ((outer_acretion_disk - inner_acretion_disk)//radius_schwarz + 1)/num_of_rings
"""file = open("tempvsspectra", "w")
writer = csv.writer(file)
top_row = ["Ring Number ", "Temperature ", "Frequecny ", "Spectral Radiance ", "Flux"]
writer.writerow(top_row)
xval = 0
yval = 0
fig, axs = plt.subplots(4, 3)
for i in range(1, 13):
        while yval < 3:
                if xval < 4:
                        [xval, yval].plot()"""
x_vals = []
y_vals = []
for i in np.arange(10, 10**4, 10**3):
    frequency = i * (10 ** 13)           
    for t in range(1, num_of_rings + 1):
        distance_from_ring = 3 * radius_schwarz + width_ring * (t) * radius_schwarz
        for r in range(0, num_of_slices):
                observer_angle = 360/num_of_slices
                angle_in_radians = math.radians(observer_angle)
                x_vals.append(frequency)
                y_vals.append([find_spectral_radiance(find_temp_of_acretion((.25 * radius_schwarz) + 3 * radius_schwarz), frequency)])
                x_vals = []
                y_vals = []
                plt.plot(x_vals, get_redshift(find_keplerian_velocity(distance_from_ring, bh_grams), frequency, optimal_angle_of_velocity(distance_from_ring, distance_from_center_to_observe_cm)) * math.cos(angle_in_radians) * np.array(y_vals))


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