from django.db import models
from django.templatetags.static import static
error_img_url = "https://www.shutterstock.com/image-vector/error-500-page-empty-symbol-260nw-1711106146.jpg"


class Vajilla(models.Model):
   
    material_choices = [
        ('Cerámica', 'Cerámica'),
        ('Cristal', 'Cristal'),
    ]
    tipo_taza_choices = [
        ('Tazas', 'Tazas'),
        ('Vasos de Chupito', 'Vasos de Chupito'),
        ('Jarra', 'Jarra'),
        ('Platos', 'Platos'),
        ('Vaso Vaquero', 'Vaso Vaquero'),
    ]
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=50, choices=material_choices, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_rebajado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medidas = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    imagen_url = models.URLField(default=error_img_url, blank=True, null=True)
    volumen = models.CharField(max_length=100, blank=True, null=True)
    tipo_taza = models.CharField(max_length=50, choices=tipo_taza_choices, blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Vajilla'
        verbose_name_plural = 'Vajillas'

    
class Medallas(models.Model):
    
    material_choices = [
        ('Metal', 'Metal'),
        ('Madera', 'Madera'),
        ('PLA(3d)', 'PLA(3d)'),
        ('Goma Eva', 'Goma Eva'),
        ('Cerámica', 'Cerámica'),
        ('Cristal', 'Cristal'),
        ('Tejido', 'Tejido'),
        ('Espuma', 'Espuma'),
    ]
   
    sujeccion_medalla_choices = [
        ('Imperdible', 'Imperdible'),
        ('Imán', 'Imán'),
    ]
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=50, choices=material_choices, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_rebajado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medidas = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    imagen_url = models.URLField(default=error_img_url, blank=True, null=True)
    sujeccion_medalla = models.CharField(max_length=50, choices=sujeccion_medalla_choices, blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Medalla'
        verbose_name_plural = 'Medallas'

class Llaveros(models.Model):
    material_choices = [
        ('Metal', 'Metal'),
        ('Madera', 'Madera'),
        ('PLA(3d)', 'PLA(3d)'),
        ('Goma Eva', 'Goma Eva'),
        ('Cerámica', 'Cerámica'),
        ('Cristal', 'Cristal'),
        ('Tejido', 'Tejido'),
        ('Espuma', 'Espuma'),
    ]
   
    sujeccion_llavero_choices = [
        ('Anilla', 'Anilla'),
        ('Cadena', 'Cadena'),
        ('Cierre de Plástico', 'Cierre de Plástico'),
    ]
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=50, choices=material_choices, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_rebajado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medidas = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    imagen_url = models.URLField(default=error_img_url, blank=True, null=True)
    sujeccion_llavero = models.CharField(max_length=50, choices=sujeccion_llavero_choices, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Llavero'
        verbose_name_plural = 'Llaveros'
        
class Banderines(models.Model):
    material_choices = [
        ('Metal', 'Metal'),
        ('Madera', 'Madera'),
        ('PLA(3d)', 'PLA(3d)'),
        ('Goma Eva', 'Goma Eva'),
        ('Cerámica', 'Cerámica'),
        ('Cristal', 'Cristal'),
        ('Tejido', 'Tejido'),
        ('Espuma', 'Espuma'),
    ]
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=50, choices=material_choices, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_rebajado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medidas = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    imagen_url = models.URLField(default=error_img_url, blank=True, null=True)
    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Banderin'
        verbose_name_plural = 'Banderines'    
class ObjetoMagico(models.Model):
    material_choices = [
        ('Metal', 'Metal'),
        ('Madera', 'Madera'),
        ('PLA(3d)', 'PLA(3d)'),
        ('Goma Eva', 'Goma Eva'),
        ('Cerámica', 'Cerámica'),
        ('Cristal', 'Cristal'),
        ('Tejido', 'Tejido'),
        ('Espuma', 'Espuma'),
    ]
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=50, choices=material_choices, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_rebajado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medidas = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    imagen_url = models.URLField(default=error_img_url, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Objeto Magico'
        verbose_name_plural = 'Objetos Magicos'    
class Arrojadizos(models.Model):
    material_choices = [
        ('Metal', 'Metal'),
        ('Madera', 'Madera'),
        ('PLA(3d)', 'PLA(3d)'),
        ('Goma Eva', 'Goma Eva'),
        ('Cerámica', 'Cerámica'),
        ('Cristal', 'Cristal'),
        ('Tejido', 'Tejido'),
        ('Espuma', 'Espuma'),
    ]
        
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=50, choices=material_choices, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_rebajado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medidas = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    imagen_url = models.URLField(default=error_img_url, blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Arrojadizo'
        verbose_name_plural = 'Arrojadizos'       
        
class Medallon(models.Model):
    material_choices = [
        ('Metal', 'Metal'),
        ('Madera', 'Madera'),
        ('PLA(3d)', 'PLA(3d)'),
        ('Goma Eva', 'Goma Eva'),
        ('Cerámica', 'Cerámica'),
        ('Cristal', 'Cristal'),
        ('Tejido', 'Tejido'),
        ('Espuma', 'Espuma'),
    ]
   
    sujeccion_medallon_choices = [
        ('Cadena', 'Cadena'),
        ('Cordón', 'Cordón'),
        ('Cuero', 'Cuero'),
    ]
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=50, choices=material_choices, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_rebajado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medidas = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    imagen_url = models.URLField(default=error_img_url, blank=True, null=True)
    sujeccion_medallon = models.CharField(max_length=50, choices=sujeccion_medallon_choices, blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Medallon'
        verbose_name_plural = 'Medallones'  