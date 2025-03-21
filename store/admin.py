from django.contrib import admin
from .models import RegisterProduct, RegisterUser

@admin.register(RegisterUser)
class RegisterUserAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'password',)

@admin.register(RegisterProduct)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
