# Input we need from the user 
# Total rent
# Total food order from snacking
# Electricity units spend
# Charge per unit
# Person living in room/flat

# #Output
# Total amount you'hv to pay is
Rent = int(input("Enter your hostel/flat rent = "))
Food = int(input("Enter the amount of Food ordered = "))
Electricity_spend = int(input("Enter the Total the electricity spend = "))
Charge_per_unit = int(input("Enter the charge per unit = "))
Person = int(input("Enter the number of person living in room/flat = "))

Total_bill = Electricity_spend * Charge_per_unit

Output =  (Rent+Food+Total_bill) // Person
print (f"Each person will pay = ", Output )






