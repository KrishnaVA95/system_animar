from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=127, unique=True)
    emphasis = models.BooleanField(null=True, default=False)
    image = models.ImageField(upload_to='assets/')
    description = models.TextField()
    content = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    def __repr__(self) -> str:
        return f"<Post ({self.id}) - ({self.title})>"