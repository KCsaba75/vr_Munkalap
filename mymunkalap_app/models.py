from django.db import models

# Create your models here.
class Megrendelo(models.Model):
    nev = models.CharField(max_length=255)
    cim = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefon = models.IntegerField()
    rendszam = models.CharField(max_length=10)
    gyartmany = models.CharField(max_length=255)
    tipus = models.CharField(max_length=255)
    gyartasi_ev = models.IntegerField()
    alvazszam = models.CharField(max_length=50)

    def __str__(self):
        return f"Név: {self.nev} ,    ,  Cím: {self.cim}   , Rendszám: {self.rendszam}"
    


class Hibatipusok(models.Model):
     hiba = models.CharField(max_length=255)

     def __str__(self):
        return self.hiba



class Munkalap(models.Model):
    megrendelo_id = models.ForeignKey(Megrendelo, on_delete=models.CASCADE)
    datum = models.DateTimeField(auto_now_add=True)
    utolsomodositas=models.DateTimeField(auto_now=True)
    MUNKALAPSTATUS_CHOICES = [('enum_value_1', 'Aktív'), ('enum_value_2', 'Lezárt')]
    munkalapstatus = models.CharField(max_length=20, choices=MUNKALAPSTATUS_CHOICES)
    munkalapszam = models.CharField(unique=True ,max_length=20)
    kmoraallas = models.IntegerField()
    UZEMENYAGSZINT_CHOICES = [('enum_value_1', 'Negyed'), ('enum_value_2', 'Fél'),('enum_value_3', 'Háromnegyed'), ('enum_value_4', 'Tele')]
    uzemenyagszint = models.CharField(max_length=20, choices=UZEMENYAGSZINT_CHOICES)
    hibatipus_id = models.ForeignKey(Hibatipusok, on_delete=models.CASCADE)
    hibaleiras = models.TextField()
    varhatohatarido = models.DateField()
    elvegzettmunka = models.TextField(blank=True)
    felhasznaltanyag = models.TextField(blank=True)

    def __str__(self):
        return self.munkalapszam +  '________ ' + self.hibaleiras
