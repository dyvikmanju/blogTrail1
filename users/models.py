from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from cloudinary.models import CloudinaryField


from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import cloudinary.uploader

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='media/default_nhoexz.jpg')

    def save(self, *args, **kwargs):
        # Only upload if image is a new local file, not a public ID
        if self.image and hasattr(self.image, 'file'):
            upload_result = cloudinary.uploader.upload(
                self.image,
                folder='media/profile_pics'
            )
            self.image = upload_result['public_id']
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self,*args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
