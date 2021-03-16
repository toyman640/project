from frontend.models import *
import datetime


def cat_menu(request):
    category = Category.objects.all()
    return {'category': category}