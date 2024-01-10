from django.contrib import admin

from api.models import Shape, Drawing, Annotation

admin.site.register(Shape)
admin.site.register(Drawing)
admin.site.register(Annotation)