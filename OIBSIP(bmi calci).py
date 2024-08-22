def calculate_bmi(weight, height):
    """Calculating BMI taking weight in kilograms and height in meters."""
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """Checking the BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        
        print("Your BMI is:",bmi)
        print("Category: ",category)
    except ValueError:
        print("Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()