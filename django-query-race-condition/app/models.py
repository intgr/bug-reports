from django.db import models


class Fk1(models.Model):
    value = models.CharField(max_length=100)


class Fk2(models.Model):
    value = models.CharField(max_length=100)


class Fk3(models.Model):
    value = models.CharField(max_length=100)


class Fk4(models.Model):
    value = models.CharField(max_length=100)


class Fk5(models.Model):
    value = models.CharField(max_length=100)

class Fk6(models.Model):
    value = models.CharField(max_length=100)


class Fk7(models.Model):
    value = models.CharField(max_length=100)


class Fk8(models.Model):
    value = models.CharField(max_length=100)


class Fk9(models.Model):
    value = models.CharField(max_length=100)


class Fk10(models.Model):
    value = models.CharField(max_length=100)


class Fk11(models.Model):
    value = models.CharField(max_length=100)


class Fk12(models.Model):
    value = models.CharField(max_length=100)


class Fk13(models.Model):
    value = models.CharField(max_length=100)


class Fk14(models.Model):
    value = models.CharField(max_length=100)


class Fk15(models.Model):
    value = models.CharField(max_length=100)


class Fk16(models.Model):
    value = models.CharField(max_length=100)


class Fk17(models.Model):
    value = models.CharField(max_length=100)


class Fk18(models.Model):
    value = models.CharField(max_length=100)


class Fk19(models.Model):
    value = models.CharField(max_length=100)


class Fk20(models.Model):
    value = models.CharField(max_length=100)


class Root(models.Model):
    fk1 = models.ForeignKey(Fk1, on_delete=models.CASCADE)
    fk2 = models.ForeignKey(Fk2, on_delete=models.CASCADE)
    fk3 = models.ForeignKey(Fk3, on_delete=models.CASCADE)
    fk4 = models.ForeignKey(Fk4, on_delete=models.CASCADE)
    fk5 = models.ForeignKey(Fk5, on_delete=models.CASCADE)
    fk6 = models.ForeignKey(Fk6, on_delete=models.CASCADE)
    fk7 = models.ForeignKey(Fk7, on_delete=models.CASCADE)
    fk8 = models.ForeignKey(Fk8, on_delete=models.CASCADE)
    fk9 = models.ForeignKey(Fk9, on_delete=models.CASCADE)
    fk10 = models.ForeignKey(Fk10, on_delete=models.CASCADE)
    fk11 = models.ForeignKey(Fk11, on_delete=models.CASCADE)
    fk12 = models.ForeignKey(Fk12, on_delete=models.CASCADE)
    fk13 = models.ForeignKey(Fk13, on_delete=models.CASCADE)
    fk14 = models.ForeignKey(Fk14, on_delete=models.CASCADE)
    fk15 = models.ForeignKey(Fk15, on_delete=models.CASCADE)
    fk16 = models.ForeignKey(Fk16, on_delete=models.CASCADE)
    fk17 = models.ForeignKey(Fk17, on_delete=models.CASCADE)
    fk18 = models.ForeignKey(Fk18, on_delete=models.CASCADE)
    fk19 = models.ForeignKey(Fk19, on_delete=models.CASCADE)
    fk20 = models.ForeignKey(Fk20, on_delete=models.CASCADE)
