import streamlit as st
import requests
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="MathPro", page_icon="🧮", layout="wide")

# Session state
if "page" not in st.session_state:
    st.session_state.update({
        "page": "Login",
        "logged_in": False,
        "username": "",
        "membership": "",
        "history": []
    })

# Main container
main_container = st.container()

with main_container:
    if st.session_state.page == "Register":
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("### Create Account")

            # Username input outside form for better UX
            username = st.text_input("Username", key="reg_username")
            password = st.text_input("Password", type="password", key="reg_password")

            # Plan selection outside form so it updates immediately
            membership = st.selectbox("Plan", ["Quid", "Pro", "Quo"], key="reg_plan")

            # Features and price - these will update immediately when plan changes
            st.markdown("**Features & Pricing:**")
            features = {
                "Quid": ["Basic addition"],
                "Pro": ["Addition", "Subtraction"],
                "Quo": ["Addition", "Subtraction", "Multiplication", "Division", "Graphing", "Analysis", "Currency conversion"]
            }
            price = {
                "Quid": "💰 One reduced Planck constant cent per Hypermassive Black hole evaporation",
                "Pro": "💰 $20 per month",
                "Quo": "💰 TREE(googolplex^G) dollars per quectosecond"
            }

            # Create a nice looking container for the features
            with st.container():
                st.markdown(f"**Selected Plan: {membership}**")
                for f in features[membership]:
                    st.markdown(f"✓ {f}")
                st.markdown(f"_{price[membership]}_")

            st.divider()

            # Mock Payment Section - Only shown when a plan is selected
            st.markdown("### Payment Information")
            st.caption("🔒 This is a mock payment - no real charges will be processed")

            # Create a payment form
            with st.form(key="payment_form"):
                # Card details in columns
                col_card1, col_card2 = st.columns(2)
                with col_card1:
                    card_number = st.text_input("Card Number",
                                                placeholder="4111 1111 1111 1111",
                                                help="Mock payment - use any number")
                with col_card2:
                    card_name = st.text_input("Cardholder Name",
                                              placeholder="John Doe")

                col_exp1, col_exp2, col_cvv = st.columns([1, 1, 1])
                with col_exp1:
                    exp_month = st.selectbox("Expiry Month",
                                             options=[f"{i:02d}" for i in range(1, 13)],
                                             index=0)
                with col_exp2:
                    exp_year = st.selectbox("Expiry Year",
                                            options=[str(i) for i in range(2024, 2035)],
                                            index=0)
                with col_cvv:
                    cvv = st.text_input("CVV",
                                        placeholder="123",
                                        type="password",
                                        max_chars=3,
                                        help="3-digit security code")

                # Billing address
                st.markdown("**Billing Address**")
                address = st.text_input("Street Address", placeholder="123 Main St")

                col_city1, col_city2, col_zip = st.columns([2, 1, 1])
                with col_city1:
                    city = st.text_input("City", placeholder="New York")
                with col_city2:
                    state = st.text_input("State", placeholder="NY", max_chars=2)
                with col_zip:
                    zip_code = st.text_input("ZIP", placeholder="10001", max_chars=5)

                # Add some visual separation
                st.divider()

                # Submit button inside form
                submitted = st.form_submit_button("Process Payment & Create Account",
                                                  use_container_width=True,
                                                  type="primary")

            # Handle form submission
            if submitted:
                if not username or not password:
                    st.error("Please enter both username and password")
                elif not card_number or not card_name or not cvv or not address or not city or not state or not zip_code:
                    st.error("Please fill in all payment information")
                else:
                    # Basic validation for mock payment
                    if len(cvv) != 3 or not cvv.isdigit():
                        st.error("CVV must be 3 digits")
                    elif len(zip_code) != 5 or not zip_code.isdigit():
                        st.error("ZIP code must be 5 digits")
                    else:
                        # Show processing animation
                        with st.spinner("Processing payment and creating account..."):
                            # Mock payment processing - simulate a delay
                            import time
                            import requests
                            from requests.adapters import HTTPAdapter
                            from urllib3.util.retry import Retry

                            time.sleep(1)

                            # Prepare the data for the API endpoint
                            registration_data = {
                                "username": username,
                                "password": password,
                                "membership": membership,
                                "payment_data": {
                                    "card_number": card_number,
                                    "cardholder_name": card_name,
                                    "expiry_month": exp_month,
                                    "expiry_year": exp_year,
                                    "cvv": cvv,
                                    "street_address": address,
                                    "city": city,
                                    "state": state,
                                    "zip_code": zip_code
                                }
                            }

                            # Create a session with retry strategy
                            session = requests.Session()
                            retry_strategy = Retry(
                                total=2,
                                backoff_factor=0.5,
                                status_forcelist=[500, 502, 503, 504]
                            )
                            adapter = HTTPAdapter(max_retries=retry_strategy)
                            session.mount("http://", adapter)
                            session.mount("https://", adapter)

                            try:
                                # First check if server is reachable
                                try:
                                    health_check = session.get("http://127.0.0.1:8000", timeout=2)
                                except:
                                    # If root doesn't exist, try a simple endpoint
                                    pass

                                # Make API call to register with payment - with longer timeout
                                response = session.post(
                                    "http://127.0.0.1:8000/register-with-payment",
                                    json=registration_data,
                                    timeout=30  # Increased timeout
                                )

                                if response.status_code == 200:
                                    st.success("✅ Payment processed and account created successfully!")

                                    # Small delay to ensure database is updated
                                    time.sleep(1)

                                    # Now log the user in automatically
                                    login_response = session.post(
                                        "http://127.0.0.1:8000/login",
                                        json={"username": username, "password": password},
                                        timeout=10
                                    )

                                    if login_response.status_code == 200:
                                        data = login_response.json()
                                        st.session_state.update({
                                            "logged_in": True,
                                            "username": data["token"],
                                            "membership": data["membership"],
                                            "page": "Calculator"
                                        })
                                        st.balloons()
                                        st.rerun()
                                    else:
                                        st.warning("Account created! Please log in manually.")
                                        if st.button("Go to Login Page"):
                                            st.session_state.page = "Login"
                                            st.rerun()

                                elif response.status_code == 400:
                                    error_detail = response.json().get('detail', 'Unknown error')
                                    st.error(f"❌ Registration failed: {error_detail}")
                                else:
                                    st.error(f"❌ Registration failed: {response.status_code}")
                                    if response.text:
                                        with st.expander("Error details"):
                                            st.code(response.text)

                            except requests.exceptions.ConnectionError:
                                st.error(
                                    "🔌 Cannot connect to server. Make sure the backend is running at http://127.0.0.1:8000")
                                with st.expander("How to start the server"):
                                    st.code("uvicorn main:app --reload --host 127.0.0.1 --port 8000")
                            except requests.exceptions.Timeout:
                                st.error("⏱️ Connection timeout. The server is taking too long to respond.")
                                st.info(
                                    "This might happen if the server is busy or starting up. Try again in a moment.")
                            except Exception as e:
                                st.error(f"❌ Unexpected error: {str(e)[:200]}")
                                with st.expander("Error details"):
                                    st.exception(e)

            # Add a note about mock payment
            st.info(
                "📝 This is a demonstration - no actual payment will be processed. Any card number format will work as long as it's provided.")

            # Back to login button
            if st.button("← Back to Login", use_container_width=True):
                st.session_state.page = "Login"
                st.rerun()
    # Login
    elif st.session_state.page == "Login":
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("### Welcome Back")

            # Username and password inputs (outside form for consistent styling)
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")

            # Add a subtle feature preview to match register page style
            st.markdown("**Your Benefits:**")
            with st.container():
                st.markdown("✓ Secure login")
                st.markdown("✓ Access to your membership features")
                st.markdown("✓ Calculation history saved")

            st.divider()

            # Login button
            if st.button("Log In", use_container_width=True, type="primary"):
                if not username or not password:
                    st.error("Please enter both username and password")
                else:
                    import requests
                    from requests.exceptions import ConnectionError, Timeout, RequestException

                    try:
                        r = requests.post(
                            "http://127.0.0.1:8000/login",
                            json={"username": username, "password": password},
                            timeout=5
                        )

                        if r.status_code == 200:
                            data = r.json()
                            if "token" in data and "membership" in data:
                                st.session_state.update({
                                    "logged_in": True,
                                    "username": data["token"],
                                    "membership": data["membership"],
                                    "page": "Calculator"
                                })
                                st.rerun()
                            else:
                                st.error("Invalid response from server: missing token or membership")
                        elif r.status_code == 401:
                            st.error("❌ Invalid username or password")
                        elif r.status_code == 404:
                            st.error("❌ Login endpoint not found. Check if backend is running on port 8000")
                        else:
                            st.error(f"❌ Server error (HTTP {r.status_code}): {r.text[:100]}")

                    except ConnectionError:
                        st.error(
                            "🔌 Cannot connect to server. Make sure the backend is running at http://127.0.0.1:8000")
                        with st.expander("Troubleshooting tips"):
                            st.markdown("""
                            1. Check if your backend server is running
                            2. Verify the server is on port 8000
                            3. Try running: `python your_backend_file.py`
                            4. Check for any firewall blocking local connections
                            """)

                    except Timeout:
                        st.error("⏱️ Connection timeout. Server is taking too long to respond")

                    except RequestException as e:
                        st.error(f"📡 Network error: {str(e)[:100]}")

                    except Exception as e:
                        st.error(f"❌ Unexpected error: {type(e).__name__}")
                        if st.checkbox("Show error details"):
                            st.exception(e)

            # Create account button
            if st.button("Create Account →", use_container_width=True):
                st.session_state.page = "Register"
                st.rerun()

    # Calculator (Homepage)
    elif st.session_state.page == "Calculator" and st.session_state.logged_in:
        membership = st.session_state.membership

        # Welcome message at the top
        st.markdown(f"### Welcome, {st.session_state.username}!")
        st.markdown(f"**Membership Plan:** {st.session_state.membership}")

        # Add a separator
        st.divider()

        if membership == "Quo":
            tab1, tab2, tab3, tab4 = st.tabs(["Calculator", "Graphs", "History", "Currency Converter"])
        else:
            tab1, tab2, tab3 = st.tabs(["Calculator", "Graphs", "History"])

        # Calculator tab
        with tab1:
            col1, col2 = st.columns(2)
            with col1:
                a = st.number_input("First number", value=0.0)
                b = st.number_input("Second number", value=0.0)

            with col2:
                ops = ["Addition"]
                if membership in ["Pro", "Quo"]:
                    ops.append("Subtraction")
                if membership == "Quo":
                    ops.extend(["Multiplication", "Division"])

                op = st.selectbox("Operation", ops)

                if st.button("Calculate", use_container_width=True):
                    op_map = {"Addition": "add", "Subtraction": "subtract", "Multiplication": "multiply",
                              "Division": "divide"}
                    try:
                        r = requests.post("http://127.0.0.1:8000/api/calculate",
                                          json={"operation": op_map[op], "a": a, "b": b},
                                          headers={"token": st.session_state.username})
                        if r.ok:
                            result = r.json()['result']
                            st.success(f"Result: {result}")
                            st.session_state.history.append({
                                'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                'op': op, 'a': a, 'b': b, 'result': result
                            })
                        else:
                            st.error("Calculation failed")
                    except:
                        st.error("Cannot connect to server")

        # Graphs tab
        with tab2:
            if membership == "Quo":
                expr = st.text_input("f(x) =", value="x**2")

                col1, col2 = st.columns(2)
                with col1:
                    x_min = st.number_input("x min", value=-10.0)
                with col2:
                    x_max = st.number_input("x max", value=10.0)

                if st.button("Plot", use_container_width=True):
                    try:
                        x = np.linspace(x_min, x_max, 200)
                        allowed = {"x": x, "np": np, "sin": np.sin, "cos": np.cos,
                                   "exp": np.exp, "log": np.log, "sqrt": np.sqrt, "pi": np.pi}
                        y = eval(expr, {"__builtins__": {}}, allowed)

                        fig = go.Figure()
                        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='blue')))
                        fig.update_layout(title=f"y = {expr}", xaxis_title="x", yaxis_title="y")
                        st.plotly_chart(fig, use_container_width=True)

                        # Quick stats
                        st.metric("Min", f"{np.min(y):.2f}")
                        st.metric("Max", f"{np.max(y):.2f}")
                        st.metric("Mean", f"{np.mean(y):.2f}")

                    except Exception as e:
                        st.error("Invalid function")
            else:
                st.info("Upgrade to Quo plan for graphing features")

        # History tab
        with tab3:
            if st.session_state.history:
                df = pd.DataFrame(st.session_state.history)
                st.dataframe(df.sort_values('time', ascending=False), use_container_width=True, hide_index=True)
                if st.button("Clear History"):
                    st.session_state.history = []
                    st.rerun()
            else:
                st.info("No calculations yet")

        # Currency Converter tab (only for Quo users)
        with tab4 if membership == "Quo" else tab1:
            if membership == "Quo":
                st.markdown("### 💱 Currency Converter")
                st.markdown("Real-time exchange rates from Frankfurter API")

                # Import currency functions
                from currency_scraper import (
                    get_exchange_rates, convert_currency, get_popular_currencies,
                    get_currency_flags, get_currency_names, get_historical_rates
                )

                # Create tabs within the Currency Converter
                conv_tab1, conv_tab2, conv_tab3 = st.tabs(["💰 Converter", "📊 Rate Charts", "ℹ️ About"])

                with conv_tab1:
                    # Get exchange rates (cached)
                    with st.spinner("Fetching latest exchange rates..."):
                        rates, last_updated = get_exchange_rates()

                    if rates:
                        # Show last updated time
                        st.info(f"🕐 Rates updated: {last_updated} (from European Central Bank via Frankfurter API)")

                        # Get flags and names
                        flags = get_currency_flags()
                        names = get_currency_names()
                        currencies = get_popular_currencies()

                        # Create currency options with flags
                        currency_options = {f"{flags.get(c, '')} {c} - {names.get(c, '')}": c for c in currencies}

                        # Main converter
                        col1, col2, col3 = st.columns([2, 1, 2])

                        with col1:
                            amount = st.number_input("Amount", min_value=0.01, value=100.0, step=10.0,
                                                     key="currency_amount")
                            from_display = st.selectbox("From", options=list(currency_options.keys()),
                                                        index=0, key="from_currency_display")
                            from_currency = currency_options[from_display]

                        with col2:
                            st.markdown("<h1 style='text-align: center; margin-top: 60px;'>→</h1>",
                                        unsafe_allow_html=True)

                        with col3:
                            to_display = st.selectbox("To", options=list(currency_options.keys()),
                                                      index=1, key="to_currency_display")
                            to_currency = currency_options[to_display]

                            # Calculate conversion
                            converted_amount = convert_currency(amount, from_currency, to_currency, rates)

                            # Show exchange rate
                            rate = rates.get(to_currency, 1.0) / rates.get(from_currency, 1.0)

                            # Display result in a nice box
                            st.markdown(f"""
                            <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                                        padding: 25px; border-radius: 15px; text-align: center;'>
                                <p style='color: white; margin: 0; font-size: 14px;'>Converted Amount</p>
                                <h1 style='margin: 5px 0; color: white; font-size: 36px;'>
                                    {converted_amount:,.2f} {to_currency}
                                </h1>
                                <p style='color: rgba(255,255,255,0.8); margin: 0; font-size: 14px;'>
                                    1 {from_currency} = {rate:.4f} {to_currency}
                                </p>
                            </div>
                            """, unsafe_allow_html=True)

                        # Quick conversion table
                        st.divider()
                        st.markdown("### 📊 Quick Reference")

                        # Create a grid of common conversions
                        common_amounts = [1, 10, 100, 1000]
                        quick_cols = st.columns(len(common_amounts))

                        for i, amt in enumerate(common_amounts):
                            with quick_cols[i]:
                                quick_convert = convert_currency(amt, from_currency, to_currency, rates)
                                st.metric(
                                    label=f"{amt} {from_currency}",
                                    value=f"{quick_convert:,.2f} {to_currency}",
                                    delta=f"Rate: {rate:.4f}"
                                )

                        # Popular pairs
                        st.divider()
                        st.markdown("### 🌟 Popular Currency Pairs")

                        popular_pairs = [
                            ('USD', 'EUR'), ('USD', 'GBP'), ('USD', 'JPY'),
                            ('EUR', 'GBP'), ('EUR', 'JPY'), ('GBP', 'JPY')
                        ]

                        pair_cols = st.columns(3)
                        for i, (base, quote) in enumerate(popular_pairs):
                            with pair_cols[i % 3]:
                                pair_rate = rates.get(quote, 1.0) / rates.get(base, 1.0)
                                st.metric(
                                    label=f"{base}/{quote}",
                                    value=f"{pair_rate:.4f}",
                                    delta=f"1 {base} = {pair_rate:.4f} {quote}"
                                )

                with conv_tab2:
                    st.markdown("### 📈 Exchange Rate Charts")

                    # Currency selection for chart
                    col1, col2 = st.columns(2)
                    with col1:
                        base_currency_display = st.selectbox("Base Currency", options=list(currency_options.keys()),
                                                             index=0, key="chart_base")
                        base_currency = currency_options[base_currency_display]
                    with col2:
                        target_currency_display = st.selectbox("Target Currency", options=list(currency_options.keys()),
                                                               index=1, key="chart_target")
                        target_currency = currency_options[target_currency_display]

                    # Time period selection
                    period = st.selectbox("Time Period", ["7 Days", "30 Days", "90 Days"], index=0)
                    days = int(period.split()[0])

                    # Fetch historical data
                    with st.spinner("Fetching historical data..."):
                        historical_rates = get_historical_rates(base_currency, days)

                    if historical_rates and target_currency in list(historical_rates.values())[0]:
                        # Prepare data for plotting
                        dates = []
                        rates_history = []

                        for date, rate_data in historical_rates.items():
                            if target_currency in rate_data:
                                dates.append(date)
                                rates_history.append(rate_data[target_currency])

                        if dates and rates_history:
                            # Create a simple line chart
                            chart_data = pd.DataFrame({
                                'Date': pd.to_datetime(dates),
                                f'{base_currency}/{target_currency}': rates_history
                            })

                            st.line_chart(chart_data.set_index('Date'))

                            # Show statistics
                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.metric("Highest", f"{max(rates_history):.4f}")
                            with col2:
                                st.metric("Lowest", f"{min(rates_history):.4f}")
                            with col3:
                                st.metric("Average", f"{sum(rates_history) / len(rates_history):.4f}")
                        else:
                            st.warning("No historical data available for this currency pair")
                    else:
                        st.info("Historical data is being fetched. Please try again in a moment.")

                with conv_tab3:
                    st.markdown("### ℹ️ About this Currency Converter")

                    st.markdown("""
                    **Data Source:** European Central Bank via Frankfurter API

                    **Features:**
                    - ✅ Real-time exchange rates updated daily
                    - ✅ Support for 30+ global currencies
                    - ✅ Historical rate charts (7-90 days)
                    - ✅ Quick conversion tables
                    - ✅ Popular currency pairs

                    **Currencies Available:**
                    - Major: USD, EUR, GBP, JPY, CHF, CAD, AUD
                    - Emerging: CNY, INR, MXN, BRL, KRW, SGD, ZAR
                    - And many more...

                    **Note:** Exchange rates are provided for informational purposes only.
                    For the most accurate and real-time rates, please check with your financial institution.

                    **API Information:** This tool uses the free Frankfurter API (frankfurter.app)
                    """)

                    # Rate update button
                    if st.button("🔄 Manually Refresh Rates", use_container_width=True):
                        st.cache_data.clear()
                        st.rerun()

            else:
                st.info("💱 Upgrade to Quo plan to access the Currency Converter with real-time exchange rates!")

        # Add some space before the logout button
        st.markdown("<br><br>", unsafe_allow_html=True)

        # Logout button at the bottom left
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 5])
        with col1:
            if st.button("🚪 Logout", use_container_width=True, type="secondary"):
                # Clear session state and redirect to login
                st.session_state.update({
                    "logged_in": False,
                    "username": "",
                    "membership": "",
                    "history": [],
                    "page": "Login"
                })
                st.rerun()