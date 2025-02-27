print("⭐Welcome to bill & tip calculator!⭐")

# Inputs
bill = float(input("Total Bill: $ "))
tip = int(input("Tip: 5%, 10%, 12%, or 15%: "))
person = int(input("How many people split the bill?:"))

# Calculations
tip_cal = tip / 100 #into decimals
get_tip_per = bill * tip_cal + bill #getting percentage
total = round(get_tip_per / person,2)


# Results
print("\n⭐Here is your bill details!⭐")
print(f"Your bill 💵 ${bill}")
print(f"Your tip 🪙  {tip}%")
print(f"Number of person {person}")
print(f"Each person should pay:💵 ${total} ")

# NOTES:
#calculate the percentage. 12% = 12 / 100 = 0.12
# 150 * 0.12  + 150