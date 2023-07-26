from django.db import models


class Dashboard(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    spending_this_month = models.IntegerField()
    expected_spending_this_month = models.IntegerField()
    percentage_over_under_this_month = models.FloatField()
