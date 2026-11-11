from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    altura = models.FloatField()
    peso = models.FloatField()

class Dui(models.Model):
    codigo = models.CharField(max_length=10)
    persona = models.OneToOneField(Persona,on_delete=models.CASCADE)
    fechaexp = models.DateField()
    fechaven = models.DateField()

class Artista(models.Model):
    nartistico = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=100)

class Album(models.Model):
    nombre = models.CharField(100)
    artista = models.ForeignKey(Artista,on_delete=models.CASCADE)
    fechalanzamiento = models.DateField()
    rating = models.IntegerField()


class Cancion(models.Model):
    nombre = models.CharField(100)
    artista = models.ForeignKey(Artista,on_delete=models.CASCADE)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    duracion = models.FloatField()    

class Playlist(models.Model):
    nombre  = models.CharField(100)
    cancion = models.ManyToManyField(Cancion)