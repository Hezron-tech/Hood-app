from django.contrib import admin
from.models import Neighborhood, Profile, HoodMember,Business,Post

# Register your models here.


admin.site.register(Profile)
admin.site.register(Neighborhood)
admin.site.register(HoodMember)
admin.site.register(Business)
admin.site.register(Post)
