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

DATA_FILE = "/Users/alexc/Documents/mod1project/Python-Sporting-Goods-Inventory-Tracker/data/athletic_transactions.txt"

class SportingGoods:
    lowstock = 10

    """
    TODO: rename this class to something that fits your scenario, and
    write a real docstring. What does one of these represent? At minimum
    you'll need a name and a quantity. Add what your stakeholder asked
    for, not more and not less.
    """

    def __init__(self, name, quantity, category):
        self.name = name
        self.quantity = quantity 
        self.category = category
        # add your own parameters (self, plus each attribute you're
        # tracking) and store each one as self.whatever = whatever.
        

    def is_low_stock(self):
        """True if the item is amost out or up till the limit (lowstock). False if the item is at 0"""
        return 0 < self.quantity <= self.lowstock
        # REFLECTION.md's "Assumptions" section.
    
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
    def in_stock(self):
        if self.quantity == 0:
            return "Out of Stock"


     


def read_batch_file(filepath):
    """
    Read the batch file at `filepath` and return a list of its lines
    (strings), unchanged. Deciding whether a line is usable happens in
    validate_line(), not here. Use this docstring as the model for the
    ones you write below: what the function does, what it takes, and what
    it returns.
    """
    with open(filepath) as f:
        lines = f.read().splitlines()
    return lines
    # TODO: implement

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
        return False, "Unknown command, its not ADD,REMOVE, or SEARCH"
        # if there isn't a command, return False
    name = records[1]
    if name == "":
        return False, "Missing a name here"
        # if there isn't a name, we return false
    quantity = int(records[2])
    if quantity == '':
        return False, "Missing a quantity here"
        # if there isn't a quantity value, we return false
    category = records[3]
    if category == '':
        return False, "Missing a category here"
        # if there isn't a category value, we return false
  
    



'''
records = read_batch_file(DATA_FILE)
print("Total lines: ",len(records))
# showcase how many total lines there is
valid = []
for linenumber, line in records:
    ok, reason = validate_line(line)
    if ok:
        valid.append(reason)
    else:
        print(f"line {linenumber} rejected {reason}")
'''
    # TODO: implement. One choice worth making on purpose: a quantity can
    # be present but not a number ("five"). Wrap int(quantity) in a
    # try/except ValueError. That asks Python "did this work?" instead
    # of trying to predict every way it could fail.



def process_transactions(lines):
    """TODO: write your own docstring."""
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
