'''
# bikin program yg bisa diakses di file lain (lanjut di file 'Day11Task_2')
import datetime as dt
x = dt.datetime.now()
listHari = {
    'Monday': 'Senin', 'Tuesday': 'Selasa', 'Wednesday': 'Rabu',
    'Thursday': 'Kamis', 'Friday': 'Jumat', 'Saturday': 'Sabtu',
    'Sunday': 'Minggu'}
listBulan = {
    'January': 'Januari', 'February': 'Februari', 'March': 'Maret',
    'April':'April', 'May': 'Mei', 'June': 'Juni', 'July': 'Juli',
    'August': 'Agustus', 'September': 'September', 'October': 'Oktober',
    'November': 'November', 'December': 'Desember'}

class asr:
    def __init__(self):
        self.hari = listHari[x.strftime('%A')]
        self.tanggal = x.strftime('%d')
        self.bulan = listBulan[x.strftime('%B')]
        self.tahun = x.strftime('%Y')
        self.jam = x.strftime('%H')
        self.menit = x.strftime('%M')
        self.detik = x.strftime('%S')

waktu = asr()
'''


# bikin mean, median, modus tanpa modul statistik
from functools import reduce
class Statistik:
    def rataRata(self, x):
        total = reduce(lambda a, b: a+b, x)
        return total / len(x)
    def nilaiTengah(self, x):
        x.sort()
        if len(x) % 2 != 0:
            iTengah = [int(len(x)/2)]
        else:
            iTengah = [int(len(x)/2) - 1, int(len(x)/2)]
        aTengah = list(map(lambda a : x[a], iTengah))
        total = reduce(lambda x, y: x+y, aTengah)
        return total / len(aTengah)
    def nilaiTerbanyak(self, x):
        a = []
        for i in x:
            b = x.count(i)
            a.append(b)
        c = max(a)
        d = x[a.index(c)]
        return d

stat = Statistik()
print(stat.nilaiTerbanyak([2, 7, 5, 5, 7]))