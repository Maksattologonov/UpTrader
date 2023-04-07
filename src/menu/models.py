from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=100, blank=True)

    def str(self):
        return self.name

    def is_current(self, current_url):
        if self.url == current_url or self.url == reverse(current_url):
            return True
        return False

    def get_parent(self):
        if self.parent:
            return self.parent.name
        return "None"
