import json

class CsvReader():
    def __init__(self, text = '',\
        sep=',', header=False, skip_top=0, skip_bottom=0):
        self.header = header
        self.sep = sep
        self.text = text
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
    
    def __enter__(self):
        self.text = open(self.text, "r")
        size = 0
        for line in self.text:
            test = line.split(self.sep)
            if size and size != len(test):
                return None  
            size = len(test)
        self.text.seek(0,0)
        return self.text

    def __exit__(self, exception_type, exception_value, traceback):
        self.text.close()
    
    def getdata(self):
        data = []
        ind = 0
        if header == True:
            ind += 1
        ind += skip_top
        for line in self.text[ind:-skip_bottom]:
            data.append(line.split(self.sep))
        return data
    # def getheader(self):

with CsvReader('good.csv') as file:
    if not file:
        print('NONE')
    else:
        # print(file.read())
        file.getdata()