import json
import os
import requests

from django.shortcuts import render
from django.views import View

from plaid import Client
from plaid.errors import APIError, ItemError

class IndexView(View):
  template = 'test_template.html'
  context = {}

  PLAID_CLIENT_ID = '5cfadf5f1aa68500128fcb9e'
  PLAID_SECRET = '3c82383b382173750b37f16e52c07d'
  PLAID_PUBLIC_KEY = '477f7b16c8ad370e5e5e5e2b8ebbca'

  # Use 'sandbox' to test with Plaid's Sandbox environment (username: user_good,
  # password: pass_good)
  # Use `development` to test with live users and credentials and `production`
  # to go live
  PLAID_ENV = os.getenv('PLAID_ENV', 'sandbox')

  # PLAID_PRODUCTS is a comma-separated list of products to use when initializing
  # Link. Note that this list must contain 'assets' in order for the app to be
  # able to create and retrieve asset reports.
  PLAID_PRODUCTS = os.getenv('PLAID_PRODUCTS', 'transactions')

  # PLAID_COUNTRY_CODES is a comma-separated list of countries for which users
  # will be able to select institutions from.
  PLAID_COUNTRY_CODES = os.getenv('PLAID_COUNTRY_CODES', 'US,CA,GB,FR,ES')

  client = Client(client_id=PLAID_CLIENT_ID, secret=PLAID_SECRET,
    public_key=PLAID_PUBLIC_KEY, environment=PLAID_ENV)

  access_token = None

  def get(self, request):
    access_token = None
    global client

    try:
      self.client.Auth.get(access_token)
    except ItemError as error:
      # check the code attribute of the error to determine the specific error
      if error.code == 'ITEM_LOGIN_REQUIRED':
          # the users' login information has changed, generate a public_token
          # for the user and initialize Link in update mode to
          # restore access to this user's data
          # see https://plaid.com/docs/api/#updating-items-via-link
          print(error.code)
      else:
          print('I have no idea/')
    except APIError as error:
      if e.code == 'PLANNED_MAINTENANCE':
        print(e.code)
      else:
        print('I have no idea.')
    except requests.Timeout:
      pass

    response = client.Item.public_token.exchange(public_token)
    access_token = response['access_token']
    print(access_token)

    return render(request, self.template, context=self.context)