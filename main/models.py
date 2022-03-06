from django.db import models


class Account(models.Model):
    creation_date = models.DateField()
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    account_type = models.CharField(max_length=50)

    def __str__(self):
        return "username : " + self.user_name + ", account type : " + self.account_type


class Persson(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name + " " + self.first_name


class Sanction(models.Model):
    desiniation = models.CharField(max_length=100, verbose_name="la cause de la sanction")
    date_end = models.DateField(verbose_name="la date de la fin de sanction ")
    person = models.ForeignKey(Persson, on_delete=models.CASCADE)

    def __str__(self):
        return "sanction " + str(self.date_end)


class Riter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    filed = models.CharField(max_length=100, verbose_name="domaine")
    image = models.ImageField()
    abstract = models.TextField()
    copy_number = models.IntegerField(default=0, verbose_name="nombre d'exemplaire")
    riter = models.ManyToManyField(Riter)

    def __str__(self):
        return self.title


class Exemplaire(models.Model):
    decription = models.CharField(max_length=50)
    embrinte = models.BooleanField(verbose_name="déja emprinté", default=False)  # a revoire
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.livre) + " : " + self.decription


class Inscription(models.Model):
    inscription_date = models.DateTimeField()
    borrow_date = models.DateTimeField(verbose_name="date d'emprunt")
    delvery_date = models.DateTimeField(verbose_name="date de remise")
    served = models.BooleanField(verbose_name="déja servie", default=False)
    persson = models.ForeignKey(Persson, on_delete=models.CASCADE)
    exemplaire = models.ForeignKey(Exemplaire, on_delete=models.CASCADE)


class Order(models.Model):
    Order_date = models.DateTimeField()
    served = models.BooleanField(verbose_name="déja servie", default=False)
    Persson = models.ForeignKey(Persson, on_delete=models.CASCADE)
