print("Welcome to the tip calculator!\n")

bill = float(input("What was the total bill? £"))

tip_options = {"0":0.0, "10": 0.1, "12": 0.12, "15": 0.15}
tip_percentage = input("\nWhat percentage would you like to tip: 0, 10%, 12%, or 15%? ")

while tip_percentage not in tip_options:
    print("Invalid input! Please enter 0, 10, 12, or 15.")
    tip_percentage = input("\nWhat percentage would you like to tip: 0, 10%, 12%, or 15%? ")

ppl = int(input("\nHow many people are splitting the bill? "))

tip = tip_options[tip_percentage]
total_bill = bill + (tip * bill)
split = total_bill / ppl
final_total = "Each person needs to pay: £{:.2f}".format(split)

print(final_total)