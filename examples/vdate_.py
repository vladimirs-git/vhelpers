"""Examples vdate.py."""
from datetime import datetime

from vhelpers import vdate

# Calculate the elapsed days, hours, minutes and seconds between two datetime objects.
start = datetime.strptime("2001-01-02 2:3:4", "%Y-%m-%d %H:%M:%S")
end = datetime.strptime("2002-02-03 3:4:5", "%Y-%m-%d %H:%M:%S")
print(vdate.delta(start, end))  # {'hours': 9529, 'minutes': 1, 'seconds': 1}

# Calculate the elapsed time in the format %H:%M:%S.
print(vdate.delta_s(start, end))  # 9529:01:01
