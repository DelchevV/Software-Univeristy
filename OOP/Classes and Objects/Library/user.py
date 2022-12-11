class User:
    def __init__(self, user_id:int, username:str):
        self.user_id=user_id
        self.username=username
        self.books=[]

    def info(self):
        return ", ".join(sorted(self.books, key=lambda x:x))

    def __str__(self):
        result=f"{self.user_id}, {self.username}, {self.books}"
        return result
