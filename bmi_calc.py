def BMI_calc(): #doctest needs work
    """Make a program that calcuates the BMI from user input."""
    w = input('\nWhat is your weight?')
    h = input('\nWhat is your height?')
    bmi = int(w)/int(h)
    print(f'Your BMI is {bmi}')
    
        
if __name__ == "__main__":
    BMI_calc()
