# init по умолчанию ждет аргументов
# repr возвращает строку по которой видно (и можно воссоздать) состояния объекта
# str возвращает строку
# если не реализованы репр и стр, то будет возвращен адрес в памяти
# eq по умолчанию сравнивает адрес в памяти, в реализации лучше сразу проверить тип
# если методы сравнения не реализованы то падает ошибка
# contains для реализации проверки IN
# bool для самодельных объектов всегда вернет True, для изменения поведения нужно написать __bool__
# len вернет ошибку если не переопределить метод __len__
# чтобы объект стал вызываемым (callable) нужно реализовать __call__,иначе ошибка
# __iter__ возвращет объект итератор, тот кто реализует итер = Итерабл
# __next__ должен вернуть следущий обьет из контейнера, кто его реализует = Итератор, for работает до StopIteration
# __getitem__ нужен для функционала [] (аналог списка и словаря) __setetiem__ для присвоения через [], если релизовать = ошибка
#если в объекте не реализован __iter__ то для фор будет __getitem__ там ожидается падение IndexError




class Banknote:
    def __init__(self,value: int):
        self.value = value

    def __repr__(self):
        return f'Banknote({self.value})'

    def __str__(self):
        return f'Банкнота номиналом в {self.value} рублей'

    def __eq__(self, other):
        if other is None or not isinstance(other,Banknote):
            return False
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

class Iterator:
    def __init__(self,container):
        self.container = container
        self.index = 0

    def __next__(self):
        if 0 <= self.index < len(self.container):
            value = self.container[self.index]
            self.index +=1
            return value
        raise StopIteration


class Wallet:
    def __init__(self,*banknotes:Banknote):
        self.container = []
        self.container.extend(banknotes)
        self.index = 0

    def __repr__(self):
        return f'Wallet({self.container})'

    def __contains__(self, item):
        return item in self.container

    def __bool__(self):
        return len(self.container) > 0

    def __len__(self):
        return len(self.container)

    def __call__(self):
        return f'{sum(e.value for e in self.container)} рублей'

    def __iter__(self):
        return Iterator(self.container)

    def __getitem__(self, item:int):
        if item < 0 or item > len(self.container):
            raise IndexError
        return self.container[item]

    def __setitem__(self, key:int, value:Banknote):
        if key < 0 or key > len(self.container):
            raise IndexError
        self.container[key] =  value

if __name__=='__main__':
    banknote = Banknote(50)
    fifty = Banknote(50)
    hundred = Banknote(100)
    wallet = Wallet(fifty,hundred)
    wallet[0] = Banknote(500)
    print(wallet[0])