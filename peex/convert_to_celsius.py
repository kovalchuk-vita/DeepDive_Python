"""
Write a Python program to convert temperature from Fahrenheit to Celsius degree.
"""
def convertion(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def main():
    while True:
        try:
            user_input = input("Enter temperature in Fahrenheit (or 'q' to exit): ")
            if user_input.lower() == 'q':
                break
            fahrenheit = float(user_input)
            celsius = convertion(fahrenheit)
            print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


main()

