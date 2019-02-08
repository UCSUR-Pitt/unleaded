from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exemp
import json, csv
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

    home = qd.get('home', '')

    steps_dict = {}
    for k in range(1,7):
        step_k = 'step{}'.format(k)
        if step_k in qd:
            steps_dict[step_k] = qd.get(step_k, '')

    other_dict = {}
    other_dict['email'] = qd.get('email', '')
    other_dict['share'] = qd.get('share', '')
    other_dict['wall_floor'] = qd.get('wallfloor', '')
    other_dict['own_rent'] = qd.get('ownrent', '')
    other_dict['previously_tested'] = qd.get('testedbefore', '')
    other_dict['units'] = qd.get('units', '')
    other_dict['income'] = qd.get('income', '')
    other_dict['children'] = qd.get('children', '')
    other_dict['address1'] = qd.get('address1', '')
    other_dict['address2'] = qd.get('address2', '')
    other_dict['city'] = qd.get('city', '')
    other_dict['state'] = qd.get('state', '')
    other_dict['zip_code'] = qd.get('zip', '')

    pr = PipeRecord(home=home, full_submission = json.dumps(qd), **steps_dict, **other_dict)
    pr.save()

    parameters_dict = { **steps_dict, 'home': home, **other_dict } # These are the
    # parameters that have been explicitly recognized and individually added to the
    # database.
    response_data = {
        "success": True,
        "payload": {
            "parameters": parameters_dict
        }
    }

    return JsonResponse(response_data)

def extract_as_csv(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % ('/admin/login/', request.path))

    meta = PipeRecord._meta
    field_names = [field.name for field in meta.fields]
    queryset = PipeRecord.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response

def index(request):
    return HttpResponse("Welcome to the index!")
