def convert_price_to_int(price: str) -> int:
    multiplier = 1
    if price.endswith('M'):
        multiplier = 1_000_000
        price = price[:-1]
    elif price.endswith('K'):
        multiplier = 1_000
        price = price[:-1]
    return int(float(price) * multiplier)

