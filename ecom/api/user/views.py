from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomeUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
import re
import random

def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(10))

@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error':'Send a post request with vaild parameters'})

    username=request.POST('email') 
    password=request.POST('password')

# validation your

    if not re.match("/([\w\.\-_]+)?\w+@[\w-_]+(\.\w+){1,}/igm",username):
        return JsonResponse({'error':'Enter a Valid email'})

    if len(password)<5:
        return JsonResponse({'error':'Password needs to be at least of 5 character'})

    UserModel =get_user_model()

    try:
        user=UserModel.objects.get(email=username)

        if user.check_password(password):
            usr_dict=UserModel.objects.filter(email=username).values()
            usr_dict.pop('password')

            if user.session_token != "0":
                user.session_token ="0"
                user.save()
                return JsonResponse({'error':'Previous Session Exits'})

            token=generate_session_token()
            user.session_token=token
            user.save()
            login(request,user)
            return JsonResponse({'token':token,'user':usr_dict})

        else:
            return JsonResponse({'error':'Invalid Password'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error':'Invalid Email'})