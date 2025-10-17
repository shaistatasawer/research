# Global counter for requisition ids
requisition_counter = 0

#List to save requisitions
requisitions_list = []

# Task 1: Staff info
def staff_info():
    global requisition_counter
    requisition_counter += 1
    requisition_id = 10000 + requisition_counter
    date = input("Enter Date: ")
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")
    print("\nPrinting Staff Information:")
    print("Date:", date)
    print("Staff ID:", staff_id)
    print("Staff Name:", staff_name)
    print("Requisition ID:", requisition_id)
    return date, staff_id, staff_name, requisition_id


# Task 2: Requisitions Total
def requisitions_total():
    staff_data = staff_info()
    total = 0
    items = []
    while True:
            item_name = input("Enter item name or type 'exit' to total): ")
            if item_name.lower() == "exit":
                break
            price = float(input("Enter item price: "))
            items.append((item_name, price))
            total += price

    print("\nTotal: $", total)
    requisitions_list.append((staff_data, items, total))
    return staff_data, items, total




#Task 3:Requisition Approval
def requisition_approval():
    staff_data, items, total = requisitions_total()
    status = "Pending"
    approval_ref = "None"
    if total < 500:
        status = "Approved"
        approval_ref = staff_data[1] + str(staff_data[3])[-3:]
    print("\nTotal: $", total)
    print("Status:", status)


    if status == "Approved":
        print("Approval Reference Number:", approval_ref)
    return staff_data, items, total, status, approval_ref



# Task 4: Display Requisitions
def display_requisitions():
    staff_data, items, total, status, approval_ref = requisition_approval()
    print("\nPrinting Requisitions:")
    print("Date:", staff_data[0])
    print("Requisition ID:", staff_data[3])
    print("Staff ID:", staff_data[1])
    print("Staff Name:", staff_data[2])
    print("Total: $", total)
    print("Status:", status)
    if status == "Approved":
        print("Approval Reference Number:", approval_ref)



#call display_requisitions()
display_requisitions()
