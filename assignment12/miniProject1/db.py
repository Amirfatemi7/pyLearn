
class Data_base:
    def __init__(self, addr):
        self.addr = addr
        self.data = []
    def read(self):
        f = open(self.addr, 'r')

        for line in f:
            result = line.split(',')
            my_obj = Product(result[0], result[1], result[2], result[3])
            self.data.append(my_obj)

        f.close()

    def write(self):
        f = open(self.addr, 'w')
        f.write(self.data)
        f.close()