from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from .models import User, Agent, Lead, UserProfile, Category

# class hash(UserAdmin):
#     pass

admin.site.register(Category)
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(UserProfile)