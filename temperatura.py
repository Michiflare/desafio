def celsius_a_farenheit(celsius):
    return (celsius*9/5)+32

def celsius_a_kelvin(celsius):
    return celsius+273.15

if __name__=="__main__":
    celsius = 25
    farenheit= celsius_a_farenheit(celsius)
    print(f"{celsius} grados celsius equivalen a {farenheit} grados farenheit")