print ("==============================Toko Serba Ada======================================")
penjual = input("Nama Penjual : ")
print("===============================Selamat datang ditoko Bapak Udin====================")
pembeli = input("Nama Pembeli : ")
nama = input("Masukkan Nama Barang : ")
x = int(input("Masukkan Harga Barang : "))
jumlah_barang = int(input("Masukkan jumlah barang = "))
berat_barang = int(input("Masukkan berat barang = "))
total = x*jumlah_barang*berat_barang
print("Total Harga", nama, "Anda adalah Rp.",total)
pembayaran = int(input("Tunai = "))
kekurangan = total-pembayaran
if(pembayaran>total):
	print("===========================Terimakasih telah datang ke Toko kami===============")
	print("kembali Rp.", pembayaran-total)
else:
	print("Anda memiliki kekurangan sebesar Rp.",kekurangan)