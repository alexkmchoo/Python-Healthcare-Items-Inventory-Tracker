"""
Command-line inventory tracker -- you choose the scenario.

See ../PROJECT_OVERVIEW.md to pick your stakeholder and data file. Design your own
class for one inventory item, based on what *your* stakeholder needs.
There's no single right set of attributes, and that's on purpose.

Run it from your repo's top folder (not from inside this folder):
    python3 starter/inventory.py
Before your final push you'll rename this folder to analysis/.
"""
import json

DATA_FILE = "/Users/alexc/Documents/mod1project/Python-Sporting-Goods-Inventory-Tracker/data/healthcare_transactions.txt"

class MedicalInventory:
    """Represents medical item in inventory with tracking"""
    low_general = 13
    low_specific = {"PPE": 20,
    "Wound Care" : 20,
    "Equipment" : 10,
    "Medication" : 15
    }

    def __init__(self, name, quantity, category):
        self.name = name
        self.quantity = quantity 
        self.category = category
        # we don't add command here as an attribute because we don't actually call it
        

    def is_low_stock(self):
        """Returns true if the quantity is at or below the quantity's cutoff"""
        cutoff = self.low_specific.get(self.category, self.low_general)
        return 0 <= self.quantity <= cutoff
    
    def add_stock(self, amount):
        if amount <= 0:
            return False, "Amount must be a positive number"
        self.quantity += amount
        return True, "Stock successfully added!"
    def reduce_stock(self, amount):
        if amount > self.quantity:
            return False, "Your amount will be negative"
        self.quantity -= amount
        return True, "Stock reduced successfully!"

masks = MedicalInventory("Surgical Face Masks", 29, "PPE") 
gloves = MedicalInventory("Nitrile Exam Gloves (M)", 20, "PPE")
# testing to see if the method works
# print(masks.is_low_stock()) 
# This should print out False because 29 > 20, meaning we don't need to restock
# print(gloves.is_low_stock())
# # This should print out False because 20 = 20, meaning we we are at the threshold, we need to restock


# Use this docstring as the model for the ones you write below: what the function does, what it takes, and what it returns.
def read_batch_file(filepath):
    """ Read the batch file at `filepath` and return a list of its lines (strings), unchanged"""
    with open(filepath) as f:
        lines = f.read().splitlines()
    return lines

field_count = {"ADD": 4, "REMOVE": 3, "SEARCH": 2}
# set what each field should hold 
def validate_line(line):
    """TODO: write your own docstring. What makes an ADD, REMOVE, or
    SEARCH line valid? What do you return for a valid line, and what for
    an invalid one?"""
    line = line.strip()
    if line == "":
        return False, "Blank : missing category"
    parts = line.split(',')
    records = []
    for x in parts:
        records.append(x.strip())
    command = records[0].upper()
    # automatically change all commands to uppercase, since thats the majority format
    if command not in field_count:
        return False, "Unknown command, its not ADD, REMOVE, or SEARCH"
        # catches any mistyped commands or random commands
        # Kept getting a KeyError, even though I have something that catches it, so moved this above the length check and it worked
    if len(records) != field_count[command]:
        return False, f"The number of fields must equal the stated field count. I got: {len(records)}"
        # We stated the number of fields each command must have , this checks it so we can safely move on
    name = records[1]
    if name == "":
        return False, "Missing a name here"
        # if there isn't a name, we return false
    if command == "SEARCH":
        return True, (command, name, None, None)
        # included this so the next part runs when we use records[2] after, since records[2] doesn't exist in search
    try:
        quantity = int(parts[2])
        # was going to do this without a try, but an error came up because in the dataset there is a "five" in the quantity column
    except ValueError:
        return False, f"'{parts[2]}' is not a whole number"
    if quantity <=0:
        return False, "quantity must be greater than 0"
    if command == "REMOVE":
        return True, (command, name, quantity, None)
        # included this here so records[3] after this can be used since remove doesn't have that third index
    category = records[3]
    if category == '':
        return False, "Missing a category here"
        # if there isn't a category value, we return false
    return True, (command, name, quantity, category)

print(validate_line("ADD, Surgical Masks, 90, PPE"))
# perfect one
print(validate_line("Add, Surgical Masks, 7, PPE"))
# lowercase, checking if the upper works
print(validate_line("random, Surgical Masks, 7, PPE"))
# checking to see if non command works, got a keyerror instead of continuing with the next print
print(validate_line("RAMOVE, Surgical Masks, 90, PPE"))
# checking to see if a mistyped command works
print(validate_line("ADD, Surgical Masks, 7 million, PPE"))
# checking to see if a non-integer would work, got the keyerror above this print line, but when commented out, it did catch it
print(validate_line("Search, Surgical Masks, 90, PPE"))
# checking to see if a fieldout error would be caught and continue running
print(validate_line("SEARCH, Surgical Masks"))
# safety print to see if it prints the actual correct field out
    




lines = read_batch_file(DATA_FILE)
print("Total lines: ",len(lines))
# showcase how many total lines there is

    # TODO: implement. One choice worth making on purpose: a quantity can
    # be present but not a number ("five"). Wrap int(quantity) in a
    # try/except ValueError. That asks Python "did this work?" instead
    # of trying to predict every way it could fail.



def process_transactions(lines):
    """TODO: write your own docstring."""
    ok, reason = validate_line(line)
    if ok :
        return (command, name, quantity, category)
    if not ok:
        return reason

    # TODO: implement. Loop over the lines, apply each valid one to your
    # collection of items, and print a specific message for each line
    # you skip. Return the collection at the end. The full inventory
    # printout is print_summary's job, not this function's.
    pass


def find_item(items, name):
    """TODO: write your own docstring."""
    # TODO: implement
    pass


def export_to_json(items, filepath="inventory.json"):
    """TODO: write your own docstring. json.dump can't write your objects
    directly, so turn each one into a dict first."""
    # TODO: implement
    pass


def print_summary(items):
    """TODO: write your own docstring."""
    # TODO: implement. This one only prints, so it doesn't need to return
    # anything.
    pass


# TODO: point this at the data file for the scenario you chose.
lines = read_batch_file("data/athletic_transactions.txt")
items = process_transactions(lines)
print_summary(items)
export_to_json(items)
