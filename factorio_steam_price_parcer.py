import requests
import datetime
from bs4 import BeautifulSoup


def main():
    r = requests.get("https://store.steampowered.com/app/427520/Factorio/")
    soup = BeautifulSoup(r.text)
    soup_id = soup.find(id='game_area_purchase_section_add_to_cart_88199')
    discount_price = soup_id.find(attrs={"class": "discount_final_price"})
    normal_price = soup_id.find(attrs={"class": "game_purchase_price"})
    current_time = datetime.datetime.now().strftime('%Y.%m.%d %H:%M')

    if discount_price is not None:
        print(current_time, "Discount price", discount_price.text.strip())
    elif normal_price is not None:
        print(current_time, "Normal price", normal_price.text.strip())
    else:
        print(current_time, "Something went wrong")


if __name__ == '__main__':
    main()
