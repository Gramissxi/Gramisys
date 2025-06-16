from django.db import models
from django.utils.html import format_html
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100,blank=True, db_index=True)

    def __str__(self):
        return '%s' % self.nombre
    
class Subcategoria(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='subcategorias') 

    def __str__(self, ):
        return f'{self.nombre}'

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
        ('Limón','Limón'),
        ('Pera','Pera'),
        ('Uva','Uva'),
        ('Naranja','Naranja'),
        ('Durazno','Durazno'),
        ('Frutilla','Frutilla'),
        ('Tirabuzón','Tirabuzón'),
        ('Limonada','Limonada'),
        ('Sprite','Sprite'),
        ('Tónica','Tónica'),
        ('Spaghetti','Spaghetti'),
        ('Moño','Moño'),
        ('Fusilli','Fusilli'),
        ('Codito','Codito'),
        ('Cinta','Cinta'),
        ('Fetuccine','Fettuccine'),
        ('Mostacchioli','Mostaccioli'),
        ('Dadito','Dadito'),
        ('Caracol','Caracol'),
        ('Integral','Integral'),
        ('Fino','Fino'),
        ('Largo','Largo'),
        ('Descremada','Descremada'),
        ('Entera','Entera'),
        ('Semidescremada','Semidescremada'),
        ('Descremada saborizada','Descremada saborizada'),
        ('Entera saborizada','Entera saborizada'),
        ('Semidescremada saborizada','Semidescremada saborizada'),
        ('Al aceite', 'Al aceite'),
        ('Al natural', 'Al natural')
        ]
    nombre = models.CharField(max_length=255, blank=True, null=True)  
    precio= models.IntegerField()
    stock= models.IntegerField()
    fecha_ingreso= models.DateField(null= True, blank=True)
    #Tablas concatenadas
    subcategoria=models.ForeignKey(Subcategoria,blank=False, null=True, on_delete=models.CASCADE, related_name='productos')# relacion con tabla categoria
    marca= models.ForeignKey(Marca, on_delete=models.CASCADE) #relacion con tabla marca
    imagen = models.ImageField(upload_to='productos/%Y/%m/%d/', null=True, blank=True) #nueva 

   #quise evitar usar mas tablas innecesarias
    tipo = models.CharField(max_length=100, choices=Tipo, null=True,blank=True)
    tamaños = models.CharField(max_length=100, choices=Tamaños, null=True,blank=True)

    def save(self, *args, **kwargs):
        partes = [str(self.subcategoria), str(self.marca)]
        if self.tipo:
            partes.append(str(self.tipo))
        self.nombre = " ".join(partes)
        super().save(*args, **kwargs)

    

    def Stock(self):
        if self.stock <=10:
            return format_html('<span style="color: #DB180D;">{}</span>', self.stock)
        return self.stock
        
    
    def Precio(self):
        return format_html('<span>${}</span>', self.precio)
    

    def __str__(self):
        return f" {self.subcategoria.categoria} - {self.subcategoria} -- {self.marca} - {self.precio} - {self.nombre} - {self.tipo or ''} - {self.tamaños}-{self.fecha_ingreso}" 
        
    
