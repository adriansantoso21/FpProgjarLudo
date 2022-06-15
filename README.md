# FpProgjarLudo

### Anggota Kelompok :
1. 05111940000080 Kelvin Andersen
2. 05111940000120 Jonathan Timothy 
3. 05111940000130 Adrian Santoso 
4. 05111940000157 Kevin Davi Samuel
5. 05111940000206 Samuel Hamonangan
6. 05111940000211 Vicky Thirdian
7. 05111940000220 Marsa Aushaf Rafi

### Cara Menjalankan Program :  
- Install dependency yang dibutuhkan pygame, plyer dan mixer  
```pip install pygame```  
```pip install plyer```  
```pip install mixer```  
- Run server.py
- Run start.py karena ludo akan dimainkan oleh 4 orang maka run start.py sebanyak 4 kali
- Pada home ui, klik tombol 'Play'
- Pada regis ui, pemain mengisi username dan email
- Pada game ui, pada putaran pertama bermain akan dilakukan penentuan urutan bermain
- Kemudian, pemain bermain ludo sesuai aturan bermain menurut urutan yang telah ditentukan
- Ketika menyelesaikan permainan, pemain akan menerima pop up untuk menerima email atau tidak

### Aturan Bermain :
1. Urutan bermain ditentukan oleh angka dadu tertinggi. Pemain dengan angka dadu tertinggi akan berjalan terlebih dahulu
2. Arah urutan bermain pemain searah jarum jam 
3. Untuk menggerakkan pion dari posisi awal / base dibutuhkan angka dadu 6
4. Jika pemain mendapatkan angka dadu 6 sebanyak 3 kali maka gilirannya akan dialihkan ke pemain selanjutnya 
5. Pemain harus menggerakkan pion sesuai dengan angka dadu yang didapat
6. Jika posisi pion pemain ditempati oleh pion pemain lain, kemudian pion dipindahkan ke posisi awal

### Fitur :
- Client & Server
- Socket
- Pickle
- Chat antar pemain
- Smtp email

### Penjelasan Folder :
- Asset  
Resources yang dibutuhkan oleh aplikasi seperti gambar dan musik
- Data  
Data dari masing-masing player seperti chat, pion pemain, nama email pemain, dll
- Entity  
Class yang digunakan untuk menampung data  
- Logic  
Berupa client dan server yang berkomunikasi melalui socket yang berisi logika permainan
- Ui  
Berupa tampilan aplikasi yang dilihat oleh pemain yang menerima data dari socket

### Tampilan Aplikasi
1. Home Ui  
Halaman awal aplikasi di mana user dapat memilih untuk bermain, melihat ruleUi, dan exit untuk keluar
![alt text](https://github.com/adriansantoso21/FpProgjarLudo/blob/main/asset/readmeImg/img.png?raw=true)
2. Rule Ui  
Halaman yang menunjukkan peraturan untuk bermain ludo
![alt text](https://github.com/adriansantoso21/FpProgjarLudo/blob/main/asset/readmeImg/img_1.png?raw=true)
3. Regis Ui  
Halaman dimana pemain mendaftarkan username untuk bermain dan email yang digunakan untuk memberikan notifikasi ketika berhasil menyelesaikan permainan
![alt text](https://github.com/adriansantoso21/FpProgjarLudo/blob/main/asset/readmeImg/img_2.png?raw=true)
4. Game Ui  
Halaman dimana pemain bermain ludo dan dapat melakukan chat pada pemain lainnya
![alt text](https://github.com/adriansantoso21/FpProgjarLudo/blob/main/asset/readmeImg/img_3.png?raw=true)
5. Notifikasi email  
Notifikasi yang dikirimkan ke email player ketika menyelesaikan permainan
![alt text](https://github.com/adriansantoso21/FpProgjarLudo/blob/main/asset/readmeImg/img_4.png?raw=true)
