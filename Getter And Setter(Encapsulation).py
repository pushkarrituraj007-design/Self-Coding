#Encapsulation usage of Getter And Setter:-
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Internal/protected variable

    # 1. The Getter method:-
    @property
    def salary(self):
        """Retrieves the value of salary."""
        print("Fetching salary...")
        return self._salary

    # 2. The Setter Method:-
    @salary.setter
    def salary(self, value):
        """Validates and sets the value of salary."""
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        print("Setting salary...")
        self._salary = value

# --- Usage ---
emp = Employee("RituRaj", 50000)

# Accessing like a regular attribute triggers the getter
print(emp.salary)  # Prints: Fetching salary... \n 50000

# Modifying like a regular attribute triggers the setter
emp.salary = 60000  # Prints: Setting salary...

# Data validation prevents invalid inputs
# emp.salary = -1000  # Raises: ValueError: Salary cannot be negative!
