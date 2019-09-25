import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from finance.models import Account

from plaid import Client
from plaid.errors import APIError, ItemError

class EstablishLinkView(View):
  template = 'establish-link-template.html'

  def get(self, request):
    return render(request, self.template)


class ItemDisplayView(View):
  template = 'item-display-template.html'
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


  def get(self, request):
    access_token = request.session['access_token']
    self.context.update({'hello': access_token})
    return render(request, self.template, context=self.context)

  def post(self, request):
    try: 
      public_token = request.POST['public_token']
    except KeyError:
      return HttpResponse('No public token found.')

    item_response = self.client.Item.public_token.exchange(public_token)

    request.session['access_token'] = item_response['access_token']
    item_id = item_response['item_id']
    public_token_request_id = item_response['request_id']

    auth_response = self.client.Auth.get(request.session['access_token'])

    accounts = auth_response['accounts']
    numbers = auth_response['numbers']
    access_token_request_id = auth_response['request_id']

    for account in accounts:
      account_model_type = account['type'].upper()
      account_model = Account(account_id=account['account_id'],
                              account_balance=account['balances']['available'],
                              account_type=Account.CHECKING)
      account_model.save()

    response = {'success': '1'}

    return HttpResponse(response)