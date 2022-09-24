from django.http import HttpResponse
from django.shortcuts import render
from .models import Asgard
from django.template import loader


def webasgard(request,):
    geo=Asgard.objects.filter(title='Geography',id=1).values()
    his=Asgard.objects.filter(title='History',id=2).values()
    cul=Asgard.objects.filter(title='Culture',id=3).values()
    lan=Asgard.objects.filter(title='Language',id=4).values()
    template=loader.get_template('webasgard.html')
    context={
        'GeoM':geo,
        'HisM':his,
        'CulM':cul,
        'LanM':lan,
    }
    return HttpResponse(template.render(context,request))
 #   return render(request, 'webasgard.html')
