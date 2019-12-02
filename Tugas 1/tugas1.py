import re
import mechanize
import urllib.request
import os


br = mechanize.Browser()

linkList= []
dictionary= {}
values=1

tgl1 = 1
tgl2 = 1
bln1 = 3
bln2 = 3
thn1 = 2016
thn2 = 2016
tahun = thn1
bulan = bln1
tanggal = tgl1
halaman = 1
count = 0

def checkKey(dictionary, key):
    if key in dictionary:
        print("ada yang sama ")
    else:
        print("data dimasukan")

while(tahun<=thn2):
    print("tahun",tahun)
    tahun+=1
    while(bulan<=bln2):
        print("bulan", bulan)
        bulan+=1
        while(tanggal<=tgl2):
            print("tanggal", tanggal)
            tanggal+=1
            while(halaman<=5):
                print("halaman", halaman)
                halaman+=1
                if tanggal < 10:
                    if bulan < 10:
                        r = br.open("https://news.detik.com/indeks/all/"+ str(halaman)+ "?date=0"+ str(bulan)+ "/0"+ str(tanggal) + "/" + str(tahun))
                    else:
                        r = br.open("https://news.detik.com/indeks/all/"+ str(halaman)+ "?date="+ str(bulan)+ "/0"+ str(tanggal)+"/"+ str(tahun))
                else:
                    if bulan <10:
                        r = br.open("https://news.detik.com/indeks/all/"+ str(halaman)+ "?date=0"+ str(bulan)+ "/"+ str(tanggal)+"/"+ str(tahun))
                    else:
                        r = br.open("https://news.detik.com/indeks/all/"+ str(halaman)+ "?date="+ str(bulan)+ "/"+ str(tanggal)+"/"+ str(tahun))

                for link in br.links(url_regex='/d-'):
                    linkList.append(link.url)
                
                for links in linkList:
                    if links not in dictionary and re.search(r"/berita/",links):
                        dictionary[links]=values
                        # simpen waktunya lebih baik dari 1 == timestamp
                        # jumlah url
                        # escape yang ada %20 di url wkwk
                        count+=1
                    else:
                        pass



f = open("linknya.txt","w")
for x in dictionary:
    f.write(x + "\n")

print("berhasil mendapat", count, "url")

f.close()

pilih = input("Apakah anda ingin langsung mendownload halaman dari link yang telah didapat Y/N:")
print("anda memilih", pilih)
if pilih == "Y" or pilih == "y":
    print("---------menjalankan cobatugas.py---------")
    os.system("python3 cobatugas.py")
    print("---------selesai menjalankan cobatugas.py---------")
else:
    print("anda jalanin sendiri wkwk")





