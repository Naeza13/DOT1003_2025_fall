ucret = input("Hourly wage: ")
saat = input("Hours worked: ")
gunn = input("Day of the week: ")

wage = float(ucret)
hour = float(saat)

maas = wage * hour

if gunn == "sunday":
    maas = (wage * 2) * hour

print(f"Daily wages: {int(maas)} liras")