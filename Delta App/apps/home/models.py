from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Ansad_db(models.Model):
 
    # Fields
    annee = models.PositiveBigIntegerField(help_text='Annee de l execution', verbose_name='Annee',validators=[MinValueValidator(2000), MaxValueValidator(2050)])
    lib_chap = models.CharField(max_length=1000, help_text='lib de chapitre', verbose_name='Nom', null=True, blank=True)
    Libellé_SSCHAP= models.CharField(max_length=1000, help_text='lib de sous chapitre', verbose_name='Nom', null=True, blank=True)
    
    C_PART =  models.PositiveBigIntegerField(verbose_name='C_PART')
    C_ART =  models.PositiveBigIntegerField(verbose_name='C_ART')
    C_PGPH = models.PositiveBigIntegerField(verbose_name='C_PGPH')
    
    DOTATION =  models.PositiveBigIntegerField(verbose_name='DOTATION')
    INDISPONIBLE  =  models.PositiveBigIntegerField(verbose_name='INDISPONIBLE')
    Indisp	 =  models.PositiveBigIntegerField(verbose_name='Indisp')
    DISPONIBLE  =  models.PositiveBigIntegerField(verbose_name='DISPONIBLE')
    

    #lib operation 
    LIBELLE = models.CharField(max_length=1000, help_text='lib de sous chapitre', verbose_name='lib_operation', null=True, blank=True)

    #class_compte= models.ForeignKey('id', help_text='id_compte cclassification', verbose_name='id', on_delete=models.SET_NULL, null=True)


class classification(models.Model):

    lib_chap = models.CharField(max_length=1000, help_text='lib de chapitre',null=True, verbose_name='Nom', blank=True)
    LIBELLE = models.CharField(max_length=1000, help_text='lib de sous chapitre', verbose_name='lib_operation', null=True, blank=True)


    Epi_Epac = models.CharField(max_length=50, help_text='EPI/EPAC',verbose_name='EPI/EPAC')
    Branche =  models.CharField(max_length=50, help_text='BRANCHE',verbose_name='BRANCHE')
    Secteur =  models.CharField(max_length=50, help_text='SECTEUR',verbose_name='SECTEUR')
    Si = models.CharField(max_length=50, help_text='SI',verbose_name='SI')
    Operation = models.CharField(max_length=50, help_text='PRODUIT',verbose_name='PRODUIT')