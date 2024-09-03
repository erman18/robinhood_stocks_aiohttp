import asyncio
import os

import pyotp
from Robinhood import Robinhood


async def main():
    client = Robinhood()
    try:
        await client.initialize()

        username = os.environ.get("ROBINHOOD_USERNAME")
        password = os.environ.get("ROBINHOOD_PASSWORD")
        totp_key = os.environ.get("ROBINHOOD_TOTP_KEY")

        if not all([username, password, totp_key]):
            raise ValueError("Robinhood credentials not set in environment variables")

        totp = pyotp.TOTP(totp_key).now()
        print(f"totp code: {totp}")

        login_response = await client.login(
            username=username, password=password, mfa_code=totp
        )
        print("Login response:", login_response)

        # Get all positions
        positions = await client.get_option_positions_from_account()
        print("Account positions:", positions)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
