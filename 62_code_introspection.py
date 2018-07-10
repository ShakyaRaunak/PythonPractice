# https://www.learnpython.org/en/Code_Introspection
# Example to print a list of all attributes of the given Vehicle object.

# Define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


# Print a list of all attributes of the Vehicle class.
print(dir(Vehicle))
