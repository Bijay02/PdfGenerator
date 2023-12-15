from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
import json
from .utils import render_to_pdf

def home(request):
    return render(request, "home/index.html")

@csrf_exempt
def user(request):
    if request.method == "GET":
        result = []

        users = User.objects.all()
        for user in users:
            data = {
                "name": user.name,
                "phone": user.phone,
                "email": user.email,
                "address": user.address
            }
            result.append(data)
        return HttpResponse(json.dumps(result))
    

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        name = data['name']
        phone = data['phone']
        email = data['email']
        address = data['address']
        

        user = User(name = name, phone = phone, email = email, address= address)
        user.save()
        return HttpResponse({"User successfully added"})


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = User.objects.all().values()

        pdf = render_to_pdf("home/report.html", {'users': data})
        return HttpResponse(pdf, content_type='application/pdf')