from django.db import models


class MagicCard(models.Model):
    name = models.CharField(max_length=255)
    current_value = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming the value is in dollars
    description = models.TextField()
    image_url = models.URLField(max_length=200, null=True)
    mana_cost = models.CharField(max_length=255)  # Assuming the mana cost is a string (e.g., "2UU")

    def __str__(self):
        return self.name
