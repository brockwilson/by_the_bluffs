from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    creation_date_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True

class Area(CommonInfo):
    pass

class Crag(CommonInfo):
    area = models.ForeignKey(Area)

class Climb(CommonInfo):
    grade = models.CharField(max_length=20)
    crag = models.ForeignKey(Crag)
    
class Pitch(models.Model):
    pitch_number = models.IntegerField()
    description = models.TextField()
    grade = models.CharField(max_length=20)
    climb = models.ForeignKey(Climb)






    
