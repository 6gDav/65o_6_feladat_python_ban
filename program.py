import random as rmd
import statistics as stc
import os
import time
import threading

os.system("cls")

def futasi_t(func):
    def wrapper(*args, **kwargs):
        kz_t = time.time()
        result = func(*args, **kwargs)
        vgz_t = time.time()
        print(f"Program futasi ido: {vgz_t - kz_t}")
    return wrapper
#oszály
class Main:
    def __init__(self, szamok) -> int:
        self.szamok = szamok

    @property
    @futasi_t
    def neg_min(self)->str:
        neg = 0
        poz = 0
        for s in self.szamok:
            if s < 0 and s != 0:
                neg += 1
            else:
                poz += 1
        #return f"Pozitiv számok száma: {poz} és negativ szamok szama: {neg}"
        print("-")
        print(f"Pozitiv számok száma: {poz} és negativ szamok szama: {neg}")  
    
    @property
    @futasi_t
    def hets_szam(self):
        hetes = 0
        for s in self.szamok:
            if s == 7:
                hetes += 1
        #return f"Hetesek szama: {hetes}"
        print("-")
        print(f"Hetesek szama: {hetes}")
    
    @property
    @futasi_t
    def null_index(self):
        null_i = []
        for i, a in enumerate(self.szamok):
            if a == 0:
                null_i.append(i)
        print("-")
        print(f"A null értékű elemek indexei: {null_i}")

    @property
    @futasi_t
    def neg_avg(self):
        negs = []
        for s in self.szamok:
            if s<0:
                negs.append(s)
        atlag= stc.mean(negs)
        print("-")
        print(f"Negativ szamok átlaga {atlag}")
     
    @property
    @futasi_t    
    def poz_min(self):
        """
        min = self.szamok[0]
        for s in self.szamok:
            if s>min & s>0:
                 min = s
        print("-")
        print(f"Pozitivok kozott a legkisebb {min}")  
        """
        max_S = []
        for s in self.szamok:
            if s >0:
                max_S.append(s)
        print("-")
        print(f"Pozitiv kozott a legnagyobb {min(max_S)}")
     
      
    @property
    @futasi_t   
    def max_neg(self):
        """
        max = self.szamok[0]  
        for s in self.szamok:
            if s > max and s < 0 and s !=0:
                max = s
        print("-")
        print(f"Negativok kozott a legnagyobb {max}")
        """
        neg_S = []
        for s in self.szamok:
            if s <0:
                neg_S.append(s)
        print("-")
        print(f"Negativok kozott a legnagyobb {max(neg_S)}")
        
    def __str__(self):
        return f"{self.szamok}"
    
szamok = []
for i in range(28):
    szam = rmd.randint(-10, 10)
    szamok.append(szam)

os.system("cls")
if __name__ =="__main__":
    main = Main(szamok)
    print(main)
    t1 = threading.Thread(target=main.neg_min).start
    t2 = threading.Thread(target=main.hets_szam).start
    t3 = threading.Thread(target=main.null_index).start
    t4 = threading.Thread(target=main.neg_avg).start
    t5 = threading.Thread(target=main.poz_min).start
    t6 = threading.Thread(target=main.max_neg).start
