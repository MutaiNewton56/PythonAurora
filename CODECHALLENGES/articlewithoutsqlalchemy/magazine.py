class Magazine():
    def __init__(self, name, category):
        self._name=name
        self._category=category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        ## Make all checks here
        self._name=value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        ## Make all checks here
        self._category=value
