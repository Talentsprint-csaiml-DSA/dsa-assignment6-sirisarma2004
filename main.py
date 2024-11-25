# box_packing.py

def can_fit(box1, box2):
    """Returns True if box1 can fit inside box2, based on sorted dimensions."""
    return all(x < y for x, y in zip(box1, box2))

def longest_box_sequence(boxes):
    """Returns the length of the longest sequence of boxes where each box can fit inside the next."""
    # Normalize each box by sorting its dimensions (ascending order)
    sorted_boxes = [tuple(sorted(box)) for box in boxes]
    
    # Sort the list of boxes by their dimensions
    sorted_boxes.sort()

    print("Sorted boxes:", sorted_boxes)  # Debugging line to check the sorted order
    
    n = len(sorted_boxes)
    
    # Initialize the dynamic programming table where dp[i] is the length of the longest sequence ending at i
    dp = [1] * n

    # Loop through each box starting from the second one
    for i in range(1, n):
        for j in range(i):
            # Check if box j can fit inside box i
            if can_fit(sorted_boxes[j], sorted_boxes[i]):
                # Update dp[i] with the maximum sequence length possible
                dp[i] = max(dp[i], dp[j] + 1)

        # Print the dp table after processing each box for debugging
        print(f"dp[{i}] = {dp[i]}")

    # Return the length of the longest sequence found
    return max(dp)

# Test the function with the provided test case

def test_complex_case():
    boxes = [(5, 4, 6), (6, 7, 8), (3, 2, 1), (4, 5, 6), (6, 5, 7)]
    result = longest_box_sequence(boxes)
    print(f"Longest box sequence length: {result}")
    assert result == 3, "Failed on complex input"

# Running the test
test_complex_case()
