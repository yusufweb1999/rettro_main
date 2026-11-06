from django.forms import ModelForm  # type: ignore
from .models import ariza


class shopModelForm(ModelForm):
    class Meta:
        model = ariza
        fields = ['ism familya', 'shikoyat turi', 'qanday muammo']
        
from django.db import models


class Application(models.Model):
    CRIME_TYPES = [
        ("fraud", "Firibgarlik"),
        ("vol_zakrol", "O'g'irlik"),
        ("threat", "Tahdid"),
        ("violence", "Zo'ravonlik"),
        ("cybercrime", "Kiberjinoyat"),
         ("so'kma", "So'kish"),
        ("other", "Boshqa"),
    ]

    first_name = models.CharField(max_length=100, verbose_name="Ism")
    last_name = models.CharField(max_length=100, verbose_name="Familiya")
    created_at = models.DateTimeField(auto_now_add=True)
    crime_type = models.CharField(
        max_length=20,
        choices=CRIME_TYPES,
        verbose_name="Jinoyat turi"
    )

    description = models.TextField(
        verbose_name="Prablema haqida ma'lumot"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Ariza yuborilgan vaqt"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.created_at}"
