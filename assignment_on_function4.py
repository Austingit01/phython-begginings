def Temperatureconversion():
    Celcius = int(input("what is the temperature in Celcius? "))
    Farenheit = (Celcius * 9/5) + 32
    return Farenheit

Convert = Temperatureconversion()
print("Equals", Convert,"Farenheit")