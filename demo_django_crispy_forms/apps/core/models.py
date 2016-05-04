from django.db import models
from django_countries.fields import CountryField


class Registration(models.Model):
    """
    Modèle de l'inscription
    """
    CIVILITY_CHOICES = (
        ('M.', 'M.'),
        ('MME', 'Mme')
    )
    STREET_TYPE_CHOICES = (
        ('Boulevard', 'Boulevard'),
        ('Avenue', 'Avenue'),
        ('Cours', 'Cours'),
        ('Place', 'Place'),
        ('Rue', 'Rue'),
        ('Route', 'Route'),
        ('Voie', 'Voie'),
        ('Chemin', 'Chemin'),
        ('Square', 'Square'),
        ('Impasse', 'Impasse'),
        ('Rond-point', 'Rond-point'),
        ('Quai', 'Quai')
    )

    civility = models.CharField(max_length=3, choices=CIVILITY_CHOICES,
                                default='M.', verbose_name="Civilité")
    birth_name = models.CharField(max_length=255, verbose_name="Nom de naissance")
    last_name = models.CharField(max_length=255, blank=True, null=True,
                                 verbose_name="Nom d'usage ou marital")
    first_name = models.CharField(max_length=255, verbose_name="Prénom")
    birth_date = models.DateField(verbose_name="Date de naissance ")
    birth_place = models.CharField(max_length=255, verbose_name="Ville de naissance")
    birth_country = CountryField(max_length=255, verbose_name="Pays de naissance")
    mail = models.EmailField(max_length=255, verbose_name="Mail")
    street_type = models.CharField(max_length=30, verbose_name="Type de rue",
                                   choices=STREET_TYPE_CHOICES, default='Rue')
    street_number = models.CharField(max_length=30, verbose_name="Numéro de rue")
    street = models.CharField(max_length=30, verbose_name="Rue")
    comp_1 = models.CharField(max_length=255, verbose_name="Complément 1",
                              blank=True, null=True)
    comp_2 = models.CharField(max_length=255, verbose_name="Complément 2",
                              blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name="Ville")
    zip_code = models.CharField(max_length=255, verbose_name="Code postal")
    country = CountryField(max_length=255, verbose_name="Pays")
    phone = models.CharField(max_length=255, blank=True, null=True,
                             verbose_name="Téléphone")
    comments = models.TextField(blank=True, null=True, verbose_name="Commentaires")
