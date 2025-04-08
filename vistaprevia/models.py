from django.db import models
from django.utils.html import format_html
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100,blank=True, db_index=True)

    def __str__(self):
        return '%s' % self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=200) 

    def __str__(self, ):
        return '%s' % self.nombre
    
    
class Producto(models.Model):
    Tamaños= (
        ('1K', '1K'),
        ('1_5L','1,5L'),
        ('2_5', '2,5'),
        ('3L', '3L'),
        ('500g', '500g'),
        ('900g','900g'),
        ('120g','120g')
        )

    Tipo=[
        ('Zero','Zero'),
        ('Clasica','Clasica'),
        ('Pomelo','Pomelo'),
        ('Manzana','Manzana'),
        ('Naranja','Naranja')
        ]
    
    nombre= models.CharField(max_length=100, null=True,blank=True )
    precio= models.IntegerField()
    stock= models.IntegerField()
    fecha_ingreso= models.DateField(null= True, blank=True)
    #Tablas concatenadas
    categoria=models.ForeignKey(Categoria,blank=False, null=True, on_delete=models.CASCADE)# relacion con tabla categoria
    marca= models.ForeignKey(Marca, on_delete=models.CASCADE) #relacion con tabla marca
    imagen = models.ImageField(upload_to='productos/%Y/%m/%d/', null=True, blank=True) #nueva 


   #quise evitar usar mas tablas innecesarias
    tipo = models.CharField(max_length=100, choices=Tipo, null=True,blank=True)
    tamaños = models.CharField(max_length=100, choices=Tamaños, null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.nombre and self.marca:
            self.nombre= self.marca.nombre
        super().save(*args, **kwargs)
    

    def Stock(self):
        if self.stock <=10:
            return format_html('<span style="color: #DB180D;">{}</span>', self.stock)
        return self.stock
        
    
    def Precio(self):
        return format_html('<span>${}</span>', self.precio)
    

    def __str__(self):
        return f" {self.categoria} - {self.marca} - {self.precio} - {self.nombre} - {self.tipo or ''} - {self.tamaños}-{self.fecha_ingreso}" 
        
    
