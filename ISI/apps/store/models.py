from io import BytesIO
from django.core.files import File
from django.db import models
from PIL import Image

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)

    def __str__(self):
        return self.title

class Product(models.Model):
      category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
      title = models.CharField(max_length=255)
      slug = models.SlugField(max_length=255)
      description = models.TextField(blank=True, null=True)
      price = models.FloatField()
      id = models.AutoField(primary_key=True)

      image = models.ImageField(upload_to='uploads/', blank=True, null=True)
      thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
      
      

      

      def __str__(self):
          return self.title
      
      def save(self, *args, **kwargs):
          print('Save',)
          self.thumbnail = self.make_thumbnail(self.image)

          super().save(*args, **kwargs)

      def make_thumbnail(self, image, size=(300, 200)):
          img =  Image.open(image)
          img.convert('RGB')
          img.thumbnail(size)

          thumb_io = BytesIO()
          img.save(thumb_io, 'JPEG', quality=85)

          thumbnail = File(thumb_io, name=image.name)
           
          return thumbnail