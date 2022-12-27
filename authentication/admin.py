from django.contrib import admin
from authentication.models import User_authentication

@admin.register(User_authentication)
class userShow(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'address',
        'city',
        'pin_code'
    )


# Register your models here.
