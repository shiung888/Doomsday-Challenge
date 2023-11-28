def solution(area):
    result = []
    while area > 0:
        # Calculate the side length of the largest square that can fit in the remaining area
        side_length = int(area**0.5)
        # Calculate the area of this square
        square_area = side_length**2
        # Append the square's area to the result list
        result.append(square_area)
        # Update the remaining area
        area -= square_area
    return result

# Example usage:
#area = 15324
#result = solution(area)
#print(result)  
