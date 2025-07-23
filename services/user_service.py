class UserService:
    """
    A service class to handle user-related operations.
    """

    def __init__(self, user_repository):
        """
        Initialize the UserService with a user repository.

        :param user_repository: An instance of a repository to interact with user data.
        """
        self.user_repository = user_repository

    def create_user(self, user_data):
        """
        Create a new user.

        :param user_data: A dictionary containing user details.
        :return: The created user object or an error message.
        """
        try:
            user = self.user_repository.add_user(user_data)
            return user
        except Exception as e:
            return {"error": str(e)}

    def get_user_by_id(self, user_id):
        """
        Retrieve a user by their ID.

        :param user_id: The ID of the user to retrieve.
        :return: The user object or None if not found.
        """
        return self.user_repository.get_user(user_id)

    def update_user(self, user_id, updated_data):
        """
        Update an existing user's information.

        :param user_id: The ID of the user to update.
        :param updated_data: A dictionary containing updated user details.
        :return: The updated user object or an error message.
        """
        try:
            user = self.user_repository.update_user(user_id, updated_data)
            return user
        except Exception as e:
            return {"error": str(e)}

    def delete_user(self, user_id):
        """
        Delete a user by their ID.

        :param user_id: The ID of the user to delete.
        :return: A success message or an error message.
        """
        try:
            self.user_repository.delete_user(user_id)
            return {"message": "User deleted successfully"}
        except Exception as e:
            return {"error": str(e)}

    def list_users(self):
        """
        Retrieve a list of all users.

        :return: A list of user objects.
        """
        return self.user_repository.get_all_users()