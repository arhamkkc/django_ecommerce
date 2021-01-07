from django.db import models

# Create your models here.




class Category(models.Model):
    objects = models.Manager()
    product_category = models.CharField(max_length=100,blank=True,null=True)




    def __str__(self):
        return self.product_category


    def get_products(self):
        return Product.objects.filter(category = self)




class Product(models.Model):
    objects = models.Manager()
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    pub_date = models.DateField(max_length=50)
    image = models.ImageField(upload_to='store/images')

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.CharField(max_length=1000)



    def __str__(self):
        return self.name
    
    

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


    

    