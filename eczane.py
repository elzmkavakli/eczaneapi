import http.client
conn = http.client.HTTPSConnection("api.collectapi.com")
import json
headers = {
    'content-type': "application/json",
    'authorization': "apikey 5tCBxAFxdnYeuY5eSZMpKT:2g7n15R9k4ootHADsjl6Vz"
    }
#il ve ilce ayarlamasi yapiliyor
il=input("İl Giriniz:")
if il=="":
    print("İl Boş bırakılırsa Elazig İline ait veriler gelecek")
    il="Elazig"
else:
    il=il.strip().capitalize()
ilce=input("İlçe giriniz")
if ilce=="":
    print("İl Boş bırakılırsa Merkez ait ilk veri gelecek")
    ilce="Merkez"
else:
    ilce=ilce.strip().capitalize()
print(il,ilce)
adres="/health/dutyPharmacy?ilce="+ilce+"&il="+il
conn.request("GET",adres, headers=headers)
res = conn.getresponse()
data = res.read()

veri=data.decode("utf-8")
json_veri=json.loads(veri)
#print(json_veri)
if json_veri["success"]==True:
    bilgi1=json_veri["result"][0]
    print("Eczane Adı:"+bilgi1["name"]+"\nAdresi:"+bilgi1["address"]+"\nTelefonu:"+bilgi1["phone"])
else:
    print("Başarısız")