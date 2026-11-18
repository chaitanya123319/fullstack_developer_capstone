from django.db import models


class Dealer(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.TextField()
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    dealer = models.ForeignKey(
        Dealer,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    name = models.CharField(max_length=100)
    review = models.TextField()
    purchase = models.CharField(max_length=100, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    sentiment = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.dealer.name}"