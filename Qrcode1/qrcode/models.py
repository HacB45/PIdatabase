from django.db import models

# Create your models here.

class Caso(models.Model):
    caso=models.CharField(max_length=255)
    idmaquina=models.CharField(max_length=10, default='anything')
    def __str__(self):
        return self.caso

class Historico(models.Model):
    avaria=models.CharField(max_length=255)
    idmaquina=models.CharField(max_length=10, default='anything')
    dataabertura=models.CharField(max_length=50, default='anything')
    datafecho=models.CharField(max_length=50, default='anything')
    problema=models.CharField(max_length=100, default='anything')
    solicitante=models.CharField(max_length=50, default='anything')
    planificador=models.CharField(max_length=50, default='anything')
    def __str__(self):
        return self.avaria

class Avarias(models.Model):
    avarias=models.CharField(max_length=255)
    idmaquina=models.CharField(max_length=10, default='anything')
    ot=models.CharField(max_length=50, default='anything')
    estado=models.CharField(max_length=50, default='anything')
    dataabertura=models.CharField(max_length=50, default='anything')
    datafecho=models.CharField(max_length=50, default='anything')
    problema=models.CharField(max_length=100, default='anything')
    solicitante=models.CharField(max_length=50, default='anything')
    planificador=models.CharField(max_length=50, default='anything')
    def __str__(self):
        return self.avarias        

class Informacao(models.Model):
    informacao=models.CharField(max_length=255)
    idmaquina=models.CharField(max_length=10, default='anything')
    estadomaquina=models.CharField(max_length=50, default='anything')
    image=models.ImageField(upload_to='Images/',default='Images/None/No-img.jpg')
    doc=models.FileField(upload_to='Doc/',default='Doc/None/No-doc.pdf')
    video=models.FileField(upload_to='Video/',default='Video/None/No-vid.mp4')
    def __str__(self):
        return self.informacao 

class Fotos(models.Model):
    info=models.CharField(max_length=255)
    idmaquina=models.CharField(max_length=10, default='anything')
    passo=models.CharField(max_length=50, default='anything')
    image=models.ImageField(upload_to='Images/',default='Images/None/No-img.jpg')
    def __str__(self):
        return self.info
