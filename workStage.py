import json
import base64
import zipfile
import os

# JSON dosyasını yükleme
with open('input_data.json', 'r') as json_file:
    json_data = json.load(json_file)

# JSON verisini string formatına çevir
json_string = json.dumps(json_data)

# JSON string'ini Base64 formatına çevir
base64_encoded = base64.b64encode(json_string.encode('utf-8')).decode('utf-8')

# Base64 verisini .txt dosyasına yaz
txt_filename = 'base64_data.txt'
with open(txt_filename, 'w') as txt_file:
    txt_file.write(base64_encoded)

# .txt dosyasını zip dosyasına ekle
zip_filename = 'output_data.zip'
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.write(txt_filename)

# Kullandığımız geçici .txt dosyasını silelim (isteğe bağlı)
os.remove(txt_filename)

print(f"{zip_filename} dosyası oluşturuldu ve Base64 verisi içeriyor.")
