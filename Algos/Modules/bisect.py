import bisect

# A list must be sorted before using bisect functions
sorted_list = [10, 20, 30, 40, 50]

# --- Finding Insertion Points (O(log n)) ---
# Find the position to insert 25
pos = bisect.bisect(sorted_list, 25)
print(f"Position to insert 25: {pos}")
# Output: Position to insert 25: 2

# Find the leftmost position to insert 20 (it already exists)
left_pos = bisect.bisect_left(sorted_list, 20)
print(f"Leftmost position for 20: {left_pos}")
# Output: Leftmost position for 20: 1

# Find the rightmost position to insert 20
right_pos = bisect.bisect_right(sorted_list, 20)
print(f"Rightmost position for 20: {right_pos}")
# Output: Rightmost position for 20: 2


# --- Inserting Elements (O(n)) ---
# Insert 35 while keeping the list sorted
bisect.insort(sorted_list, 35)
print(f"List after inserting 35: {sorted_list}")
# Output: List after inserting 35: [10, 20, 30, 35, 40, 50]

# Insert another 20 using insort_left
bisect.insort_left(sorted_list, 20)
print(f"List after inserting 20 (left): {sorted_list}")
# Output: List after inserting 20 (left): [10, 20, 20, 30, 35, 40, 50]

# Insert another 20 using insort_right
bisect.insort_right(sorted_list, 20)
print(f"List after inserting 20 (right): {sorted_list}")
# Output: List after inserting 20 (right): [10, 20, 20, 20, 30, 35, 40, 50]
