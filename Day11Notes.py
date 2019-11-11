'''
# MULTILEVEL INHERITANCE CLASS
class X:
    def __init__(self, x):
        self.x = x

class Y(X):
    def __init__(self, x, y):
        X.__init__(self, x)
        self.y = y

class Z(Y):
    def __init__(self, x, y, z):
        Y.__init__(self, x, y)
        self.z = z

objA = Z('Andi', 'PNS', True)
objB = Y('Yuni', 'Wira')
print(vars(objA))
print(vars(objB))



# MULTIPLE HERITANCE (sebuah kelas yg inherit ke dua kelas yg kedua kelas itu tidak saling terhubung)
class Karnivora:
    def __init__(self):         # ga perlu pake objek dibelakang self, karena self nya udah paten
        self.daging = True
        self.nama = 'Karnivora'

class Herbivora:
    def __init__(self):
        self.tumbuhan = True
        self.nama = 'Herbivora'

class Omnivora(Karnivora, Herbivora):
    def __init__(self):
        Herbivora.__init__(self)
        Karnivora.__init__(self)
        self.McD = True
        self.nama = 'Omnivora'

objA = Omnivora()
print(vars(objA))
print(objA.nama)        # nama yg keluar itu yg ada di kelas tersebut, atau kalo di kelas tersebut ga ada maka munculnya nama yg di subclass init terakhir (Karnivora)

# buat ngeliat urutan order di sebuah kelas
print(Omnivora.__mro__)



# akses file python dari file python lain (lanjut di file 'lanjut')
nama = 'Andi'
usia = 24

def halo(a):
    return f'Halo {a}'

class Test:
    nama = 'Andra'



# Datetime
import datetime as dt
x = dt.datetime.now()

print(x)
# print hanya sebagian
print(x.strftime('%d'))     # tanggal
print(x.strftime('%A'))     # hari
print(x.strftime('%m'))     # bulan
print(x.strftime('%B'))     # nama bulan
print(x.strftime('%Y'))     # tahun

print(x.strftime('%H'))     # jam sistem 24 jam
print(x.strftime('%I'))     # jam sistem 24 jam
print(x.strftime('%p'))     # am/pm
print(x.strftime('%M'))     # menit
print(x.strftime('%S'))     # detik

print(x.strftime('%c'))     # waktu lengkap
print(x.strftime('%x'))     # tgl/bln/thn
print(x.strftime('%X'))     # jam/min/sec


print(x.strftime('Sekarang jam %H:%M:%S WIB'))
print(x.strftime('Hari ini hari %A'))



# Statistik
import statistics

x = [1, 3, 9, 2, 6, 4, 7, 8, 5, 5]
print(statistics.mean(x))       # mencari rata-rata
print(statistics.median(x))     # mencari nilai tengah
print(statistics.mode(x))       # mencari nilai yg paling banyak muncul
'''