from Library.library import Library
from Library.user import User


class Registration:

    def add_user(self, user: User, library: Library):
        for show in library.user_records:
            if show.user_id == user.user_id:
                return f"User with id = {user.user_id} already registered in the library!"
        return library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id, new_username, library: Library):
        for users in library.user_records:
            if users.user_id == user_id:
                if users.username == new_username:
                    return "Please check again the provided username - it should be different than the username used so far!"
                else:
                    searched_name = users.username
                    users.username = new_username
                    for key, value in library.rented_books:
                        if key == searched_name:
                            library.rented_books[key] = new_username
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
        return f"There is no user with id = {user_id}!"



