from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Name of category', max_length=50, null=False, blank=False)
    slug = models.SlugField(unique=True, verbose_name="URL")

    def __str__(self):
        return f"{self.pk} - {self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Actor(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="First name")
    last_name = models.CharField(max_length=30, verbose_name="Last name")
    bio = models.TextField(verbose_name="biography")
    photo = models.ImageField(verbose_name="Image", default="default.png", upload_to='movies/')
    slug = models.SlugField(unique=True, db_index=True, verbose_name="URL")

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("actor_view", kwargs={"actor_slug": self.slug})

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"
        ordering = ['last_name']


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="category"
    )
    description = models.TextField(
        verbose_name="Description",
        null=True,
        blank=True
    )
    year = models.PositiveSmallIntegerField(verbose_name="Year of production")
    poster = models.ImageField(
        "Poster",
        default="poster.png",
        upload_to="movies/"
    )
    actors = models.ManyToManyField(Actor, related_name="movie_actor")
    budget = models.PositiveIntegerField(
        verbose_name="Budget",
        default=0,
        help_text="million of US dollars"
    )
    genre = models.ManyToManyField(Genre, verbose_name="Genre")
    slug = models.SlugField(unique=True)

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"movie_slug": self.slug})

    def get_director(self):
        return self.director_set.all()

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        ordering = ['year']
        indexes = [
            models.Index(fields=('created_at',))
        ]


class Director(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="First name")
    last_name = models.CharField(max_length=30, verbose_name="Last name")
    bio = models.TextField(verbose_name="biography")
    photo = models.ImageField(verbose_name="Image", default="default.png", upload_to='movies/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Movie")
    slug = models.SlugField(unique=True, db_index=True, verbose_name="URL")

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("director_view", kwargs={"director_slug": self.slug})

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directors"
        ordering = ['last_name']


class Screenshot(models.Model):
    image = models.ImageField("Image", upload_to="movies/screenshots")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_shots")

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    class Meta:
        verbose_name = "Screenshot"
        verbose_name_plural = "Screenshots"
