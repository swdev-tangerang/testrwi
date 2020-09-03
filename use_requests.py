import requests

url = "https://detik.com"
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Sukses {response.status_code}")
        print(f"Contentnya : {response.text}")
    else:
        print("Ada kesalahan waktu get.")
except Exception as e:
    print("Ada error: ", e)
