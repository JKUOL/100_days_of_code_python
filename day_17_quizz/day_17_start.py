# Define a class named User
class User:
    # Constructor to initialize a new User object with ID, username, and default followers/following.
    def __init__(self, user_id, username):
        self.id = user_id  # Unique identifier for the user.
        self.username = username  # Username of the user.
        self.followers = 0  # Initialize the number of followers to 0.
        self.following = 0  # Initialize the number of followings to 0.

    # Method to simulate following another user.
    def follow(self, user):
        user.followers += 1  # Increment the other user's follower count.
        self.following += 1  # Increment this user's following count.


# Create an instance of User with ID "001" and username "angela".
user_1 = User("001", "angela")
# Create another instance of User with ID "002" and username "jack".
user_2 = User("002", "jack")

# User 1 follows User 2, which affects both users' followers and following count.
user_1.follow(user_2)

# Print the number of followers for User 2 (should be 1).
print(user_2.followers)
# Print the number of followings for User 1 (should be 1).
print(user_1.following)
