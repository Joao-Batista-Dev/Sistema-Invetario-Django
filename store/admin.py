from django.contrib import admin
from .models import Brand, Category, RegisterProduct, RegisterUser, Movement, Maintenance, EquipmentStatus

@admin.register(RegisterUser)
class RegisterUserAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'password',)

@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ('register_product', 'movement_type', 'date_time', 'responsible', 'sector', 'status')

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('product', 'maintenance_date', 'description', 'performed_by',)

@admin.register(EquipmentStatus)
class EquipmentStatusAdmin(admin.ModelAdmin):
    list_display = ('product', 'status', 'changed_at',)
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'id',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    

@admin.register(RegisterProduct)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
