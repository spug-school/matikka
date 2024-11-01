import numpy as np


deg_list = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
rad_list = []

deg_rad_dict ={}

def deg_to_rads(deg):
    return deg * np.pi / 180

def rads_to_deg(rads):
    return rads * 180 / np.pi




if __name__ == '__main__':
    # Tehtävä 1

    print(rads_to_deg(2.493))
    print(rads_to_deg(0.911))

    print(deg_to_rads(137.7))
    print(deg_to_rads(62.3))

    for deg in deg_list:
        rad_list.append(deg_to_rads(deg))

    for i, j in zip(rad_list, deg_list):
        deg_rad_dict.update({j:i})

    for x in deg_rad_dict:
        print(x)
        print(deg_rad_dict[x])

    #tehtävä 2
    print("Lasketaan hypotenuusa")
    print(np.sqrt(1.6**2+2.3**2))