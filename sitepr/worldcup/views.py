from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import logout

def index(request):
    #teams_list = Team.objects.order_by('-group_number').reverse()
    #output = ', '.join([t.name for t in teams_list])
    #return HttpResponse(output)
    template = loader.get_template('worldcupapp/index.html')
    #context = {
        # information about user
    #}
    return HttpResponse(template.render())

@csrf_exempt
def login_admin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    context = {
        'obtained_name': username,
    }
    if user is not None:
        if user.is_superuser:
            login(request, user)
            #OK!
            template = loader.get_template('worldcupapp/index.html')
        else:
            template = loader.get_template('worldcupapp/not_admin.html')
    else:
        #not OK
        template = loader.get_template('worldcupapp/fail.html')
    return HttpResponse(template.render(context, request))

@csrf_exempt
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    context = {
        'obtained_name': username,
    }
    if user is not None:
        login(request, user)
        #OK!
        template = loader.get_template('worldcupapp/sucess.html')
    else:
        #not OK
        template = loader.get_template('worldcupapp/fail.html')
    return HttpResponse(template.render(context, request))

@csrf_exempt
def create_admin(request):
    uname = request.POST['username']
    pwd = request.POST['pwd1']
    try:
        user = User.objects.create_superuser(username=uname, email=None, password=pwd)
        return HttpResponse('Account created successfully!')
    except ValueError:
        return HttpResponse('Could not create the account')

@csrf_exempt
def create_user(request):
    uname = request.POST['username']
    pwd = request.POST['pwd1']
    try:
        user = User.objects.create_user(username=uname, email=None, password=pwd)
        return HttpResponse('Account created successfully!')
    except ValueError:
        return HttpResponse('Could not create the account')

@csrf_exempt
def logoutview(request):
    logout(request)
    # direccionar para página de sucesso
