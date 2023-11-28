def staircase_combinations(height, bricks, memo):
    if memo[height][bricks] != 0:
        return memo[height][bricks]
    if bricks == 0:
        return 1
    if bricks < height:
        return 0

    memo[height][bricks] = staircase_combinations(height + 1, bricks - height, memo) + \
                           staircase_combinations(height + 1, bricks, memo)

    return memo[height][bricks]


def solution(n):
    # n will always be at least 3 (so we can have a staircase at all), but no more than 200 (because of budget)
    min_bricks = 3
    max_bricks = 200

    # if we have too few bricks, or too many are requested, then we can't build a staircase
    if min_bricks < n > max_bricks:
        return 0

    # create a grid to store the combinations, and initialize the elements to 0
    combinations = [[0 for column in range(n + 2)] for row in range(n + 2)]

    starting_height = 1
    combinations = staircase_combinations(starting_height, n, combinations) - 1

    return combinations
