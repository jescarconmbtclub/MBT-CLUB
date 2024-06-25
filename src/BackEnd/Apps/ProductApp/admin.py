from django.contrib import admin
from django.templatetags.static import static
from .models import Vajilla, Medallas, Llaveros, Banderines, ObjetoMagico, Arrojadizos, Medallon
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class VajillaResource(resources.ModelResource):
    class Meta:
       model = Vajilla

class VajillaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'material', 'tipo_taza'] # Barra de búsqueda por título
    list_display = ('id', 'nombre', 'material', 'precio', 'precio_rebajado', 'medidas', 'descripcion', 'imagen_url', 'volumen', 'tipo_taza') # Nombra las columnas
    resource_class = VajillaResource



class MedallasResource(resources.ModelResource):
    class Meta:
       model = Medallas

class MedallasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'material', 'sujeccion_medalla'] # Barra de búsqueda por título
    list_display = ('id', 'nombre', 'material', 'precio', 'precio_rebajado', 'medidas', 'descripcion', 'imagen_url', 'sujeccion_medalla') # Nombra las columnas
    resource_class = MedallasResource


class LlaverosResource(resources.ModelResource):
    class Meta:
       model = Llaveros

class LlaverosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'material', 'sujeccion_llavero'] # Barra de búsqueda por título
    list_display = ('id', 'nombre', 'material', 'precio', 'precio_rebajado', 'medidas', 'descripcion', 'imagen_url', 'sujeccion_llavero') # Nombra las columnas
    resource_class = LlaverosResource



class BanderinesResource(resources.ModelResource):
    class Meta:
       model = Banderines

class BanderinesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'material'] # Barra de búsqueda por título
    list_display = ('id', 'nombre', 'material', 'precio', 'precio_rebajado', 'medidas', 'descripcion', 'imagen_url') # Nombra las columnas
    resource_class = BanderinesResource


class ObjetoMagicoResource(resources.ModelResource):
    class Meta:
       model = ObjetoMagico

class ObjetoMagicoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'material'] # Barra de búsqueda por título
    list_display = ('id', 'nombre', 'material', 'precio', 'precio_rebajado', 'medidas', 'descripcion', 'imagen_url') # Nombra las columnas
    resource_class = ObjetoMagicoResource


class ArrojadizosResource(resources.ModelResource):
    class Meta:
       model = Arrojadizos

class ArrojadizosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'material'] # Barra de búsqueda por título
    list_display = ('id', 'nombre', 'material', 'precio', 'precio_rebajado', 'medidas', 'descripcion', 'imagen_url') # Nombra las columnas
    resource_class = ArrojadizosResource


class MedallonResource(resources.ModelResource):
    class Meta:
       model = Medallon

class MedallonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'material', 'sujeccion_medallon'] # Barra de búsqueda por título
    list_display = ('id', 'nombre', 'material', 'precio', 'precio_rebajado', 'medidas', 'descripcion', 'imagen_url', 'sujeccion_medallon') # Nombra las columnas
    resource_class = MedallonResource


admin.site.register(Vajilla, VajillaAdmin)
admin.site.register(Medallas, MedallasAdmin)
admin.site.register(Llaveros, LlaverosAdmin)
admin.site.register(Banderines, BanderinesAdmin)
admin.site.register(ObjetoMagico, ObjetoMagicoAdmin)
admin.site.register(Arrojadizos, ArrojadizosAdmin)
admin.site.register(Medallon, MedallonAdmin)
