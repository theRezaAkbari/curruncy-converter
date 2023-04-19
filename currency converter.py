import requests
base_currency = ""
target_currency = ""
print("1)USD  2)ERU  3)GBP  4)IRR  5)AED  6)CNY  7)YEN")
choice=input("Chioce your base currency:")
if choice=="1":
  base_currency="USD"
elif choice=="2":
  base_currency="ERU"
elif choice=="3":
  base_currency="GBP"
elif choice=="4":
  base_currency="IRR"
elif choice=="5":
  base_currency="AED"
elif choice=="6":
  base_currency="CNY"
elif choice=="7":
  base_currency="YEN"

choice=input("Chioce your target currency:")
if choice=="1":
  target_currency="USD"
elif choice=="2":
  target_currency="ERU"
elif choice=="3":
  target_currency="GBP"
elif choice=="4":
  target_currency="IRR"
elif choice=="5":
  target_currency="AED"
elif choice=="6":
  target_currency="CNY"
elif choice=="7":
  target_currency="YEN"

amount=int(input("Enter amount: "))

url = f"https://api.apilayer.com/exchangerates_data/convert?to={target_currency}&from={base_currency}&amount={amount}"

payload = {}
headers= {
  "apikey": "nx7GZziJFRXWApG3LWk8BuZoJrVcSphj"
}

response = requests.request("GET",url,headers=headers,data=payload)

status_code = response.status_code
result = response.text
print(result)