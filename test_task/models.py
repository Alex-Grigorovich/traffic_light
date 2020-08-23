from django.db import models


class User(models.Model):
    name = models.CharField(verbose_name='full_name', max_length=70)
    username = models.CharField(verbose_name='username', max_length=50)
    email = models.EmailField(verbose_name='email', max_length=254, blank=True)
    phone = models.CharField(verbose_name='phone', max_length=30, blank=True)
    website = models.URLField(verbose_name='website', max_length=100, blank=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return 'name: {}'.format(self.name)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Address(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='address')
    street = models.CharField(verbose_name='street', max_length=50)
    suite = models.CharField(verbose_name='suite', max_length=10)
    city = models.CharField(verbose_name='city', max_length=50, blank=True)
    zipcode = models.CharField(verbose_name='zipcode', max_length=10, blank=True)

    def __str__(self):
        return 'address: {}'.format(self.id)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class Geo(models.Model):
    address = models.OneToOneField('Address', on_delete=models.CASCADE, related_name='geo')
    latitude = models.FloatField(verbose_name='latitude', max_length=90, blank=True)
    longitude = models.FloatField(verbose_name='longitude', max_length=180, blank=True)

    def __str__(self):
        return 'latitude: {}, longitude: {}'.format(self.latitude, self.longitude)

    class Meta:
        verbose_name = 'Geo'
        verbose_name_plural = 'Geos'


class Company(models.Model):
    company_name = models.CharField(verbose_name='name_company', max_length=30)
    catchPhrase = models.TextField(verbose_name='catch_phrase', max_length=100, blank=True)
    bs = models.TextField(verbose_name='bs', max_length=100, blank=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return 'company: {}'.format(self.company_name)


class Post(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='posts')
    title = models.TextField(verbose_name='title', max_length=200, blank=True)
    body = models.TextField(verbose_name='body', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return 'title: {}'.format(self.title)
