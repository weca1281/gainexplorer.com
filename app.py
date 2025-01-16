import json

import streamlit as st  # type: ignore


with open("coins.json", "r") as f:
    json_data = json.load(f)

# returns an amount of the coin
def select_amount():
    amount = st.number_input(
        "Insert a number",
        value=10000,
        placeholder="Type a number...",
        min_value=0,
        step=1,
    )
    st.write("The current number is ", amount)
    return amount


# returns a coin from the json list of coins. This list comes from https://github.com/crypti/cryptocurrencies/blob/master/cryptocurrencies.json
def select_crypto():
    selected_crypto = st.selectbox(
        "Issuing Country:", json_data.values(), placeholder="Select coin", index=1458)
    return selected_crypto


# returns a date, with a default of when that guy bought that pizza for 10,000 bitcoin
def select_dates():
    date = st.date_input("Chosen Date", value="2009-05-22")
    return date


# TODO This is the magic sauce, that we need to calculate
# We can take the values passed in and use APIs or whatever to calculate the value at that point in time
def calculate_value(chosen_amount, chosen_crypto, chosen_date):
    result = "One million doll hairs"
    return result


def main():
    st.header("GainExplorer.com")
    st.write("What if financial calculator for Stocks and Cryptos")

    # Create a section for selecting passport and a button to add more
    with st.container(border=True):

        col1, col2, col3 = st.columns([1, 1, 1], border=True)

        # Select Amount
        with col1:
            st.write("Amount")
            chosen_amount = select_amount()

        # Select Crypto coins
        with col2:
            st.write("Crypto")
            chosen_crypto = select_crypto()

        # Select Dates
        with col3:
            st.write("Date")
            chosen_date = select_dates()

    # Section to display the result
    with st.expander("Results", expanded=True):
        value = calculate_value(chosen_amount, chosen_crypto, chosen_date)

        # We use a multi line formatted string
        st.write(
            f"""

**{chosen_amount}** **{chosen_crypto}** in **{chosen_date}** would have been worth:\n
## {value}

"""
        )


if __name__ == "__main__":
    main()
