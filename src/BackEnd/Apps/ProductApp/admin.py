from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Vajilla, Medallas, Llaveros, Banderines, ObjetoMagico, Arrojadizos, Medallon

# Define resources for each model for import-export functionality
class VajillaResource(resources.ModelResource):
    class Meta:
        model = Vajilla

class VajillaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'material', 'tipo_taza', 'codigo']  # Agregamos 'codigo' a los campos de búsqueda
    list_display = ('id', 'codigo', 'nombre', 'material', 'precio', 'precio_rebajado', 'medidas', 'descripcion', 'imagen_url', 'volumen', 'tipo_taza')  # Agregamos 'codigo' antes del 'nombre'
    resource_class = VajillaResource

class MedallasResource(resources.ModelResource):
    class Meta:
        model = Medallas

class MedallasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'material', 'sujeccion_medalla', 'codigo']  # Agregamos 'codigo' a los campos de búsqueda
    list_display = ('id', 'codigo', 'nombre', 'material', 'precio', 'precio_rebajado', 'medidas', 'descripcion', 'imagen_url', 'sujeccion_medalla')  # Agregamos 'codigo' antes del 'nombre'
    resource_class = MedallasResource

class LlaverosResource(resources.ModelResource):
    class Meta:
        model = Llaveros

class LlaverosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'material', 'sujeccion_llavero', 'codigo']  # Agregamos 'codigo' a los campos de búsqueda
    list_display = ('id', 'codigo', 'nombre', 'material', 'precio', 'precio_rebajado', 'medidas', 'descripcion', 'imagen_url', 'sujeccion_llavero')  # Agregamos 'codigo' antes del 'nombre'
    resource_class = LlaverosResource

class BanderinesResource(resources.ModelResource):
    class Meta:
        model = Banderines

class BanderinesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'material', 'codigo']  # Agregamos 'codigo' a los campos de búsqueda
    list_display = ('id', 'codigo', 'nombre', 'material', 'precio', 'precio_rebajado', 'medidas', 'descripcion', 'imagen_url')  # Agregamos 'codigo' antes del 'nombre'
    resource_class = BanderinesResource

class ObjetoMagicoResource(resources.ModelResource):
    class Meta:
        model = ObjetoMagico

class ObjetoMagicoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'material', 'codigo']  # Agregamos 'codigo' a los campos de búsqueda
    list_display = ('id', 'codigo', 'nombre', 'material', 'precio', 'precio_rebajado', 'medidas', 'descripcion', 'imagen_url')  # Agregamos 'codigo' antes del 'nombre'
    resource_class = ObjetoMagicoResource

class ArrojadizosResource(resources.ModelResource):
    class Meta:
        model = Arrojadizos

class ArrojadizosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'material', 'codigo']  # Agregamos 'codigo' a los campos de búsqueda
    list_display = ('id', 'codigo', 'nombre', 'material', 'precio', 'precio_rebajado', 'medidas', 'descripcion', 'imagen_url')  # Agregamos 'codigo' antes del 'nombre'
    resource_class = ArrojadizosResource

class MedallonResource(resources.ModelResource):
    class Meta:
        model = Medallon

class MedallonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'material', 'sujeccion_medallon', 'codigo']  # Agregamos 'codigo' a los campos de búsqueda
    list_display = ('id', 'codigo', 'nombre', 'material', 'precio', 'precio_rebajado', 'medidas', 'descripcion', 'imagen_url', 'sujeccion_medallon')  # Agregamos 'codigo' antes del 'nombre'
    resource_class = MedallonResource

# Register models with their respective admin classes
admin.site.register(Vajilla, VajillaAdmin)
admin.site.register(Medallas, MedallasAdmin)
admin.site.register(Llaveros, LlaverosAdmin)
admin.site.register(Banderines, BanderinesAdmin)
admin.site.register(ObjetoMagico, ObjetoMagicoAdmin)
admin.site.register(Arrojadizos, ArrojadizosAdmin)
admin.site.register(Medallon, MedallonAdmin)
