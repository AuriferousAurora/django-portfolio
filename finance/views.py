import json
import os

from django.shortcuts import render
from django.views import View

from plaid import Client
from plaid.errors import APIError, ItemError

class IndexView(View):
  template = 'test_template.html'
  context = {}

  PLAID_SANBOX_URL = 'https://sandbox.plaid.com'

  PLAID_CLIENT_ID = '5cfadf5f1aa68500128fcb9e'
  PLAID_SECRET = '3c82383b382173750b37f16e52c07d'
  PLAID_PUBLIC_KEY = '477f7b16c8ad370e5e5e5e2b8ebbca'
  PLAID_ENV = 'sandbox'
  PLAID_PRODUCTS = 'transactions'
  PLAID_COUNTRY_CODES = 'US,CA,GB,FR,ES'

  client = Client(client_id=PLAID_CLIENT_ID, secret=PLAID_SECRET,
    public_key=PLAID_PUBLIC_KEY, environment=PLAID_ENV)

  access_token = None

  def get(self, request):
    self.context.update({'test': {'1': '1', '2': '2'}})
    return render(request, self.template, context=self.context)

  def post(self, request):
    public_token = request.POST['public_token']

    response = self.client.Item.public_token.exchange(public_token)

    access_token = response['access_token']
    item_id = response['item_id']
    request_id = response['request_id']


    auth_response = self.client.Auth.get(access_token)

    accounts = auth_response['accounts']

    # for account in accounts:
    #   a = {account['account_id']: {'balance_available': account['balances']['available'],
    #                                'balance_current': account['balances']['current']}}
    #   account_dict.update(a)
    self.context.update({'accounts': {}})
    for account in accounts:   
      self.context['accounts'].update({account['account_id']: account['balances']['available']})
      print(self.context)

    print(self.context)
    return render(request, self.template, context=self.context)