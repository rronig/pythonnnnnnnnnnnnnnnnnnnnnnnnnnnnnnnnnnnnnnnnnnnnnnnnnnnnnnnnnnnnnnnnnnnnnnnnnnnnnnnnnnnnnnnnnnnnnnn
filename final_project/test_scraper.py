# test_scraper.py
from currency_scraper import get_exchange_rates, convert_currency


def test_scraper():
    print("Testing currency scraper...")
    rates, timestamp = get_exchange_rates()

    if rates:
        print(f"✅ Successfully fetched rates at {timestamp}")
        print("\nCurrent exchange rates (per USD):")
        for currency, rate in rates.items():
            if currency != 'USD':
                print(f"  {currency}: {rate:.4f}")

        # Test conversion
        amount = 100
        from_curr = 'USD'
        to_curr = 'EUR'
        result = convert_currency(amount, from_curr, to_curr, rates)
        print(f"\n✅ Conversion test: {amount} {from_curr} = {result:.2f} {to_curr}")
    else:
        print("❌ Failed to fetch rates")


if __name__ == "__main__":
    test_scraper()