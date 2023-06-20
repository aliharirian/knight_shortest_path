# Function to check if a position is valid on the chessboard
def is_valid_position(x, y):
    return 0 <= x < 8 and 0 <= y < 8


# Function to find the shortest path using BFS algorithm
def shortest_path(start, end):
    # Possible moves for a knight piece
    moves = [
        (1, 2),
        (2, 1),
        (-2, -1),
        (-1, -2),
        (-2, 1),
        (1, -2),
        (-1, 2),
        (2, -1),
    ]

    # Initialize the visited matrix
    visit = []
    for _ in range(8):
        row = [False] * 8
        visit.append(row)

    # Initialize the queue list
    queue = [(start, [])]

    # Using the BFS algorithm to find the shortest path
    while queue:
        (x, y), path = queue.pop(0)

        if (x, y) == end:
            return path

        if not visit[x][y]:
            visit[x][y] = True

            # Generate all possible next moves
            for dx, dy in moves:
                next_x, next_y = x + dx, y + dy

                if is_valid_position(next_x, next_y) and not visit[next_x][next_y]:
                    queue.append(((next_x, next_y), path + [(next_x, next_y)]))

    # If no path is found
    return []


if __name__ == '__main__':
    # Example usage
    a = (0, 0)  # Starting position (A)
    b = (7, 7)  # Ending position (B)
    shortest_path_result = shortest_path(a, b)

    # Show the result of the shortest path func on terminal
    if shortest_path_result:
        print(f"The shortest path from {a} to {b} is {len(shortest_path_result)} moves.")
        print(f"The path is:")
        for position in shortest_path_result:
            print(f" - {position}")
    else:
        print(f"No path found from {a} to {b}.")
