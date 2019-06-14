from django.db import models
from django.utils.safestring import mark_safe


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
    email = models.CharField(
        max_length=300,
        default=''
    )
    share = models.CharField(  # values include "teamonly"
        max_length=100,
        default=''
    )
    wall_floor = models.CharField(
        # Does your pipe come through the wall or floor?
        max_length=10,
        default=''
    )
    own_rent = models.CharField(
        # Are you a homeowner or renter? values include "own"
        max_length=10,
        default=''
    )
    previously_tested = models.CharField(
        # Have you had your water tested for lead? values include "yes-nolead"
        max_length=30,
        default=''
    )
    units = models.CharField(
        # Are you a homeowner or renter? values include "-1"
        max_length=20,
        default=''
    )
    income = models.CharField(  # values include "0"
        max_length=30,
        default=''
    )
    children = models.CharField(  # values include "0"
        max_length=20,
        default=''
    )
    address1 = models.CharField(
        max_length=100,
        default=''
    )
    address2 = models.CharField(
        max_length=100,
        default=''
    )
    city = models.CharField(
        max_length=100,
        default=''
    )
    state = models.CharField(
        max_length=3,
        default=''
    )
    zip_code = models.CharField(
        # Allowing 10 characters to allow for a ZIP+4 code.
        max_length=10,
        default=''
    )
    image = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        blank=True,
        null=True
    )
    full_submission = models.CharField(  # The complete raw text
        max_length=9999,
        default=''
    )

    linked_image = models.OneToOneField(
        'PipePicture',
        related_name='submission',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    @property
    def picture(self):
        return mark_safe('<img src="/media/{}" />'.format(self.linked_image.image))


    # passed from the front end.

    class Meta:
        verbose_name = "submission"

    def __str__(self):
        return '{} ({}, {}, {}, {}, {}, {}, {})'.format(
            self.created_at,
            self.home,
            self.step1,
            self.step2,
            self.step3,
            self.step4,
            self.step5,
            self.step6
        )


class PipePicture(models.Model):
    image = models.FileField(
        upload_to='uploads/pipes/%Y/%m/%d/',
        blank=True,
        null=True
    )

    @property
    def img(self):
        return mark_safe('<img src="{}" />'.format(self.image))

    def __str__(self):
        return '{}'.format(self.image)
