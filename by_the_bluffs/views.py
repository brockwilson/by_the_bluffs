from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from crags.models import Area, Crag, Climb

def home(request):
    areas = Area.objects.all()
    crags = Crag.objects.all()
    climbs = Climb.objects.all()
    return render_to_response('home.html', {"areas": areas,
                                            "crags": crags,
                                            "climbs": climbs}, context_instance=RequestContext(request))
