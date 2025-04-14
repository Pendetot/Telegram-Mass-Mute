# MasVen Telegram Mass Mute

Script ini kubuat untuk menyelesaikan masalah yang sering kualami - kebanjiran notifikasi Telegram dari puluhan grup dan channel yang tak bisa kuhapus karena masih perlu kuakses sesekali. Daripada harus mute satu per satu secara manual (yang butuh waktu lama), tool ini akan otomatis mute semua grup, channel, dan bot Telegram dengan sekali jalan.

## Untuk Apa Tool Ini?

Tool ini berguna buat kamu yang:
- Punya banyak grup dan channel Telegram yang berisik
- Malas mute satu-satu secara manual
- Ingin fokus tanpa diganggu notifikasi

Script ini cukup dijalankan sekali, dan semua notifikasi dari grup/channel/bot akan otomatis dimatikan. Hemat waktu, hemat tenaga.

## Cara Install

Gampang banget:

1. Clone repo ini
```
git clone https://github.com/masven/telegram-mass-mute
cd telegram-mass-mute
```

2. Install yang dibutuhkan
```
pip install -r requirements.txt
```

## Cara Pakai

1. Jalankan script
```
python masven_mass_mute.py
```

2. Pertama kali pakai, kamu perlu masukkan API ID dan API Hash Telegram. Dapatkan dari https://my.telegram.org

3. Login ke akun Telegram kamu (pakai nomor HP)

4. Duduk santai sambil lihat script bekerja - bakal muncul progress bar yang nunjukin berapa grup yang sudah di-mute

5. Selesai! Script akan memberi tahu berapa total grup yang berhasil di-mute

Setelah pertama kali pakai, script bakal simpan API ID dan Hash kamu di file data.py. Jadi kalo mau jalanin lagi (misal buat akun lain atau setelah join grup baru), tinggal jalanin script tanpa perlu masukin API lagi.

Catatan: Ini cuma mute notifikasi, bukan keluar grup. Kamu masih bisa akses semua grup/channel kapan aja, cuma gak bakal diganggu notifikasi.

Kalau ada masalah atau saran, silakan buka issue di repo ini atau langsung DM gw di Telegram: @masven

Selamat menikmati ketenangan dari notifikasi Telegram yang berisik!