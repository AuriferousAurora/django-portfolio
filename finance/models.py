from django.db import models
from django.utils import timezone

class Account(models.Model):

  CHECKING = 'CHECKING'
  CREDIT = 'CREDIT'
  SAVINGS = 'SAVINGS'

  account_type_choices = [
    (CHECKING, 'CHECKING'),
    (CREDIT, 'CREDIT'),
    (SAVINGS, 'SAVINGS')
  ]

  account_balance = 
  account_type = models.CharField(choices=account_type_choices, max_length=2)
  created = models.DateTimeField()

  def get_balance():
    #Todo: Determine how to loop through all transactions and add amounts.
    # return balance
    pass
  
class Transaction(models.Model):
  
  DEPOSIT = 'DEPOSIT'
  WITHDRAWAL = 'WITHDRAWAL'

  transction_type_choices = [
    (DEPOSIT, 'DEPOSIT'),
    (WITHDRAWAL, 'WITHDRAWAL')
  ]

  PENDING_RECIEVED = 'PENDING_RECIEVED'
  PENDING_AUTHORIZED = 'PENDING_AUTHORIZED'
  POSTED = 'POSTED'

  status_choices = [
    (PENDING_RECIEVED, 'PENDING_RECIEVED'),
    (PENDING_AUTHORIZED, 'PENDING_AUTHORIZED'),
    (POSTED, 'POSTED')
  ]
  amount = models.IntegerField()
  entity = models.CharField()
  time = models.DateTimeField(default=timezone.now())
  transaction_type = models.CharField(choices=transction_type_choices, max_length=2)
  status = models.CharField(choices=status_choices, max_length=2)
