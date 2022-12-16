def intervals_overlap(interval1, interval2):
    a, b = interval1
    c, d = interval2
    return max(a, c) <= min(b, d)

# Example intervals
interval1 = (2, 4)
interval2 = (4, 5)

# Check if the intervals overlap
if intervals_overlap(interval1, interval2):
    print("The intervals overlap.")
else:
    print("The intervals do not overlap.")