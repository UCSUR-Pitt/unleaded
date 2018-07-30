from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import PipeRecord

def handle_submission(request):
    """Accept a GET request, parse the keys, and file the contents away in the database."""
    # To increase robustness, use the following to get all model keys
        # myproject.myapp.models.MyModel._meta.get_all_field_names()
    # then strip out created_at and iterate over the results.
    home = request.GET['home']
    steps_dict = {}
    for k in range(1,7):
        step_k = 'step{}'.format(k)
        if step_k in request.GET:
            steps_dict[step_k] = request.GET[step_k]

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
    return HttpResponse("Hello, Zaphod. You're at the pipe_data index.")
