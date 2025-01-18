from typing import Dict, List
import requests
from pydantic import parse_obj_as
from crypto_cloud_py.crypto_cloud_invoice_created import CryptoCloudInvoiceCreated
from crypto_cloud_py.crypto_cloud_invoice_info import CryptoCloudInvoiceInfo
from crypto_cloud_py.crypto_cloud_stats import CryptoCloudStats


class CryptoCloudApi:
    # When initializing the API provide your API key
    # You can keep the rest of the parameters with default values
    def __init__(self, api_key: str, timeout_s: int = 15, base_url: str = 'https://api.cryptocloud.plus/v2'):
        self.api_key = api_key
        self.timeout_s = timeout_s
        self.base_url = base_url
        self.locales = ['en', 'ru', 'de', 'fr', 'it', 'es', 'ch']
        self.currencies = [
            'USD', 'UZS', 'KGS', 'KZT', 'AMD', 'AZN', 'BYN',
            'AUD', 'TRY', 'AED', 'CAD', 'CNY', 'HKD', 'IDR',
            'INR', 'JPY', 'PHP', 'SGD', 'THB', 'VND', 'MYR',
            'RUB', 'UAH', 'EUR', 'GBP'
        ]

    def get_headers(self) -> Dict[str, str]:
        return {'Authorization': f'Token {self.api_key}'}

    # See the original documentation at https://docs.cryptocloud.plus/en/api-reference-v2/create-invoice
    def invoice_create(self, shop_id: str, amount: int, currency: str = 'USD', add_fields: Dict = {}, order_id: str = '', email: str = '', locale: str = 'en') -> CryptoCloudInvoiceCreated:
        # Build default headers with authorization
        headers = self.get_headers()

        # Build required body
        body = {
            'shop_id': shop_id,
            'amount': amount,
        }

        # Add optional parameters
        if currency is not None:
            currency = currency.upper().strip()
            if len(currency) > 0:
                if currency in self.currencies:
                    body['currency'] = currency
                else:
                    raise RuntimeError(f"Unsupported currency {currency}")
        if add_fields is not None and len(add_fields) > 0:
            body['add_fields'] = add_fields
        if order_id is not None:
            order_id = order_id.strip()
            if len(order_id) > 0:
                body['order_id'] = order_id
        if email is not None:
            email = email.lower().strip()
            if len(email) > 0:
                body['email'] = email
        if locale is not None:
            locale = locale.lower().strip()
            if len(locale) > 0:
                if locale not in self.locales:
                    raise RuntimeError(f"Unsupported locale {locale}")

        # Build URL
        url = f"{self.base_url}/invoice/create?locale={locale}"

        # Make request
        response = requests.post(url, headers=headers, data=body, timeout=self.timeout_s)
        response.raise_for_status()
        response_json = response.json()
        return CryptoCloudInvoiceCreated.parse_obj(response_json['result'])

    # See the original documentation at https://docs.cryptocloud.plus/en/api-reference-v2/cancel-invoice
    def invoice_cancel(self, uuid: str) -> List[str]:
        # Build default headers with authorization
        headers = self.get_headers()

        # Build body
        body = {'uuid': uuid}

        # Build URL
        url = f"{self.base_url}/invoice/merchant/canceled"

        # Make request
        response = requests.post(url, headers=headers, json=body, timeout=self.timeout_s)
        response.raise_for_status()
        response_json = response.json()
        return response_json['result']

    # See the original documentation at https://docs.cryptocloud.plus/en/api-reference-v2/invoice-information
    def invoices_info(self, invoices_ids: List[str]) -> List[CryptoCloudInvoiceInfo]:
        # Build default headers with authorization
        headers = self.get_headers()

        # Build body
        body = {'uuids': invoices_ids}

        # Build URL
        url = f"{self.base_url}/invoice/merchant/info"

        # Make request
        response = requests.post(url, headers=headers, json=body, timeout=self.timeout_s)
        response.raise_for_status()
        response_json = response.json()
        return parse_obj_as(List[CryptoCloudInvoiceInfo], response_json['result'])

    # See the original documentation at https://docs.cryptocloud.plus/en/api-reference-v2/statistics
    def invoice_statistics(self, start: str, end: str) -> CryptoCloudStats:
        # Build default headers with authorization
        headers = self.get_headers()

        # Build body
        body = {'start': start, 'end': end}

        # Build URL
        url = f"{self.base_url}/invoice/merchant/statistics"

        # Make request
        response = requests.post(url, headers=headers, data=body, timeout=self.timeout_s)
        response.raise_for_status()
        response_json = response.json()
        return CryptoCloudStats.parse_obj(response_json['result'])
