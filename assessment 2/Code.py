# Shah Sultan
# 20251525

class RequisitionSystem:
    #static variables
    requisition_counter = 0
    all_requisitions = []
    def __init__(self):
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.requisition_id = 0
        self.items = []
        self.total = 0.0
        self.status = "Pending"
        self.approval_ref = "Not available"



  
    def staff_info(self):
        RequisitionSystem.requisition_counter += 1
        self.requisition_id = 10000 + RequisitionSystem.requisition_counter
        self.date = input("Enter Date: ")
        self.staff_id = input("Enter Staff ID: ")
        self.staff_name = input("Enter Staff Name: ")
        print("\nPrinting Staff Information:")
        print("Date:", self.date)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Requisition ID:", self.requisition_id)

    

    def requisitions_details(self):
        self.items = []
        self.total = 0
        while True:
            item_name = input("Enter item name (or type 'done' to finish): ")
            if item_name.lower() == "done":
                break
            try:
                price = float(input("Enter item price: "))
                self.items.append((item_name, price))
                self.total += price
            except:
                print("Invalid price, try again.")
        print("Total requisition amount: $", self.total)
    def requisition_approval(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_ref = self.staff_id + str(self.requisition_id)[-3:]
        else:
            self.status = "Pending"
            self.approval_ref = "Not available"
        print("\nTotal:", self.total)
        print("Status:", self.status)
        print("Approval Ref:", self.approval_ref)

  
    def respond_requisition(self):
        if self.status == "Pending":
            print("\nManager responding to requisition", self.requisition_id)
            decision = input("Enter response (Approve/Not Approved/Leave): ").lower()
            if decision == "approve":
                self.status = "Approved"
                self.approval_ref = self.staff_id + str(self.requisition_id)[-3:]
            elif decision == "not approved":
                self.status = "Not approved"
                self.approval_ref = "Not available"
            else:
                print("Left as pending.")
        else:
            print("This requisition is not pending.")

    
    @classmethod
    def display_requisitions(cls):
        print("\nPrinting Requisitions:")
        for r in cls.all_requisitions:
            print("\nDate:", r.date)
            print("Requisition ID:", r.requisition_id)
            print("Staff ID:", r.staff_id)
            print("Staff Name:", r.staff_name)
            print("Total: $", r.total)
            print("Status:", r.status)
            print("Approval Reference Number:", r.approval_ref)

    # f. statistics
    @classmethod
    def requisition_statistic(cls):
        total_reqs = len(cls.all_requisitions)
        approved = len([r for r in cls.all_requisitions if r.status == "Approved"])
        pending = len([r for r in cls.all_requisitions if r.status == "Pending"])
        not_approved = len([r for r in cls.all_requisitions if r.status == "Not approved"])

        print("\nStatistics:")
        print("Displaying the Requisition Statistics")
        print("The total number of requisitions submitted:", total_reqs)
        print("The total number of approved requisitions:", approved)
        print("The total number of pending requisitions:", pending)
        print("The total number of not approved requisitions:", not_approved)


if __name__ == "__main__":

#creating somerequisitions
    for i in range(5):
        print("\n--- Submitting Requisition", i + 1, "---")
        req = RequisitionSystem()
        req.staff_info()
        req.requisitions_details()
        req.requisition_approval()
        RequisitionSystem.all_requisitions.append(req)
    RequisitionSystem.requisition_statistic()

    
    for req in RequisitionSystem.all_requisitions:
        if req.total >= 500:
            req.respond_requisition()

    
    RequisitionSystem.display_requisitions()

    # show stats
    RequisitionSystem.requisition_statistic()
