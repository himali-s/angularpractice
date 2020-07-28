from django.db import models

#we create folder covers where we save all the images
def upload_path(instance, filename):
    return '/'.join(['covers', str(instance.title), filename])

#upload_to = it will be the file_path we want to upload our image to
class Book(models.Model):
    title = models.CharField(max_length= 256, blank=False)
    covers = models.ImageField(blank=True, null = True, upload_to=upload_path)





