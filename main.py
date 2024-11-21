def longest_box_sequence(box1, box2):

#def can_nest():
    return all(box1[i] < box2[i] for i in range(3))

def box_packing(n, boxes):
    # Sort boxes by dimensions
    boxes.sort(key=lambda box: (box[0], box[1], box[2]))

    # DP array to store the maximum number of boxes that can be nested ending at each box
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if longest_box_sequence(boxes[j], boxes[i]):
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example usage
if __name__ == "__main__":
    n = 6
    boxes = [(1, 5, 6), (3, 4, 5), (1, 2, 3), (6, 2, 8), (5, 5, 1), (2, 3, 1)]
    print("Largest number of boxes that can be packed:", box_packing(n, boxes))
