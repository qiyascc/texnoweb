from django.db import models

class CarouselImage(models.Model):
    POSITION_CHOICES = [
        (1, 'İlk'),
        (2, 'İkinci'),
        (3, 'Üçüncü')
    ]
    position = models.PositiveSmallIntegerField(choices=POSITION_CHOICES, unique=True, default=1)
    image = models.ImageField(upload_to='carousel_images/')


# New.html
class News(models.Model):
    main_image = models.ImageField(upload_to='news_images/')
    short_description = models.TextField()
    description = models.TextField()

    def snippet(self):
        return self.short_description[:30]
    

# Projects.html


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Başlık', default='Baslik yok')
    description = models.TextField(verbose_name='Küçük Açıklama', default='Açıklama yok')
    category = models.CharField(max_length=50, choices=[('software', 'Software'), ('hardware', 'Hardware'), ('biology', 'Biology')], default='software')



class Image(models.Model):
    image = models.ImageField(upload_to='projects/images/', verbose_name='Fotoğraf')
    projects = models.ManyToManyField(Project, related_name='project_image',verbose_name='Fotoğraflar')

    alt_text = models.CharField(max_length=200, verbose_name='Fotoğraf Alt Metni')



class Startup(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    full_text = models.TextField()
    image = models.ImageField(upload_to='startups/')
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.title