from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exemp
import json
from .models import PipeRecord

# @csrf_exempt
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

    other_dict = {}
    other_dict['email'] = qd['email']
    other_dict['share'] = qd['share']
    other_dict['wall_floor'] = qd['wallfloor']
    other_dict['own_rent'] = qd['ownrent']
    other_dict['units'] = qd['units']
    other_dict['income'] = qd['income']
    other_dict['children'] = qd['children']
    other_dict['address1'] = qd['address1']
    other_dict['address2'] = qd['address2']
    other_dict['city'] = qd['city']
    other_dict['state'] = qd['state']
    other_dict['zip_code'] = qd['zip']

    pr = PipeRecord(home=home, full_submission = json.dumps(qd), **steps_dict, **other_dict)
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
