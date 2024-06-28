from django.contrib import admin
from .models import Food, PossibleShop, UserData, Publication, AuthUser

# Register your models here.
admin.site.register(Food)
admin.site.register(PossibleShop)
admin.site.register(UserData)
admin.site.register(Publication)
admin.site.register(AuthUser)