class Person:
    persons = []

    def __init__(self, name, birth_year, gender, **kwargs):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.mother = kwargs.get('mother')
        self.father = kwargs.get('father')
        self.__class__.persons.append(self)

    def get_siblings_by_common_parent(self, parent):
        siblings = []
        if parent:
            for person in self.__class__.persons:
                if parent in person.get_parents() and person is not self:
                    siblings.append(person)
        return (list(set(siblings)))

    def get_parents(self):
        return (self.mother, self.father)

    def get_siblings(self):
        siblings = []
        parents = [self.mother, self.father]
        for parent in parents:
            siblings = self.get_siblings_by_common_parent(parent) + siblings
        return (list(set(siblings)))

    def get_sisters(self):
        return list(filter(lambda sibling: sibling.gender == 'F',
                           self.get_siblings()))

    def get_brothers(self):
        return list(filter(lambda sibling: sibling.gender == 'M',
                           self.get_siblings()))

    def children(self, **kwargs):
        genders = ['F', 'M']
        children_list = []
        if kwargs:
            genders = [kwargs.get('gender')]
        for person in self.__class__.persons:
            if self in person.get_parents():
                children_list.append(person)
        return list(filter(lambda child: child.gender in genders,
                           children_list))

    def is_direct_successor(self, another_person):
        return another_person in self.children()
