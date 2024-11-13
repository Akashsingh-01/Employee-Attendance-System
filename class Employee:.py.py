class Employee:
    def _init_(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.attendance = []
     
    def mark_attendance(self, date):
      self.attendance, append (date)

    def get_attendance (self):
        returnself.attendance 
        
        
class AttendanceSystem:
    def __init__(self):
       self.employees = {}

    def add_employee(self, employee_id, name):
        if employee_id in self. employees:
           print (f"Employee ID {employee_id} already exists.")
        else:
            self. employees [employee_id] = Employee (employee_id, name)
            print(f"Employee {name}' added with ID (employee_id?.")

def mark_attendance(self, employee_id, date):
    if employee_id in self. employees:
        self. employees [employee_id]. mark_attendance(date)
        print(f"Attendance marked for {self. employees [employee_id]. name} on {date}.")
    else:
        print (f"Employee ID {employee_id} not found.")

def view_attendance(self, employee_id):
    if employee_id in self. employees:
        attendance = self. employees [employee_id].get_attendance()
        print(f"Attendance for {self. employees [employee_id].name}: {', '. join(attendance) if attendance else 'No attendance marked. '}")
    else:
         print (f"Employee ID {employee_id} not found.")

def display_menu (self):
     print ("\nEmployee Attendance System")
     print ("1. Add Employee")
     print ("2. Mark Attendance")
     print ("3.View Attendance")
     print ("4. Exit")


def main():
    system = AttendanceSystem()

    while True:
        system.display_menu()
        choice = input("choose an option (1-4): ")

        if choice == '1':
            employee_id = input("Enter Employee ID:")
            name = input("Enter Employee Name: ")
            system.add_employee(employee_id, name)

        elif choice == '2':
            employee_id = input("Enter Employee ID: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            system.mark_attendance(employee_id, date)
      
        elif choice == '3':
            employee_id = input("Enter Employee ID: ")
            system.view_attendance(employee_id)
     
        elif  choice == '4':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invlid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()             
             