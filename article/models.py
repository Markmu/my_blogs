from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Tag(models.Model):
    category = models.CharField(max_length = 50, blank = True)

    def __str__(self):
        return self.category

class Article(models.Model):
    tag = models.ForeignKey(Tag, blank=True, null=True,
                            on_delete=models.SET_NULL)
    title = models.CharField(max_length = 100)
    date_time = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True, null = True)

    def get_absolute_url(self):
            path = reverse('page', args=[self.id])
            return "http://127.0.0.1:8000%s" % (path,)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']
