from django import template
from PG.models import multipleimage,RentarDetail
register=template.Library()
@register.filter(name='get_img')
def get_img(id):
    obj=RentarDetail.objects.filter(sno=id)[0]
    img=multipleimage.objects.filter(room=obj)
    return img
