from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from crags.models import Area, Crag, Climb

def climb_view(request, climb_id):
    try:
        climb_id_int = int(climb_id)
    except ValueError:
        raise Http404()
    
    try:
        climb = Climb.objects.get(id=climb_id_int)
    except Climb.DoesNotExist:
        raise Http404()
    return render_to_response('climb_view.html', {'climb': climb}, context_instance=RequestContext(request))

def crag_view(request, crag_id):
    try:
        crag_id_int = int(crag_id)
    except ValueError:
        raise Http404()
    
    try:
        crag = Crag.objects.get(id=crag_id_int)
    except Crag.DoesNotExist:
        raise Http404()
    climbs = Climb.objects.filter(crag_id=crag_id_int)
    return render_to_response('crag_view.html', {'crag': crag,
                                                 'climbs': climbs}, context_instance=RequestContext(request))

def area_view(request, area_id):
    try:
        area_id_int = int(area_id)
    except ValueError:
        raise Http404()
    
    try:
        area = Area.objects.get(id=area_id_int)
    except Area.DoesNotExist:
        raise Http404()
    crags = Crag.objects.filter(area_id=area_id_int)
    return render_to_response('area_view.html', {'area': area,
                                                 'crags': crags}, context_instance=RequestContext(request))
