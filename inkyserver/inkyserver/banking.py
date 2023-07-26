import plaid
from plaid.api import plaid_api
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from .models import Dashboard
from os import getenv


def save_link_item_from_public_token():
    exchange_request = ItemPublicTokenExchangeRequest(
        public_token=pt_response['public_token']
    )
    exchange_response = client.item_public_token_exchange(exchange_request)
    access_token = exchange_response['access_token']


def generate_dashboard():
    configuration = plaid.Configuration(
        host=plaid.Environment.Development,
        api_key={
            'clientId': getenv("PLAID_CLIENT_ID"),
            'secret': getenv("PLAID_CLIENT_SECRET"),
        }
    )
    api_client = plaid.ApiClient(configuration)
    client = plaid_api.PlaidApi(api_client)

    Dashboard.objects.create(
        spending_this_month=10000,
        expected_spending_this_month=10000,
        percentage_over_under_this_month=25.5
    )
