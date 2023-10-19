import httpx

STOCK_SERVICE_HOST_URL = "http://0.0.0.0:8001/api/v1/stocks/"
USER_SERVICE_HOST_URL = "http://0.0.0.0:8000/api/v1/users/"


def count_price(stocks):
    url = STOCK_SERVICE_HOST_URL
    price = 0
    for stock in stocks:
        stock = int(stock)
        price += httpx.get(f"{url}{stock}").price
    return price


def update_user_bank_count(id_user: int, delta: int):
    url = USER_SERVICE_HOST_URL + "update/"
    httpx.post(
        f"{url}{id_user}",
        data={"id": 1, "delta": delta},
    )
