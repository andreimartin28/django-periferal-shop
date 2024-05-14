from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import UserManager
from django.utils import timezone

from shopapp.libraries.validations import FirstNameValidator, LastNameValidator, EmailValidator

# Create your models here.


class User(AbstractUser):

    username_validator = UnicodeUsernameValidator()
    firstname_validator = FirstNameValidator()
    lastname_validator = LastNameValidator()
    email_validator = EmailValidator()

    username = models.CharField(
                                max_length=70,
                                unique=True,
                                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                                validators=[username_validator],
                                error_messages={
                                    "unique": "A user with that username already exists.",
                                },
                                )

    first_name = models.CharField(
                                  blank=True,
                                  max_length=50,
                                  validators=[firstname_validator],
                                  error_messages={
                                      "unique": "First name is invalid. Try again.",
                                  },
                                  )

    last_name = models.CharField(
                                 blank=True,
                                 max_length=50,
                                 validators=[lastname_validator],
                                 error_messages={
                                     "unique": "Last name is invalid. Try again."
                                 }
                                 )

    phone_number = models.CharField(
                                    blank=True,
                                    max_length=10,
                                    help_text="Format: 07********"
                                    )

    email = models.EmailField(
                              max_length=100,
                              blank=True,
                              unique=True,
                              validators=[email_validator]
                              )

    is_staff = models.BooleanField(
                                    default=False,
                                    help_text="Designates whether the user can log into this admin site.",
                                    )

    is_active = models.BooleanField(
                                    default=True,
                                    help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
                                    )

    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)

    image = models.ImageField(default='/profile_pics/profile_photo_man.jpg',
                              upload_to='profile_pics',
                              help_text="Get a representative profile image.")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,
             force_insert=False,
             force_update=False,
             using=None,
             update_fields=None):
        super().save(force_insert,
                     force_update,
                     using,
                     update_fields)


class Category(models.Model):
    name = models.CharField(max_length=100)

    slug = models.SlugField(null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Currency(models.Model):
    name = models.CharField(max_length=10)

    slug = models.SlugField(null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

# currency_list = [
#     ("RON", "RON"),
#     ("EURO", "EURO")
# ]


class Color(models.Model):
    name = models.CharField(max_length=100)

    slug = models.SlugField(null=True)

    def __str__(self):
        return f"{self.name}"

# color_list = [
#     ("black", "black"),
#     ("white", "white")
# ]


class Brand(models.Model):
    name = models.CharField(max_length=150)

    slug = models.SlugField(null=True)

    def __str__(self):
        return f"{self.name}"


# brand_list = [
#     ('Logitech', 'Logitech'),
#     ('Steelseries', 'Steelseries'),
#     ('Razer', 'Razer'),
#     ('LG', 'LG'),
#     ('Dell', 'Dell'),
# ]


class Product(models.Model):
    image = models.ImageField(null=False,
                              blank=False)

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)

    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE)

    name = models.CharField(max_length=200,
                            null=False,
                            blank=False)

    slug = models.SlugField(null=True)

    color = models.ForeignKey(Color,
                              on_delete=models.CASCADE)

    stocks = models.IntegerField(blank=False,
                                 null=False)

    price = models.IntegerField(blank=False,
                                null=False)

    currency = models.ForeignKey(Currency,
                                 on_delete=models.CASCADE)

    description = models.TextField()

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.name}"

    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total > 0:
            return reviews_total / self.reviews.count()

        return 0


class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = [
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped'),
    ]

    user = models.ForeignKey(User,
                             related_name='orders',
                             on_delete=models.CASCADE)

    first_name = models.CharField(max_length=255)

    last_name = models.CharField(max_length=255)

    email = models.CharField(max_length=255)

    address = models.CharField(max_length=255)

    optional_address = models.CharField(max_length=255,
                                        blank=True,
                                        null=True)

    phone = models.CharField(max_length=255)

    country = models.CharField(max_length=255)

    city = models.CharField(max_length=255)

    zip_code = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)

    paid_amount = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default=ORDERED)

    class Meta:
        ordering = ('-created_at',)

    def get_total_price(self):
        if self.paid_amount:
            return self.paid_amount

        return 0


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)

    product = models.ForeignKey(Product,
                                related_name='items',
                                on_delete=models.CASCADE)

    price = models.IntegerField(blank=False,
                                null=False)

    quantity = models.IntegerField(default=1)

    def get_total_price(self):
        return self.price


class Review(models.Model):
    product = models.ForeignKey(Product,
                                related_name='reviews',
                                on_delete=models.CASCADE)

    title = models.CharField(max_length=100,
                             null=True)

    rating = models.IntegerField(default=3)

    content = models.TextField()

    created_by = models.ForeignKey(User,
                                   related_name='reviews',
                                   on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
