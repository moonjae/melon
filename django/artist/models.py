from django.db import models


# Create your models here.
class Artist(models.Model):

    BLOOD_TYPE_A = 'a'
    BLOOD_TYPE_B = 'b'
    BLOOD_TYPE_O = 'o'
    BLOOD_TYPE_AB = 'c'
    BLOOD_TYPE_OTHER = 'x'
    CHOICES_BLOOD_TYPE = (
        (BLOOD_TYPE_A, 'A형'),
        (BLOOD_TYPE_B, 'B형'),
        (BLOOD_TYPE_O, 'O형'),
        (BLOOD_TYPE_AB, 'AB형'),
        (BLOOD_TYPE_OTHER, 'Other')
    )

    img_profile = models.ImageField('프로필이미지', upload_to = 'artist', blank= True)

    name = models.CharField('이름', max_length = 50)

    real_name = models.CharField('본명', max_length = 30, blank= True)

    nationality = models.CharField('국적', max_length =50)

    birth_date = models.DateField('생년원일', blank= True, null= True)

    constellation = models.CharField('별자리', max_length = 50)

    blood_type = models.CharField('혈액형', max_length = 1, choices = CHOICES_BLOOD_TYPE, blank = True)

    intro = models.TextField(
        '소개',
        blank=True,
    )






    def __str__(self):
        return self.name

