from django.db import models

# Create your models here.


class Transaction(models.Model):
    date = models.DateField(blank=True, auto_now_add=True)
    amount = models.IntegerField(null=False)
    transaction_type = models.CharField(
        choices=[("Expense", "Expense"), ("Income", "Income")], max_length=255
    )
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, null=False, related_name="transactions"
    )
