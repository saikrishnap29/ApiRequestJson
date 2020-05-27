from django.db import models
import pytz

# Create your models here.

class Members(models.Model):
    no=models.CharField(max_length=20)
    real_name=models.CharField(max_length=100)
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    tz= models.CharField(max_length=32, choices=TIMEZONES,default='UTC')
    # activities = models.ManyToManyField(Activity_Periods)

    def __str__(self):
        return self.real_name

    def get_dict(self):
        member = {}
        member['id'] = self.no
        member['real_name'] = self.real_name
        member['tz'] = self.tz
        return member


class Activity_Periods(models.Model):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    start_time=models.DateTimeField()
    end_time = models.DateTimeField()

    def get_dict(self):
        ap = {}
        ap['start_time'] = self.start_time.strftime("%b %d %Y  %#I:%M%p")
        ap['end_time'] = self.end_time.strftime("%b %d %Y  %#I:%M%p")
        return ap
