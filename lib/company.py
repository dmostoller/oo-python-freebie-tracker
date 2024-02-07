from freebie import Freebie

class Company:
    
    all = []

    def __init__(self, name, founding_year):
        self.name = name
        self.founding_year = founding_year

        self.__class__.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value

    @property
    def founding_year(self):
        return self._founding_year
    
    @founding_year.setter
    def founding_year(self, value):
        if isinstance(value, int):
            self._founding_year = value

    def freebies(self):
        from freebie import Freebie
        return [freebie for freebie in Freebie.all if freebie.company == self]
    
    def devs(self):
        return list(set([freebie.dev for freebie in self.freebies()]))
    
    def give_freebie(self, dev, item_name, value):
        Freebie(dev, self, item_name, value)

    @classmethod
    def oldest_company(cls):
        oldest_company = None
        oldest_founding_year = 2023
        for company in cls.all:
            if company.founding_year < oldest_founding_year:
                oldest_company = company
                oldest_founding_year = company.founding_year
        return oldest_company

    def __repr__(self):
        return self.name