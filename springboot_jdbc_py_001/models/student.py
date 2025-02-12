class Student:
    def __init__(self, id=None, name=None, passport_number=None):
        self.id = id
        self.name = name
        self.passport_number = passport_number

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def passport_number(self):
        return self._passport_number

    @passport_number.setter
    def passport_number(self, value):
        self._passport_number = value

    def __str__(self):
        return f"Student [id={self.id}, name={self.name}, passportNumber={self.passport_number}]"