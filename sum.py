from functionsimportsvars import *

width_ring = ((outer_acretion_disk - inner_acretion_disk)//radius_schwarz + 1)/num_of_rings

total_lum = 0
lums = []
frequencys = []
for i in np.arange(10, 10**4, 1):
        frequency = i * (10 ** 13)
        for r in range(1, num_of_rings + 1):
                temp = find_temp_of_acretion(3 * radius_schwarz + width_ring * (r) * radius_schwarz)
                area_ring = math.pi * (((inner_acretion_disk + (r * width_ring * radius_schwarz)) ** 2) - ((inner_acretion_disk + ((r - 1) * width_ring * radius_schwarz)) ** 2))
                spectral_radiance = find_spectral_radiance(temp, frequency)
                total_lum += (area_ring * spectral_radiance)
        lums.append(total_lum)
        frequencys.append(frequency)
        total_lum = 0
                
                
plt.plot(frequencys, lums)
plt.xscale("log")
plt.yscale("linear")
plt.show()