def find_cheapest_flight(prices):

    clean_prices = []

    for p in prices:

        # ignore lock price lines
        if "@" in p:
            continue

        # remove currency and comma
        p = p.replace("₹", "").replace(",", "").strip()

        try:
            clean_prices.append(int(p))
        except:
            continue

    cheapest = min(clean_prices)

    return cheapest
