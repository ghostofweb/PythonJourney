# Input the shipment code from the user
shipment_code = input("Enter the shipment code: ")

modes = []

# Input the shipment code from the user
shipment_code = input("Enter the shipment code: ")

modes = []

if shipment_code[0] == '1':
    modes.append("Airway")
else:
    modes.append("Roadway")

if shipment_code[1] == '1':
    modes.append("Waterway")

if shipment_code[2] == '1':
    modes.append("Roadway")

if len(modes) == 1:
    print(modes[0])
elif len(modes) == 2:
    print(" and ".join(modes))
else:
    print("All ways")
