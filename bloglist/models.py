from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User 
from django.urls import reverse
#from taggit.managers import TaggableManager

class PublishedManager(models.Manager): 
    def get_queryset(self): 
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Categoria(models.Model):
    descrizione = models.CharField(max_length=30)  

    def __str__(self): 
        return self.descrizione        

class Post(models.Model): 
    STATUS_CHOICES = ( 
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    ) 
    title = models.CharField(max_length=250) 
    image = models.ImageField(upload_to='images', blank=True)
    slug = models.SlugField(max_length=250) 
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               related_name='blog_posts') 
    body = models.TextField() 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=10,  
                              choices=STATUS_CHOICES, 
                              default='draft') 

    objects = models.Manager() # The default manager. 
    published = PublishedManager() # Our custom manager.   
    #tags = TaggableManager()                           

    class Meta: 
        ordering = ('-publish',) 

    def __str__(self): 
        return self.title 
        

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.slug])    

                     


#python3 manage.py makemigrations bloglist
#python3 manage.py migrate
#python3 manage.py runserver

#Post.objects.filter(categoria__descrizione='google-ads')