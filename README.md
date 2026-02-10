# geo-matcher
A module that matches each GPS point in one array to the closest point in another array using Haversine distance.

### Project Mission
This project provides developers with a straightforward method: If the user gives two arrays of geo location, match each point in the first array to the closest one in the second array

### Core Formula
We utilize the **Haversine Formula** to calculate spherical distances, which yields greater accuracy than the standard Pythagorean theorem for long-range computations.

### Usage
Developers need only import the function from `matcher.py`:

```python
from matcher import find_nearest_neighbor
array1 = [(latitude, longitude), ...]
array2 = [(latitude, longitude), ...]
matches = find_nearest_neighbor(array1, array2)
