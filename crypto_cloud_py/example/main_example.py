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