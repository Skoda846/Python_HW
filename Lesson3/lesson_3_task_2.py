from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79001234567"),
    Smartphone("Samsung", "Galaxy S23", "+79007654321"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79004567890"),
    Smartphone("Google", "Pixel 7", "+79009876543"),
    Smartphone("OnePlus", "Nord 3", "+79003456789"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")