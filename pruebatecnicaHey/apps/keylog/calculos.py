
class KeyLog(object):
    def __init__(self, data=None):
        if data is not None:
            self.data=set(data)
        else:
            self.data = self.dataRead()
        self.dig = self.digitO()

    def dataRead(self):
        return set([str(num.rstrip()) for num in open("documentos/keylog.txt", "r")])
        
    def digitO(self):
        dig = set()
        for dat in self.data: [dig.add(c) for c in dat]
        return dig

    def nSucc(self):
        nSucc = []
        for num in self.dig:
            suc_c = []
            for dat in self.data:
                try:
                    index = dat.index(num)
                    suc_c.extend(list(dat[index+1:]))
                except ValueError:
                    continue
            nSucc.append((len(set(suc_c)), num))
        return nSucc

    def passw(self):
        passw = ''.join([n[1] for n in sorted(self.nSucc(), reverse=True)])
        return passw
