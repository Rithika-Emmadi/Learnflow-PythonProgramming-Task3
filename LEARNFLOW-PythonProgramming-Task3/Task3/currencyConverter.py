import requests


def converter(fromCurr, toCurr, amount):

    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    currencies = data["rates"]

    if fromCurr != "IND":
        amount = amount / currencies[fromCurr]
    result = round(amount * currencies[toCurr], 2)

    return result


def currenyConverter():
    # install(requests)
    # os.system("pip install requests:")
    print("Some of the famous currency symbols:")
    curr_codes = (
        ("INR - Indian Rupee", "USD- United States Dollar", "AUD - Australia Dollar"),
        ("NZD - Newzealand Dollar", "JPY - Japan Yen", "KPW - Korea(south) Won"),
        ("RUB - Russia Ruble", "SGD - Singapore Dollar", "GBP - United Kingdom Pound"),
    )
    for codes in curr_codes:
        print(codes)
    fromCurr = input("From currency: ")
    toCurr = input("To currency: ")
    amount = int(input("Amount: "))
    print(converter(fromCurr, toCurr, amount))


currenyConverter()
