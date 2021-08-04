from django.shortcuts import render
from django.contrib import HttpResponse,JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from ecom import settings

import braintree

# Create your views here.

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id=settings.merchant_id,
        public_key=settings.public_key,
        private_key=settings.private_key
    )
)

