"""
Simple Interest Calculator = (P * R * T)/100
"""
P = float(input("Enter the principal p: "))
R = float(input("Enter the rate r: "))
T = float(input("Enter the Time t: "))

Simple_Interest = P * R * T/100
print("Simple Interest is ",round(Simple_Interest))