def into_km(miles):
    return miles * 1.609

def into_miles(km):
    return km / 1.609

def into_fahren(celsius):
    return (celsius * 9/5) + 32

def into_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert():
    print("1. miles to km\n"
          "2. km to miles\n"
          "3. celsius to fahrenheit\n"
          "4. fahrenheit to celsius")
   
    choice = input("Select an option (1-4): ")
    
    if choice == "1":
        miles = float(input("Enter distance in miles: "))
        print(f"{miles} miles = {into_km(miles):.2f} kilometers")
        
    elif choice == "2":
        km = float(input("Enter distance in kilometers: "))
        print(f"{km} kilometers = {into_miles(km):.2f} miles")
        
    elif choice == "3":
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {into_fahren(celsius):.2f}°F")
        
    elif choice == "4":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F = {into_cel(fahrenheit):.2f}°C")
        
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    convert()
