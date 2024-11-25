def can_fit(box1, box2):
    # Check if box1 can fit inside box2 by comparing dimensions
    return all(x < y for x, y in zip(box1, box2))

def box_packing(n, boxes):
    # Sort the dimensions of each box
    sorted_boxes = [tuple(sorted(box)) for box in boxes]
    
    # Sort the boxes first by the first dimension, then by the second, and finally by the third dimension
    sorted_boxes.sort()

    # DP array where dp[i] is the longest sequence of boxes ending with box i
    dp = [1] * n

    # Find the longest sequence of boxes
    for i in range(1, n):
        for j in range(i):
            if can_fit(sorted_boxes[j], sorted_boxes[i]):
                dp[i] = max(dp[i], dp[j] + 1)

    # The largest value in dp array is the answer
    return max(dp)

# Example usage
n = 6
boxes = [(1, 5, 6), (3, 4, 5), (1, 2, 3), (6, 2, 8), (5, 5, 1), (2, 3, 1)]

# Find the largest number of boxes that can be packed in sequence
result = box_packing(n, boxes)
print(result)  # Output: 2
