
import json
from datetime import datetime

# Let's say we have a custom class
class Meeting:
    def __init__(self, location, time):
        self.location = location
        self.time = time

def custom_encoder(obj):
    # If the object is a datetime object, convert it to an ISO string
    if isinstance(obj, datetime):
        return obj.isoformat()
    # If the object is a Meeting instance, convert it to a dictionary
    if isinstance(obj, Meeting):
        return obj.__dict__
    # For all other types, raise a TypeError
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

meeting = Meeting("Office", datetime(2025, 10, 26, 14, 30))

# Use the custom function to handle the Meeting object and the datetime object
json_string = json.dumps(meeting, default=custom_encoder, indent=4)

print(json_string)