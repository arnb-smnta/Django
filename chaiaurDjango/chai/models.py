from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta  # Add this import

# Create your models here.


class ChaiVariety(models.Model):
    chaitype_choice = [("ml", "Masala"), ("pl", "plain"), ("nm", "no milk")]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chais/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=chaitype_choice)
    description = models.TextField(default="")

    def __str__(self):
        return self.name


class review(models.Model):
    # one to many
    rating_stars = [
        (1, "⭐"),
        (2, "⭐⭐"),
        (3, "⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (5, "⭐⭐⭐⭐⭐"),
    ]
    chai = models.ForeignKey(
        ChaiVariety, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(choices=rating_stars)
    comments = models.CharField(max_length=500)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name} is({self.get_rating_display()})"


class store(models.Model):
    # Many to many
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    ChaiVariety = models.ManyToManyField(
        ChaiVariety, related_name="store"
    )  # Dusri field mein aap kya naam se jane jaoge


class chaiCertificate(models.Model):
    # one to one
    chai = models.OneToOneField(
        ChaiVariety, on_delete=models.CASCADE, related_name="ChaiCertificate"
    )
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.valid_untill:
            self.valid_untill = self.issued_date + timedelta(days=5 * 365)
        super().save(*args, **kwargs)

        def __str__(self):
            return f"chai certificate  for {self.chai.name}"
