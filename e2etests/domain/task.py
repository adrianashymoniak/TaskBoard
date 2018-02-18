class Task:
    def __init__(self, title, description, estimated, published=None):
        self.title = title
        self.description = description
        self.estimated = estimated
        self.published = published

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False
