import openpyxl
import json
class Changeling():
    def __init__(self, list):
        self.list = list
    def dic_t(self):
        return dict(enumerate(self.list, 1))

    def file_w(self):
        dat = open("test_2", 'w', encoding='utf-8')
        print(self.dic_t(), file=dat)
        print('Файл записан', self.dic_t())
        dat.close()
    def file_r(self):
        dat = open("test_2", 'r', encoding='utf-8')
        print('Файл считан', dat.read())
        dat.close()
    def file_w_x(self):
        book = openpyxl.Workbook()
        sheet = book.active
        sheet["A1"] = json.dumps(self.dic_t())
        print('Excel записан, имя файла "test_8"')
        book.save('test_8.xlsx')
        book.close()
    def file_r_x(self):
        book = openpyxl.open('test_8.xlsx', read_only=True)
        sheet = book.active
        print('Файл Excel "test_8" считан', json.loads(sheet["A1"].value), type(json.loads(sheet["A1"].value)))
        book.close()

a = Changeling([1, 2, 3])
a.file_w()
a.file_r()
a.file_w_x()
a.file_r_x()











