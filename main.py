# box_packing.py
def can_fit(box1, box2):
    return all(x < y for x, y in zip(box1, box2))

def longest_box_sequence(boxes):
    sorted_boxes = [tuple(sorted(box)) for box in boxes]
    sorted_boxes.sort()

    n = len(sorted_boxes)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if can_fit(sorted_boxes[j], sorted_boxes[i]):
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
