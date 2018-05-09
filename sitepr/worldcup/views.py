from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

def index(request):
    #teams_list = Team.objects.order_by('-group_number').reverse()
    #output = ', '.join([t.name for t in teams_list])
    #return HttpResponse(output)
    template = loader.get_template('worldcupapp/login_admin.html')
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
        login(request, user)
        #OK!
        template = loader.get_template('worldcupapp/sucess.html')

        #return HttpResponse(template.render(context, request))
    else:
        #not OK
        template = loader.get_template('worldcupapp/fail.html')
        #context = {
        #    'obtained_name':  username,
        #}
    return HttpResponse(template.render(context, request))
        # render(request, 'votacao/index.html', context)
