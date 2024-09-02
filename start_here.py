import os
from pprint import pprint

import pyotp
from Robinhood import Robinhood


class Usage(Robinhood):

    async def main(self):
        username = os.environ.get("ROBINHOOD_USERNAME")
        password = os.environ.get("ROBINHOOD_PASSWORD")
        totp_key = os.environ.get("ROBINHOOD_TOTP_KEY")

        totp = pyotp.TOTP(totp_key).now()
        print(f"totp code: {totp}")
        await self.login(username=username, password=password, mfa_code=totp)
        # await self.login()
        options_dict = await self.get_option_positions_from_account()
        pprint(options_dict)


if __name__ == "__main__":
    instance = Usage()
