from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import PipeRecord

def handle_submission(request):
    """Accept a GET or POST request, parse the keys, and file the contents away in the database."""
    # To increase robustness, use the following to get all model keys
        # myproject.myapp.models.MyModel._meta.get_all_field_names()
    # then strip out created_at and iterate over the results.
    if request.method == 'GET':
        qd = request.GET
    elif request.method == 'POST':
        qd = request.POST
    else:
        response_data = {"success": False,
                "message": "Unable to parse a {} request.".format(request.method)
        }
        return JsonResponse(response_data)

    home = qd['home']

    steps_dict = {}
    for k in range(1,7):
        step_k = 'step{}'.format(k)
        if step_k in qd:
            steps_dict[step_k] = qd[step_k]

    pr = PipeRecord(home=home, **steps_dict)
    pr.save()

    steps_dict['home'] = home
    response_data = {
        "success": True,
        "payload": {
            "parameters": steps_dict 
        }
    }
    
    return JsonResponse(response_data)

def index(request):
    return HttpResponse("Welcome to the index!")
