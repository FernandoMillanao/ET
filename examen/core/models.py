from django.db import models

# Create your models here.


#Modelo para categoria

class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')


    def __str__(self):
        return self.nombreCategoria


#Modelo para jardineria

class Flores(models.Model):
    flores = models.IntegerField(verbose_name='Flores')
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


    def __int__(self):
        return self.flores
    
class maceteros(models.Model):
    
    macetas = models.IntegerField(verbose_name='Macetas')

    def __int__(self):
        return self.macetas

class Tierradehojas(models.Model):
    tierradehojas = models.IntegerField(verbose_name='Tierra de hojas')


    def __int__(self):
        return self.tierradehojas

class Arbustos(models.Model):
    arbustos = models.IntegerField()
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __int__(self):
        return self.arbustos

