car_meter=float(input("Enter car meters travelled"))
car_hours=float(input("Enter hours"))
carmin=float(input("Enter min"))
carsec=float(input("Enter sec"))
timeseconds=(car_hours*3600)+(carmin*60)+carsec
kph=(car_meter/1000.0)/(timeseconds/3600.0)
mph=kph/1.609

print("Your speed is",mph)