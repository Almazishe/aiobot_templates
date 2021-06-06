from tortoise import fields, models


class Product(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    price = fields.FloatField(default=100)

    def __str__(self):
        return self.name
