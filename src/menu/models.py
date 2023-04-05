from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=100, blank=True)

    def str(self):
        return self.name
