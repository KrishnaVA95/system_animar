from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=127, unique=True)
    value = models.FloatField()
    emphasis = models.BooleanField(null=True, default=False)
    image = models.ImageField(upload_to='assets/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    # Relacionamento com Category, ou campo com opçones já declaradas
    def __repr__(self) -> str:
        return f"<Product ({self.id}) - ({self.name})>"