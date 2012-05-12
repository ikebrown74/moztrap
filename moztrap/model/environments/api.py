from tastypie import fields
from tastypie.resources import ModelResource, ALL

from .models import Environment, Element



class ElementResource(ModelResource):

    class Meta:
        queryset = Element.objects.all()
        fields = ["id", "name", "resource_uri"]



class EnvironmentResource(ModelResource):
    elements = fields.ToManyField(ElementResource, "elements", full=True)

    class Meta:
        queryset = Environment.objects.all()
        list_allowed_methods = ['get']
        fields = ["id", "resource_uri"]
        filtering = {"elements": ALL}