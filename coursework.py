# coursework start 
# Hotdog Vendor Management
# Create the Hotdogs.txt data file
#Format: ID ,Name, Yearweek, Vegansold ,Meatsold,Onion used, Ketchup used
import time
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
    my_file.write("RA_101,Ridwan Afrah,202313,50,120,10.5,2\n")
    my_file.write("RA_101,Ridwan Afrah,202314,60,140,15.0,3\n")
    my_file.write("JS_202,John Smith,202313,40,110,10.0,1\n")
    my_file.write("JS_202,John Smith,202314,60,150,15.5,2\n")

# 1. validation functions 
def validate_vendor_id(vendor_id):
    # must be AA_123 format
    return len(vendor_id) == 6 and vendor_id[:2].isupper() and vendor_id[2] == "_" and vendor_id[3:].isdigit()

def validate_vendor_name(name):
    # between 2 and 25 chars
    return 2 <= len(name) <= 25

def validate_year_week(year_week):
    # must be YYYYWW and week 1-52
    if len(year_week) != 6 or not year_week.isdigit():
        return False
    week = int(year_week[4:])
    return 1 <= week <= 52

def validate_hotdogs(num):
    # must be divisible by 10
    return num % 10 == 0

def validate_onions(onions):
    # must be .5 steps
    return (onions * 2).is_integer()

def validate_ketchup(ketchup):
    # must be between 1 and 4
    return 1 <= ketchup <= 4

# 2. Load vendor data from file
import time 

def load_data(filename):
    vendors = [] 
    try:
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if not data or len(data) < 7: continue 

                try:
                    
                    vendor = {
                        "id": data[0],
                        "name": data[1],
                        "year_week": data[2],
                        "vegan": int(data[3]),
                        "meat": int(data[4]),
                        "onions": float(data[5]),
                        "ketchup": int(data[6])
                    }
                    
                    
                    
                    if (
                        validate_vendor_id(vendor["id"]) and
                        validate_vendor_name(vendor["name"]) and
                        validate_year_week(vendor["year_week"]) and
                        validate_hotdogs(vendor["vegan"]) and
                        validate_hotdogs(vendor["meat"]) and
                        validate_onions(vendor["onions"]) and
                        validate_ketchup(vendor["ketchup"])
                    ):
                        vendors.append(vendor)
                    else:
                        print("Invalid row skipped:", data)

                except (ValueError, IndexError) as e:
                    print(f"Error processing row {data}: {e}")

    except FileNotFoundError:
        print("File not found!")

    return vendors

# 3. Linear search (unsorted)
def linear_search_unsorted(vendors, target_id):
    # go through list one by one
    for vendor in vendors:
        if vendor["id"] == target_id:
            return vendor
    return None

# 4. Linear search (sorted)
def linear_search_sorted(vendors, target_id):
    # same as normal but assumes sorted
    for vendor in vendors:
        if vendor["id"] == target_id:
            return vendor
        elif vendor["id"] > target_id:
            break
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

# 8. TIMING FUNCTIONS
def time_search(func, vendors, target):
    start = time.time()
    result = func(vendors, target)
    end = time.time()
    return result, end - start

def time_sort(func, vendors):
    start = time.time()
    result = func(vendors)
    end = time.time()
    return result, end - start

#  PERFORMANCE FUNCTIONS
def time_search_perf(func, vendors, target):
    start = time.perf_counter()
    result = func(vendors, target)
    end = time.perf_counter()
    return result, end - start

def time_sort_perf(func, vendors):
    start = time.perf_counter()
    result = func(vendors)
    end = time.perf_counter()
    return result, end - start

# 9. ANALYSIS
def most_productive_vendor(vendors):
    return max(vendors, key=lambda v: v["vegan"] + v["meat"])

def total_hotdogs(vendors):
    return sum(v["vegan"] for v in vendors), sum(v["meat"] for v in vendors)

def least_ketchup(vendors):
    return min(vendors, key=lambda v: v["ketchup"])

def save_results(filename, text):
    with open(filename, "w") as file:
        file.write(text)

# 9. MAIN
def main():
    vendors = load_data("Hotdogs.txt")
    if not vendors: return

    
    while True:
        target = input("Enter Vendor ID (e.g. DD_056): ")
        if validate_vendor_id(target):
            break  # Exit loop if ID is valid
        else:
            print("Error: Invalid Vendor ID format. Please use 'AA_123' (2 caps, underscore, 3 digits).")

    # Sorting 
    bubble_sorted, bubble_time = time_sort(bubble_sort, vendors)
    quick_sorted, quick_time = time_sort(quick_sort, vendors)

    # Searching 
    b_res, b_time = time_search(binary_search, quick_sorted, target)
    lu_res, lu_time = time_search(linear_search_unsorted, vendors, target)

    #  EFFICIENCY COMPARISON (SORTS) 
    sorted_bub, t_bubble_perf = time_sort_perf(bubble_sort, list(vendors))
    sorted_qui, t_quick_perf = time_sort_perf(quick_sort, list(vendors))

    #  EFFICIENCY COMPARISON (SEARCHES)
    res_un, t_unsorted = time_search_perf(linear_search_unsorted, vendors, target)
    res_so, t_sorted_lin = time_search_perf(linear_search_sorted, quick_sorted, target)
    res_bi, t_binary = time_search_perf(binary_search, quick_sorted, target)

    # Analysis
    best = most_productive_vendor(vendors)
    vegan, meat = total_hotdogs(vendors)
    least = least_ketchup(vendors)

    output = (
        f"\nMost productive vendor entry: {best['name']} (ID: {best['id']})\n"
        f"Total vegan sold: {vegan}\n"
        f"Total meat sold: {meat}\n"
        f"Vendor entry with least ketchup: {least['name']}\n"
        f"\nSort Times -> Bubble: {bubble_time:.6f}s, Quick: {quick_time:.6f}s\n"
        f"Search Times -> Binary: {b_time:.6f}s, Linear: {lu_time:.6f}s\n"
        f"\n--- Sort Efficiency Comparison (perf_counter) ---"
        f"\nBubble Sort: {t_bubble_perf:.10f}s"
        f"\nQuick Sort:  {t_quick_perf:.10f}s"
        f"\n--- Search Efficiency Comparison (perf_counter) ---"
        f"\nUnsorted Linear: {t_unsorted:.10f}s"
        f"\nSorted Linear:   {t_sorted_lin:.10f}s"
        f"\nBinary Search:   {t_binary:.10f}s\n"
    )

    print(output)
    save_results("analysis_results.txt", output)

if __name__ == "__main__":
    main()
