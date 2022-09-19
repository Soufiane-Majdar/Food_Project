from django.contrib import admin
from .models import MenuCategory, MenuItem, ComingSoon, RestaurantInfo, ContactInfo, AboutInfo,ClientReview
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group)


admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(ComingSoon)
admin.site.register(RestaurantInfo)
admin.site.register(ClientReview)
admin.site.register(AboutInfo)