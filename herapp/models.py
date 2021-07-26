from django.db import models

# Create your models here.
class Photo(models.Model):
    resim = models.ImageField(upload_to='images')
    resim_adı = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Resim'
        verbose_name_plural = 'AnasayfadaPaylaşılanResimler'
    
    def __str__(self):
        return self.resim_adı


class NakliyeFoto(models.Model):
    resim = models.ImageField(upload_to='images')
    resim_adi = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'NakliyeResim'
        verbose_name_plural = 'NakliyeResimleri'
    
    def __str__(self):
        return self.resim_adi

class BriketKomur(models.Model):
    resim = models.ImageField(upload_to='images')
    resim_adi = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'BriketKomurResim'
        verbose_name_plural = 'BriketKomurResimleri'
    
    def __str__(self):
        return self.resim_adi


class MeseKomur(models.Model):
    resim = models.ImageField(upload_to='images')
    resim_adi = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'MeseKomurResim'
        verbose_name_plural = 'MeseKomurResimleri'
    
    def __str__(self):
        return self.resim_adi

class PresSosisMangalKuru(models.Model):
    resim = models.ImageField(upload_to='images')
    resim_adi = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'PresSosisMangalKuruResim'
        verbose_name_plural = 'PresSosisMangalKuruResimleri'
    
    def __str__(self):
        return self.resim_adi

class NargileKomuru(models.Model):
    resim = models.ImageField(upload_to='images')
    resim_adi = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'NargileKömürResim'
        verbose_name_plural = 'NargileKömürüResimleri'
    
    def __str__(self):
        return self.resim_adi

class Message(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField(max_length=254)
    message= models.TextField()

    def __str__(self):
        return self.name

class Urunler(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Urunler'
        verbose_name_plural = 'Ürünlerim'
    
    def __str__(self):
        return self.name

