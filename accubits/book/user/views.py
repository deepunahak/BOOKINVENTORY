from django.http import JsonResponse
from .form import UserLoginForm, UserRegisterForm
from .models import User
from django.core.cache import cache
import json
import jwt

# Create your views here.
def generate_user_token(data):
    token = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
    return token

def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        register_frm = UserRegisterForm(data)
        if register_frm.is_valid():
            try:
                obj = User()
                obj.name = data['name']
                obj.email = data['email']
                obj.password = data['password']
                obj.save()
                response = {"msg": "created successfully", "resp": {"id": obj.pk}, "status": 200, "error": ""}
            except Exception as err:
                response = {"error": str(err), "status": 500, "msg": "", "resp": {}}
                return JsonResponse(response)
            return JsonResponse(response)


def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        login_frm = UserLoginForm(data)
        if login_frm.is_valid():
            try:
                user = User.objects.get(email=data['email'])
                if user is not None and user.password == data['password']:
                    token = generate_user_token(data)
                    cache.set(token, user.id)
                    response = {"msg": "login successfully", "resp": {"email": user.email, "token": token}, "status": 200, "error": ""}
                    return JsonResponse(response)
            except Exception as err:
                response = {"error": str(err), "status": 500, "msg": "", "resp": {}}
                return JsonResponse(response)


def logout(request):
    # Need to be implemented. Delete stored token here
    pass
