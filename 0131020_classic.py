# Puzzle for January 31, 2020
# Calculate volumes of all polyhedrons
import math as m

def UserInput():
    while True:
        try:
            start = int(input("Number of Starting Sides: "))
            radius = float(input("Radial length of Isoscelese Triangle: "))
        except ValueError:
            print("One of your inputs isn't an appropriate number. Try again.")
            continue
        if start < 4:
            print("You have less than 4 sides so you can't create a polyhedron.")
            continue
        elif radius < 0:
            print("Your shape is a black hole. Try again.")
            continue
        else:
            break

    return start, radius

# find length of side c, given length a, b, and angle c
def law_cosines(a, b, rad_c):
    c = m.sqrt(a**2 + b**2 - 2*a*b*m.cos(rad_c))
    return(c)

# find length a, given isosceles trangle with congruent sides and angles b
def isos_law_sines(b, rad_b):
    rad_a = (m.pi - rad_b) / 2
    a = b * m.sin(rad_a) / m.sin(rad_b)
    return a

# calculate area of polygon given 3 sides of triangular elements and quantity
def calc_area(a, b, c, num_sides):
    s = (a + b + c) / 2
    area = m.sqrt(s * (s - a) * (s - b) * (s - c))
    area = area * num_sides
    return area

# calculate dimensions initial polygon. Returns length and interior angle radians
def calc_initial(init_sides, radius):
    # angle of triangle when flat
    deg_t = 360.0 / init_sides
    rad_t = deg_t * m.pi / 180
    # edge length of polygon
    side_length = law_cosines(radius, radius, rad_t)
    return side_length, rad_t

# calculate dimensions final polyhedron. Returns final radius, interior angle radians
# and final height
def calc_final(init_radius, fin_num_sides, side_length):
#    print(">>>> fin_num_sides: ", fin_num_sides)
#    print(">>>> side length: ", side_length)
    deg_t2 = 360.0 / fin_num_sides
#    print(">>>> final angle: ", deg_t2)
    rad_t2 = deg_t2 * m.pi / 180
#    print(">>>> final angle rad: ", rad_t2)
    fin_radius = isos_law_sines(side_length, rad_t2)
#    print(">>>> fin_radius: ", fin_radius)
    # height of new Triangle
    height = m.sqrt(init_radius**2 - fin_radius**2)
    return fin_radius, rad_t2, height

# calculate the Volumes
def calc_volumes(init_num_sides, init_radius, side_length):
    volumes = list(range(0,init_num_sides-3))
    for n in volumes:
#        print(">>>> n: ", n)
        fin_radius, fin_rad_theta, height = calc_final(init_radius, n+3, side_length)
        area = calc_area(fin_radius, fin_radius, side_length, n+3)
        vol = area * height
        volumes[n] = vol
    return volumes

Init_NumSides, Init_Radius = UserInput()
Side_Length, Init_Rad_Theta = calc_initial(Init_NumSides, Init_Radius)
Volumes = calc_volumes(Init_NumSides, Init_Radius, Side_Length)
print(Volumes)
