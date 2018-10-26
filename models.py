from django.db import models

class PipeRecord(models.Model):
    """This model represents the answers given by a user about the pipes in their home
    as they click their way through the Leaducated app."""
    created_at = models.DateTimeField(auto_now_add=True)
    home = models.CharField(max_length=100)
    step1 = models.CharField(max_length=100)
    step2 = models.CharField(max_length=100)
    step3 = models.CharField(max_length=100)
    step4 = models.CharField(max_length=100)
    step5 = models.CharField(max_length=100)
    step6 = models.CharField(max_length=100)
    email = models.CharField(max_length=300,default='')
    share = models.CharField(max_length=100,default='') # values include "teamonly"
    wall_floor = models.CharField(max_length=10,default='') # Does your pipe come through the wall or floor?
    own_rent = models.CharField(max_length=10,default='') # Are you a homeowner or renter? values include "own"
    units = models.CharField(max_length=20,default='') # Are you a homeowner or renter? values include "-1"
    income = models.CharField(max_length=20,default='') # values include "0"
    children = models.CharField(max_length=20,default='') # values include "0"
    address1 = models.CharField(max_length=100,default='')
    address2 = models.CharField(max_length=100,default='')
    city = models.CharField(max_length=100,default='')
    state = models.CharField(max_length=3,default='')
    zip_code = models.CharField(max_length=10,default='') # Allowing 10 characters to allow for a ZIP+4 code.
    full_submission = models.CharField(max_length=9999,default='') # The complete raw text
    # passed from the front end.

    class Meta:
        verbose_name = "submission"

    def __str__(self):
        return '{} ({}, {}, {}, {}, {}, {}, {})'.format(self.created_at, self.home, self.step1, self.step2, self.step3, self.step4, self.step5, self.step6)
