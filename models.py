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
    qd = models.CharField(max_length=9999,default='')

    class Meta:
        verbose_name = "submission"

    def __str__(self):
        return '{} ({}, {}, {}, {}, {}, {}, {})'.format(self.created_at, self.home, self.step1, self.step2, self.step3, self.step4, self.step5, self.step6)
