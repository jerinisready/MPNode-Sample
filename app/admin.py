from django.contrib import admin

# Register your models here.

from .models import SampleModel
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory, MoveNodeForm


class GovtAdminForm(MoveNodeForm):
    pass

@admin.register(SampleModel)
class GovernmentAdmin(TreeAdmin):
    form = movenodeform_factory(SampleModel)

    # def get_queryset(self, request):
    #     master = SampleModel.objects.filter(user=request.user).first()
    #     return SampleModel.get_tree(parent=master) if master else SampleModel.objects.none()



