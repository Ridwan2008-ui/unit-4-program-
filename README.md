# unit-4-program-
# coursework start 
# Hotdog Vendor Management
# Create the Hotdogs.txt data file
#Format: ID ,Name, Yearweek, Vegansold ,Meatsold,Onion used
with open("Hotdogs.txt", "w") as my_file:
    my_file.write("DD_056,Dolly Dogs,202313,40,140,10.5,1\n")
    my_file.write("DD_056,Dolly Dogs,202314,40,170,15.0,2\n")
    my_file.write("DD_056,Dolly Dogs,202315,60,100,14.5,1\n")
    my_file.write("DD_056,Dolly Dogs,202316,90,130,15.0,2\n")
    my_file.write("DD_056,Dolly Dogs,202317,40,170,25.5,4\n")
    my_file.write("DD_056,Dolly Dogs,202318,70,130,20.0,1\n")
    my_file.write("DD_056,Dolly Dogs,202319,50,180,15.5,4\n")
    my_file.write("DD_056,Dolly Dogs,202320,90,130,10.0,2\n")
    my_file.write("KK_745,Korner Kart,202313,60,130,10.5,2\n")
    my_file.write("KK_745,Korner Kart,202314,30,130,10.0,4\n")
    my_file.write("KK_745,Korner Kart,202315,80,150,25.5,2\n")
    my_file.write("KK_745,Korner Kart,202316,30,140,25.0,3\n")
    my_file.write("KK_745,Korner Kart,202317,80,160,20.5,4\n")
    my_file.write("KK_745,Korner Kart,202318,90,170,25.0,1\n")
    my_file.write("KK_745,Korner Kart,202319,80,150,20.5,3\n")
    my_file.write("KK_745,Korner Kart,202320,90,180,25.0,4\n")
# 1. Load vendor data from file
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


 
