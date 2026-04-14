# coursework start 
# Hotdog Vendor Management
# Create the Hotdogs.txt data file
#Format: ID ,Name, Yearweek, Vegansold ,Meatsold,Onion used, Ketchup used
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
    vendors_list = [] 
    try:
        with open(filename, "r") as file:
            
            for line in file:
               
                if not line.strip():
                    continue
                    
                data = line.strip().split(",")
                
               
                vendor_entry = {
                    "id": data[0],
                    "name": data[1],
                    "year_week": data[2],
                    "vegan": int(data[3]),
                    "meat": int(data[4]),
                    "onions": float(data[5]),
                    "ketchup": int(data[6])
                }
                
                vendors_list.append(vendor_entry)
                
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    
    return vendors_list


data = load_data("Hotdogs.txt")


for row in data:
    print(row)

# 2. Linear search (unsorted)
def linear_search_unsorted(vendors, target_id):
    for vendor in vendors:
        if vendor["id"] == target_id:
            return vendor
    return None

# 3. Linear search (sorted)
def linear_search_sorted(vendors, target_id):
    for vendor in vendors:
        if vendor["id"] == target_id:
            return vendor
    return None

# 5. Binary Search (Sorted Only)
def binary_search(vendors, target_id):
    low = 0
    high = len(vendors) - 1
    # Keep searching while range exists
    while low <= high:
        mid = (low + high) // 2  # Middle index
        if vendors[mid]["id"] == target_id:  # Found it
            return vendors[mid]
        elif vendors[mid]["id"] < target_id:  # Target is bigger
            low = mid + 1
        else:  # Target is smaller
            high = mid - 1
    return None  # Not found

# 6. Bubble Sort
def bubble_sort(vendors):
    n = len(vendors)
    # Go through each pass
    for i in range(n):
        # Compare each pair of adjacent vendors
        for j in range(0, n-i-1):
            if vendors[j]["id"] > vendors[j+1]["id"]:
                # Swap if out of order
                vendors[j], vendors[j+1] = vendors[j+1], vendors[j]
    return vendors

# 7. Quick Sort
def quick_sort(vendors):
    # If list is empty or one item, it's already sorted
    if len(vendors) <= 1:
        return vendors
    # Pick first vendor as pivot
    pivot = vendors[0]
    # Vendors smaller or equal go left
    left = [v for v in vendors[1:] if v["id"] <= pivot["id"]]
    # Vendors bigger go right
    right = [v for v in vendors[1:] if v["id"] > pivot["id"]]
    # Sort both sides and combine with pivot
    return quick_sort(left) + [pivot] + quick_sort(right)
