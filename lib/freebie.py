
class Freebie:
    
    all = []

    def __init__(self, dev, company, item_name, value):
        self.dev = dev
        self.company = company
        self.item_name = item_name
        self.value = value 

        self.__class__.all.append(self)

    @property
    def dev(self):
        return self._dev
    
    @dev.setter
    def dev(self, value):
        from dev import Dev
        if isinstance(value, Dev):
            self._dev = value
    
    @property
    def company(self):
        return self._company
    
    @company.setter
    def company(self, value):
        from company import Company
        if isinstance(value, Company):
            self._company = value

    @property
    def item_name(self):
        return self._item_name
    
    @item_name.setter
    def item_name(self, value):
        if isinstance(value, str):
            self._item_name = value 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, int):
            self._value = value 



    def print_details(self):
        return f"{self.dev} owns a {self.item_name} from {self.company}"

    def __repr__(self):
        return f"{self.dev}: {self.company}: {self.item_name} ${self.value}"
