def cords(x, y):
    return (x, y) 

my_cords = {}

my_cords[cords(0, 0)] = "Home"
my_cords[cords(1, 1)] = "Work"
my_cords[cords(-1, -1)] = "School"

for i in my_cords:
    print(f"position: {i} name: {my_cords[i]}")