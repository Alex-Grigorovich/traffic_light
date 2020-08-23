from django.contrib import admin

from .models import Address, Company, User, Geo, Post

admin.site.register(Address)
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Geo)
admin.site.register(Post)
