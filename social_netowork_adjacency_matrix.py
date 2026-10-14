# Social Network using Adjacency Matrix

def create_matrix(n):
    return [[0 for _ in range(n)] for _ in range(n)]


def add_friend(matrix, user1, user2):
    matrix[user1][user2] = 1
    matrix[user2][user1] = 1


def remove_friend(matrix, user1, user2):
    matrix[user1][user2] = 0
    matrix[user2][user1] = 0


def display_matrix(matrix):
    print("\nAdjacency Matrix:")
    for row in matrix:
        print(*row)


def find_friends(matrix, user):
    friends = []

    for i in range(len(matrix)):
        if matrix[user][i] == 1:
            friends.append(i)

    return friends


# Main program
n = int(input("Enter number of users: "))

matrix = create_matrix(n)

while True:

    print("\n----- SOCIAL NETWORK -----")
    print("1. Add Friend")
    print("2. Remove Friend")
    print("3. Display Matrix")
    print("4. Find Friends")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        user1 = int(input("Enter first user: "))
        user2 = int(input("Enter second user: "))

        add_friend(matrix, user1, user2)
        print("Friendship added.")

    elif choice == 2:
        user1 = int(input("Enter first user: "))
        user2 = int(input("Enter second user: "))

        remove_friend(matrix, user1, user2)
        print("Friendship removed.")

    elif choice == 3:
        display_matrix(matrix)

    elif choice == 4:
        user = int(input("Enter user number: "))

        friends = find_friends(matrix, user)

        if friends:
            print("Friends of User", user, ":", friends)
        else:
            print("No friends found.")

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")