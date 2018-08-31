from django.contrib.auth.models import User
from django.db import models
from treebeard.mp_tree import MP_Node

# Create your models here.


class SampleModel(MP_Node):
    name = models.CharField(max_length=20)
    reference_id = models.CharField(max_length=25, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
