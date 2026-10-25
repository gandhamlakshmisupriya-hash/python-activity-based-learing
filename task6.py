
# Railway Fare and Reservation Calculator

n = int(input("Enter number of passengers: "))

for i in range(n):
    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter travel distance (km): "))

    print("Classes: 1. Sleeper  2. AC")
    choice = int(input("Select class (1 or 2): "))

    if age < 0 or distance <= 0 or choice not in (1, 2):
        print("Invalid passenger details.")
        continue

    # Distance-based fare slabs
    if distance <= 100:
        base_fare = distance * 1
    elif distance <= 500:
        base_fare = 100 + (distance - 100) * 1.5
    else:
        base_fare = 100 + 400 * 1.5 + (distance - 500) * 2

    # Class charges
    if choice == 1:
        class_rate = 1
        reservation_fee = 20
        class_name = "Sleeper"
    else:
        class_rate = 2
        reservation_fee = 40
        class_name = "AC"

    fare = base_fare * class_rate

    # Age-based concession
    if age < 5:
        concession = fare       # Free base fare
    elif age >= 60:
        concession = fare * 0.20
    else:
        concession = 0

    total = fare - concession + reservation_fee

    print("\n--- Reservation Details ---")
    print("Name:", name)
    print("Class:", class_name)
    print("Distance:", distance, "km")
    print("Base Fare: Rs.", round(fare, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Reservation Fee: Rs.", reservation_fee)
    print("Final Fare: Rs.", round(total, 2))

    # Cancellation calculation
    cancel = input("Cancel ticket? (yes/no): ").lower()

    if cancel == "yes":
        penalty = total * 0.25
        refund = total - penalty

        print("Cancellation Penalty: Rs.", round(penalty, 2))
        print("Refund Amount: Rs.", round(refund, 2))

# Railway Fare and Reservation Calculator

n = int(input("Enter number of passengers: "))

for i in range(n):
    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter travel distance (km): "))

    print("Classes: 1. Sleeper  2. AC")
    choice = int(input("Select class (1 or 2): "))

    if age < 0 or distance <= 0 or choice not in (1, 2):
        print("Invalid passenger details.")
        continue

    # Distance-based fare slabs
    if distance <= 100:
        base_fare = distance * 1
    elif distance <= 500:
        base_fare = 100 + (distance - 100) * 1.5
    else:
        base_fare = 100 + 400 * 1.5 + (distance - 500) * 2

    # Class charges
    if choice == 1:
        class_rate = 1
        reservation_fee = 20
        class_name = "Sleeper"
    else:
        class_rate = 2
        reservation_fee = 40
        class_name = "AC"

    fare = base_fare * class_rate

    # Age-based concession
    if age < 5:
        concession = fare       # Free base fare
    elif age >= 60:
        concession = fare * 0.20
    else:
        concession = 0

    total = fare - concession + reservation_fee

    print("\n--- Reservation Details ---")
    print("Name:", name)
    print("Class:", class_name)
    print("Distance:", distance, "km")
    print("Base Fare: Rs.", round(fare, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Reservation Fee: Rs.", reservation_fee)
    print("Final Fare: Rs.", round(total, 2))

    # Cancellation calculation
    cancel = input("Cancel ticket? (yes/no): ").lower()

    if cancel == "yes":
        penalty = total * 0.25
        refund = total - penalty

        print("Cancellation Penalty: Rs.", round(penalty, 2))
        print("Refund Amount: Rs.", round(refund, 2))
