from django.db import models

class Detail(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Detail, on_delete = models.CASCADE)
    comment_text = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.comment_text
    


