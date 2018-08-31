from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from treebeard.forms import MoveNodeForm
from app import models


class MyNodeForm(MoveNodeForm):
    class Meta:
        model = models.SampleModel
        fields = '__all__'


class Register(CreateView):
    form_class = MyNodeForm
    template_name = 'index.html'

