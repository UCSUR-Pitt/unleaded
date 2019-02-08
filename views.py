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

    field_names_extended = list(field_names)
    extra_fields = ['step7', 'step8']
    for f in extra_fields:
        if f not in field_names:
            field_names_extended.append(f)

    writer.writerow(field_names_extended)
    for obj in queryset:
        fields_to_write = [getattr(obj, field) for field in field_names]
        for f in extra_fields:
            if f not in field_names:
                full_submission_json = getattr(obj, 'full_submission')
                if full_submission_json in [None, '']:
                    value = ''
                else:
                    full_submission = json.loads(full_submission_json)
                    value = full_submission[f] if f in full_submission else ''
                fields_to_write.append(value)

        row = writer.writerow(fields_to_write)

    return response

def index(request):
    return HttpResponse("Welcome to the index!")
