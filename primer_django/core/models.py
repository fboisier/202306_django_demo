from django.db import models
    
class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    ano_lanzamiento = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"({self.id}) {self.title}"

class Plataforma(models.Model):


    class TipoPago(models.TextChoices):
        CREDITO = 'C', 'CREDITO'
        EFECTIVO = 'E', 'EFECTIVO'
        AUTOMATICO = 'A', 'AUTOMATICO'

    nombre = models.CharField(max_length=100)
    tipo_pago = models.CharField(choices=TipoPago.choices, max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"({self.id}) {self.nombre}"
    

class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='autor/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE)
    image = models.ImageField(upload_to='libros/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.title} - {self.author.name}"

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
