class Task:
    def __init__(self, title, description, estimated, priorities, published=None, edited=None, user_id=None, ):
        self.title = title
        self.description = description
        self.estimated = estimated
        self.published = published
        self.edited = edited
        self.user_id = user_id
        self.priorities = priorities

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __str__(self, *args, **kwargs):
        return str(self.__dict__)
