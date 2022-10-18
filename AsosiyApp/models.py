from django.db import models

class Shop(models.Model):
    boss=models.ForeignKey('Boss',on_delete=models.CASCADE)
    shop_name=models.CharField(max_length=50)
    shop_logo=models.CharField(max_length=50)
    shop_adress=models.CharField(max_length=50)
    shop_contact=models.CharField(max_length=50)
    def __str__(self):
        return self.shop_name

class Boss(models.Model):
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    tel=models.CharField(max_length=50)
    login=models.CharField(max_length=15)
    password=models.CharField(max_length=15)

    class Meta:
        ordering=['First_name',]
        # verbose_name="Sheff"
        # verbose_name_plural="Sheff_1"
        get_latest_by='login'
        # db_table = 'X'
        # abstract = True
    def __str__(self):
        return self.First_name+" "+self.Last_name




class Product(models.Model):
    Product_name=models.CharField(max_length=50)
    Category=models.ForeignKey('Category',on_delete=models.CASCADE)
    price=models.CharField(max_length=50)
    Brand=models.ForeignKey('Brend',on_delete=models.CASCADE)
    weight=models.CharField(max_length=50)
    Size=models.ForeignKey('Size',on_delete=models.CASCADE)
    Create_date=models.CharField(max_length=50)
    Shop=models.ForeignKey('Shop',on_delete=models.CASCADE)
    Validity_date=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    Color=models.CharField(max_length=50)
    Image=models.ForeignKey('Image',on_delete=models.CASCADE)
    def __str__(self):
        return self.Product_name

class Category(models.Model):
    Name=models.CharField(max_length=50)
    def __str__(self):
        return self.Name

class Brend(models.Model):
    Name=models.CharField(max_length=50)
    Brend_logo=models.CharField(max_length=50)
    Brend_country=models.CharField(max_length=50)
    Brend_rating=models.CharField(max_length=50)
    def __str__(self):
        return self.Name

class Size(models.Model):
    size_name=models.CharField(max_length=4)
    def __str__(self):
        return self.size_name
class Image(models.Model):
    Image_url=models.CharField(max_length=50)
    def __str__(self):
        return self.Image_url[:10]

class Shopping(models.Model):
    Product=models.ForeignKey('Product',on_delete=models.CASCADE)
    Customer=models.ForeignKey('Customer',on_delete=models.CASCADE)
    Shopping_date=models.DateTimeField(auto_now_add=True)
    Price_sum=models.CharField(max_length=50)
    Card_number=models.CharField(max_length=50)
    Shop=models.ForeignKey('Shop',on_delete=models.CASCADE)
    Brend=models.ForeignKey('Brend',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Shopping_date)

class Customer(models.Model):
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Tel=models.CharField(max_length=50)
    Card_date_valid=models.CharField(max_length=50)
    Shop_cart=models.CharField(max_length=50)
    def __str__(self):
        return self.First_name+" "+self.Tel

class Cart_product(models.Model):
    Product=models.ForeignKey('Product',on_delete=models.CASCADE)
    Customer=models.ForeignKey('Customer',on_delete=models.CASCADE)

class Payment_history(models.Model):
    Shopping=models.ForeignKey('Shopping',on_delete=models.CASCADE)
    Customer=models.ForeignKey('Customer',on_delete=models.CASCADE)
