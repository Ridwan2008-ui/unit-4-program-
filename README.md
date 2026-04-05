# unit-4-program-
# coursework start 
# 1. Load vendor data from a file
def load_data(filename):
    vendors = []
    try:
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(",")
                vendor = {
                    "id": data[0],
                    "name": data[1],
                    "year_week": data[2],
                    "vegan": int(data[3]),
                    "meat": int(data[4]),
                    "onions": float(data[5]),
                    "ketchup": int(data[6])
                }
                vendors.append(vendor)
    except FileNotFoundError:
        print("File not found!")
    return vendors
