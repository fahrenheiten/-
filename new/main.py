# 1) _dict_ - это атрибут объектов в питоне, который хранит состояние
# 2) _setattr_ вызывается при попытке установить атрибут
# 3) property - это удобный механизм создания геттеров и сеттеров
# 4) _slots_ - создан для уменьшения памяти, занимаемой объектами, но как побочное свойство -не даст добавить объекту новый атрибу
class Cat:
    __slots__ = ('_name','_age')

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if not value:
            raise AttributeError('Name cant be empty!')
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
       if value < 1 or value > 15 :
           raise AttributeError('Age should be in 1-15')
       self._age = value

    def __repr__(self):
        return f'Cat(name = {self.name},age = {self.age})'

    # def __setattr__(self, key, value):
    #     if key not in self.FIELDS:
    #         raise AttributeError(f'Only allowed {self.FIELDS}')
    #     if key == 'name' and not value:
    #         raise AttributeError('Name cant be empty!')
    #     if key == 'age' and (value < 1 or value > 15):
    #         raise AttributeError('Age should be in 1-15')
    #     self.__dict__[key] = value


if __name__ == '__main__':
    tom = Cat('Tom',15)
    print(tom)