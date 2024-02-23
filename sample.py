#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

# Create some State objects for testing
state1 = State(name="California")
state2 = State(name="New York")
storage.new(state1)
storage.new(state2)
storage.save()

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

# Check if there are State objects before accessing them
if storage.count(State) > 0:
    first_state_id = list(storage.all(State).values())[0].id
    print("First state: {}".format(storage.get(State, first_state_id)))
else:
    print("No State objects found.")
