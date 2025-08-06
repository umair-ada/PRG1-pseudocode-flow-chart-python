print("=== Food Delivery Time Predictor ===")
    
# Input
restaurant_name = input("Enter restaurant name: ")
distance_km = float(input("Enter distance in km: "))
weather_condition = input("Enter weather (sunny/raining/snowing): ").lower()
time_of_day = input("Enter time of day (morning/lunch/afternoon/dinner/evening): ").lower()

# Base calculation
base_time = distance_km * 3

# Weather adjustments
if weather_condition == "raining":
    base_time += 10
elif weather_condition == "snowing":
    base_time += 20

# Time of day adjustments
if time_of_day == "lunch" or time_of_day == "dinner":
    base_time += 15

# Delivery fee calculation
delivery_fee = 2.50
if distance_km > 5:
    delivery_fee += 1.50

# Output
print(f"\nOrder from {restaurant_name}")
print(f"Estimated delivery time: {base_time:.0f} minutes")
print(f"Delivery fee: £{delivery_fee:.2f}")

if base_time > 45:
    print("⚠️ Long wait time - maybe cook instead?")
else:
    print("✅ Reasonable wait time!")