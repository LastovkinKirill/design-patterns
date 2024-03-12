# origin:
# https://github.com/ArjanCodes/betterpython/blob/main/6%20-%20template%20method%20%26%20bridge/trading-before.py

from typing import List


class Application:
    """
    Here in should_buy and should_sell methods we violate two SOLID principles: SRP and OCP.

    SRP violation: Здесь класс Application отвечает за покупку (should_buy), за продажу (should_sell), за подключение.
    Правильней будет разделить это на свои классы, чтобы каждый отвечал за свою зону ответственности.

    OCP violation (potential): Здесь на текущей реализации мы используем два алгоритма покупки/продажи (minmax и average).
    А что если мы захотим дальше использовать новый алгоритм? Придется вносить изменения
    в уже используемый в продакшене класс Application и его методы should_buy и should_sell.
    Таким образом нарушаем принцип OCP, потому что есть шанс сломать уже текущее рабочее решение в новом релизе.
    Но если мы бы разделил бы это на классы, где каждый новый класс отвечал за свой алгоритм,
    то добавляя новый алгоритм, мы бы не исправляли ничего в уже используемых классах.
    Смотри after/main.py.
    """

    def __init__(self, trading_strategy="average"):
        self.trading_strategy = trading_strategy

    def connect(self):
        print(f"Connecting to Crypto exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 12, 18, 14]

    def list_average(self, l: List[float]) -> float:
        return sum(l) / len(l)

    # SRP and potential OCP violation
    def should_buy(self, prices: List[float]) -> bool:
        if self.trading_strategy == "minmax":
            return prices[-1] == min(prices)
        else:
            return prices[-1] < self.list_average(prices)

    # SRP and potential OCP violation
    def should_sell(self, prices: List[float]) -> bool:
        if self.trading_strategy == "minmax":
            return prices[-1] == max(prices)
        else:
            return prices[-1] > self.list_average(prices)

    def check_prices(self, coin: str):
        self.connect()
        prices = self.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}!")
        elif should_sell:
            print(f"You should sell {coin}!")
        else:
            print(f"No action needed for {coin}.")


application = Application("average")
application.check_prices("BTC/USD")
