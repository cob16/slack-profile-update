class StubUserLinkStore:
    def __init__(self):
        self.__links = []

    def link(self, source, destination):
        for link in self.__links:
            if source in link:
                link.add(destination)
                return True
            elif destination in link:
                link.add(source)
                return True

        self.__links.append({source, destination})
        return False

    def fetch(self, source):
        for user_link_set in self.__links:
            if source in user_link_set:
                new_link = user_link_set.copy()
                new_link.remove(source)
                return new_link

        raise KeyError

    def unlink(self, user):
        for user_link_set in self.__links:
            if user in user_link_set:
                if len(user_link_set) > 2:
                    user_link_set.remove(user)
                else:
                    self.__links.remove(user_link_set)
                return
