# Asynchronous Robinhood Stocks API

## About The Project

This project provides an asynchronous Python wrapper for the Robinhood API, allowing efficient and concurrent API calls for stock and option trading operations. It's designed to be easily integrated into larger projects and supports modern async Python practices.

### Built With

- [Python 3.10+](https://www.python.org/)
- [AIOHttp](https://github.com/aio-libs/aiohttp)
- [PyJWT](https://pyjwt.readthedocs.io/)
- [PyOTP](https://pyotp.readthedocs.io/)

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.10+
- pip

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/erman18/robinhood_stocks_aiohttp.git
   cd robinhood_stocks_aiohttp
   ```

2. Install required packages
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Here's a basic example of how to use the Robinhood API wrapper:

```python
import asyncio
import os
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
        print(f"TOTP code: {totp}")

        login_response = await client.login(username=username, password=password, mfa_code=totp)
        print("Login response:", login_response)

        # Get all positions
        positions = await client.get_all_positions()
        print("All positions:", positions)


    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())
```

For more advanced usage, create a `RobinhoodInterface` class to encapsulate Robinhood operations:

```python
class RobinhoodInterface:
    def __init__(self):
        self.client = Robinhood()
        self.is_authenticated = False

    async def initialize(self):
        await self.client.initialize()

    async def authenticate(self):
      pass

    @staticmethod
    def require_auth(func):
        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            if not self.is_authenticated:
                await self.authenticate()
            return await func(self, *args, **kwargs)
        return wrapper

    @require_auth
    async def get_option_positions(self, symbol):
        return await self.client.get_option_positions(symbol)

```

## Features

- Asynchronous API calls for improved performance
- Easy integration with existing Python projects
- Supports various Robinhood API operations including:
  - Authentication
  - Retrieving account information
  - Getting stock and option positions
  - Placing and canceling orders
  - And more!

## Roadmap

See the [open issues](https://github.com/erman18/robinhood_stocks_aiohttp/issues) for a list of proposed features and known issues.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Erman Nghonda - [ermannghonda@gmail.com](mailto:ermannghonda@gmail.com)

Project Link: [https://github.com/erman18/robinhood_stocks_aiohttp](https://github.com/erman18/robinhood_stocks_aiohttp)

## Acknowledgements

- [Original robinhood_stocks_aiohttp by Senh Mo Chuang](https://github.com/IoT-master/robinhood_stocks_aiohttp)
- [robin_stocks Github](https://github.com/jmfernandes/robin_stocks)
- [aiohttp Github](https://github.com/aio-libs/aiohttp)
