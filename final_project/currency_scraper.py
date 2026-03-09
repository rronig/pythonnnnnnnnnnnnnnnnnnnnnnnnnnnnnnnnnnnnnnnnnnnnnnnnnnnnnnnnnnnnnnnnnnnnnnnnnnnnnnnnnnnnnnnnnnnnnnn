# currency_scraper.py
import requests
import streamlit as st
from datetime import datetime, timedelta


# Cache for exchange rates to avoid too many requests
@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_exchange_rates():
    """
    Fetch exchange rates from Frankfurter API (free, no API key required)
    Returns a dictionary of currency: rate relative to USD
    """
    try:
        # Frankfurter API - free and reliable
        url = "https://api.frankfurter.app/latest?from=USD"

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            rates = data['rates']
            # Add USD itself
            rates['USD'] = 1.0

            # Get the date from the response
            date = data.get('date', datetime.now().strftime("%Y-%m-%d"))

            return rates, date

        else:
            print(f"API returned status code: {response.status_code}")
            return get_fallback_rates(), datetime.now().strftime("%Y-%m-%d")

    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
        return get_fallback_rates(), datetime.now().strftime("%Y-%m-%d")


@st.cache_data(ttl=86400)  # Cache for 24 hours
def get_historical_rates(base_currency='USD', days=7):
    """
    Fetch historical exchange rates for the last N days
    """
    try:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        url = f"https://api.frankfurter.app/{start_date.strftime('%Y-%m-%d')}..{end_date.strftime('%Y-%m-%d')}?from={base_currency}"

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return data['rates']
        else:
            return None

    except Exception as e:
        print(f"Error fetching historical rates: {e}")
        return None


def get_fallback_rates():
    """Provide fallback rates if API fails"""
    return {
        'USD': 1.0,
        'EUR': 0.92,
        'GBP': 0.79,
        'JPY': 148.50,
        'CHF': 0.89,
        'CAD': 1.35,
        'AUD': 1.52,
        'CNY': 7.19,
        'INR': 83.12,
        'MXN': 17.05,
        'BRL': 5.02,
        'KRW': 1330.50,
        'SGD': 1.34,
        'NZD': 1.63,
        'TRY': 30.25,
        'ZAR': 18.90
    }


def convert_currency(amount, from_currency, to_currency, rates):
    """Convert amount between currencies"""
    if from_currency == to_currency:
        return amount

    # Convert to USD first then to target currency
    if from_currency != 'USD':
        # If from_currency is not USD, convert to USD first
        usd_amount = amount / rates.get(from_currency, 1.0)
    else:
        usd_amount = amount

    # Convert USD to target currency
    if to_currency != 'USD':
        converted = usd_amount * rates.get(to_currency, 1.0)
    else:
        converted = usd_amount

    return converted


def get_popular_currencies():
    """Return list of popular currencies"""
    return ['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'CAD', 'AUD', 'CNY', 'INR', 'MXN', 'BRL', 'KRW', 'SGD', 'NZD', 'TRY',
            'ZAR']


def get_currency_flags():
    """Return currency flags for display"""
    flags = {
        'USD': '🇺🇸', 'EUR': '🇪🇺', 'GBP': '🇬🇧', 'JPY': '🇯🇵', 'CHF': '🇨🇭',
        'CAD': '🇨🇦', 'AUD': '🇦🇺', 'CNY': '🇨🇳', 'INR': '🇮🇳', 'MXN': '🇲🇽',
        'BRL': '🇧🇷', 'KRW': '🇰🇷', 'SGD': '🇸🇬', 'NZD': '🇳🇿', 'TRY': '🇹🇷',
        'ZAR': '🇿🇦'
    }
    return flags


def get_currency_names():
    """Return full currency names"""
    names = {
        'USD': 'US Dollar',
        'EUR': 'Euro',
        'GBP': 'British Pound',
        'JPY': 'Japanese Yen',
        'CHF': 'Swiss Franc',
        'CAD': 'Canadian Dollar',
        'AUD': 'Australian Dollar',
        'CNY': 'Chinese Yuan',
        'INR': 'Indian Rupee',
        'MXN': 'Mexican Peso',
        'BRL': 'Brazilian Real',
        'KRW': 'South Korean Won',
        'SGD': 'Singapore Dollar',
        'NZD': 'New Zealand Dollar',
        'TRY': 'Turkish Lira',
        'ZAR': 'South African Rand'
    }
    return names