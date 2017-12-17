print ("==============================Toko Serba Ada======================================")

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