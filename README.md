# CryptoCloud Python Client
This is a Python client for [CryptoCloud](https://cryptocloud.plus/en) API, this package is a work-in-progress client, not covering all the endpoints of the official API, but providing the basics to get started with CryptoCloud invoices. The official documentation for all API endpoints is available [here](https://docs.cryptocloud.plus/en). 

Feel free to drop your suggestions, comments and report bugs/issues you had using this package.

# Supported endpoints

* [Invoice Creation](https://docs.cryptocloud.plus/en/api-reference-v2/create-invoice), `POST https://api.cryptocloud.plus/v2/invoice/create`
* [Invoice Cancellation](https://docs.cryptocloud.plus/en/api-reference-v2/cancel-invoice), `POST https://api.cryptocloud.plus/v2/invoice/merchant/canceled` 
* [Invoice information](https://docs.cryptocloud.plus/en/api-reference-v2/invoice-information), `POST https://api.cryptocloud.plus/v2/invoice/merchant/info`
* [Statistics](https://docs.cryptocloud.plus/en/api-reference-v2/statistics), `POST https://api.cryptocloud.plus/v2/invoice/merchant/statistics`

# Installation
 
## Normal installation

```bash
pip install crypto-cloud-py
```

## Development installation

```bash
git clone https://github.com/jpleorx/crypto-cloud-py.git
cd crypto-cloud-py
pip install --editable .
```

# How to use

First of all make sure you got your [API key](https://docs.cryptocloud.plus/en/start/get-api-keys) from CryptoCloud

After you got your API key follow this basic example

```python
from crypto_cloud_py import CryptoCloudApi

# Initialize API
API_KEY = 'XXX'
SHOP_ID = 'YYY'
api = CryptoCloudApi(api_key=API_KEY)

# Create new invoice
new_invoice = api.invoice_create(shop_id=SHOP_ID, amount=100, currency='EUR', order_id='12345678', email='mail@example.com', locale='de')

# Check invoice status
invoice_statuses = api.invoices_info([new_invoice.uuid])

# Cancel invoice
api.invoice_cancel(new_invoice.uuid)

# Check statistics
stats = api.invoice_statistics(start='01.12.2024', end='20.01.2025')
```

# Links
In case you’d like to check my other work or contact me:
* [Personal website](https://tekleo.net/)
* [GitHub](https://github.com/jpleorx)
* [PyPI](https://pypi.org/user/JPLeoRX/)
* [DockerHub](https://hub.docker.com/u/jpleorx)
* [Articles on Medium](https://medium.com/@leo.ertuna)
* [LinkedIn (feel free to connect)](https://www.linkedin.com/in/leo-ertuna-14b539187/)