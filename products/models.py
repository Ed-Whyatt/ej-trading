from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Products(models.Model):

    class Meta:
        verbose_name_plural = 'Products'

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    full_name = models.CharField(max_length=254, null=True, blank=True)
    brand = models.CharField(max_length=254, null=True, blank=True)
    promotion_qr_code = models.CharField(max_length=254, null=True, blank=True)
    barcode = models.DecimalField(max_digits=50, decimal_places=0, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    wholsale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    batch_no = models.DecimalField(max_digits=50, decimal_places=0, null=True, blank=True)
    stock = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    img_paths = models.ImageField(null=True, blank=True)
    mark_up = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    expiry = models.DateField(null=True, blank=True)
    on_carousel_one = models.BooleanField(default=False)
    on_carousel_two = models.BooleanField(default=False)
    on_carousel_three = models.BooleanField(default=False)

    def __str__(self):
        return self.name
