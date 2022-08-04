
def liters_100km_to_miles_gallon(liters):
    galloni=liters/3.785411784
    miglia=100*1000/1609.344
    return miglia/galloni

def miles_gallon_to_liters_100km(miles):
    litri=3.785411784
    km=miles*1609.344/100/1000
    return litri/km


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
