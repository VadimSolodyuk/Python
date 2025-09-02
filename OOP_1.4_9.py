
input = '''1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200'''
lst_in = list(map(str.strip, input.splitlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for string in data:
            self.lst_data.append({self.FIELDS[i]:word for i, word in enumerate(string.split())})
        
    def select(self, a, b):
        return [item for index, item in enumerate(self.lst_data) if int(a) <= index <= int(b)]


db = DataBase()
db.insert(lst_in)