# Sample vehicle service history records
service_records = [
    ("AB123CD", ("2023-01-15", "2023-03-10", "2023-06-05")),
    ("XY987ZT", ("2023-02-20", "2023-04-12")),
    ("LM456OP", ("2023-03-05",)),
]

# 1. Show recent services (last 2 services for example)
def show_recent_services(vehicle_number):
    for vehicle, services in service_records:
        if vehicle == vehicle_number:
            recent_services = services[-2:]  # Show the last 2 services (slicing)
            print(f"Recent services for vehicle {vehicle}: {recent_services}")
            return
    print(f"Vehicle {vehicle_number} not found.")
    print("-" * 30)

# 2. Display service timeline using unpacking
def display_service_timeline(vehicle_number):
    for vehicle, services in service_records:
        if vehicle == vehicle_number:
            print(f"Service timeline for vehicle {vehicle}:")
            for index, service_date in enumerate(services, 1):
                print(f"Service {index}: {service_date}")
            return
    print(f"Vehicle {vehicle_number} not found.")
    print("-" * 30)

# 3. Replace old service record with a new one
def add_new_service(vehicle_number, new_service_date):
    global service_records
    updated = False
    for i, (vehicle, services) in enumerate(service_records):
        if vehicle == vehicle_number:
            # Create a new tuple with the added service date
            new_services = services + (new_service_date,)  # Append the new service date
            # Replace the old record with the new one
            service_records[i] = (vehicle, new_services)
            updated = True
            print(f"New service added for vehicle {vehicle}. Updated service history: {new_services}")
            break
    
    if not updated:
        print(f"Vehicle {vehicle_number} not found.")
    print("-" * 30)

# Testing the functions
show_recent_services("AB123CD")  # Show recent services for AB123CD
display_service_timeline("XY987ZT")  # Display full service timeline for XY987ZT
add_new_service("AB123CD", "2023-09-15")  # Add a new service for AB123CD
show_recent_services("AB123CD")  # Show recent services again after update
display_service_timeline("AB123CD")  # Display full service timeline after update

