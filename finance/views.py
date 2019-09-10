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
  PLAID_ENV = 'sandbox'
  PLAID_PRODUCTS = 'transactions'
  PLAID_COUNTRY_CODES = 'US,CA,GB,FR,ES'

  client = Client(client_id=PLAID_CLIENT_ID, secret=PLAID_SECRET,
    public_key=PLAID_PUBLIC_KEY, environment=PLAID_ENV)

  access_token = None
  public_token = PLAID_PUBLIC_KEY

  def get(self, request):
    return render(request, self.template, context=self.context)

  def post(self, request):
    print(request)
    self.context.update({'request': request})
    
    return render(request, self.template, self.context)