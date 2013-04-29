class Person:
    persons = []

    def __init__(self, name, birth_year, gender, father=None, mother=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.mother = mother
        self.father = father
        self.children_set = set()
        self.__class__.persons.append(self)
        self.add_to_parent(self.father)
        self.add_to_parent(self.mother)

    def add_to_parent(self, parent):
        if parent is not None:
            parent.children_set.add(self)

    def get_parents(self):
        return [self.mother, self.father]

    def get_siblings(self, gender=None):
        siblings = set()
        parents = self.get_parents()
        for parent in parents:
            siblings.update(parent.children(gender))

        if self in siblings:
            siblings.remove(self)
        return list(siblings)

    def get_sisters(self):
        return self.get_siblings('F')

    def get_brothers(self):
        return self.get_siblings('M')

    def children(self, gender=None):
        children = self.children_set
        if gender is not None:
            return [child for child in children if child.gender == gender]
        return list(children)

    def is_direct_successor(self, another_person):
        return another_person in self.children()
