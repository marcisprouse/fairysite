from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager



from PIL import Image


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')
    author_pic = models.FileField(upload_to='blog/img', null=True, blank=True, default='blog/img/pic_filler.jpg')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.author_pic.path)
        if img.mode in ("RGBA", "P"): img = img.convert("RGB")
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.author_pic.path)
    class CatChoice(models.TextChoices):
        Branding = 'Branding'
        Design = 'Design'
        Tech = 'Tech'
        Development = 'Development'
        Marketing = 'Marketing'
    category = models.CharField(max_length=25, choices=CatChoice.choices, default=CatChoice.Tech)
    abstract_title = models.CharField(max_length=250, blank=True, default=None)
    abstract = models.TextField(null=True, blank=True)
    subheading_one = models.CharField(max_length=250, blank=True, default=None)
    body = models.TextField(null=True, blank=True)
    body_b = models.TextField(null=True, blank=True)
    body_c = models.TextField(null=True, blank=True)
    subheading_two = models.CharField(max_length=250, blank=True, default=None)
    body_two = models.TextField(null=True, blank=True)
    blog_img = models.FileField(upload_to='blog/img', null=True, blank=True)
    blog_img_larger = models.FileField(upload_to='blog/img', null=True, blank=True)
    img_caption_long = models.TextField(null=True, blank=True)
    img_caption_short = models.CharField(max_length=250, blank=True, default=None)
    quote = models.TextField(null=True, blank=True)
    quote_author = models.CharField(max_length=250, blank=True, default=None)
    code = models.TextField(null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])

class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'



