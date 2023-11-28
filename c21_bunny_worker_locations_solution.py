def solution(x, y):
    worker_id = ((x + y - 2) * (x + y - 1)) // 2 + x
    return str(worker_id)

# Example usage:
#x1, y1 = 1, 1
#x2, y2 = 3, 2
#x3, y3 = 2, 3

#print(solution(x1, y1))  # Output: "1"
#print(solution(x2, y2))  # Output: "9"
#print(solution(x3, y3))  # Output: "8"
