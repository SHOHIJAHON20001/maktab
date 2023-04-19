from django.db import models


STATUS = [
    ("1-sinf", "1_sinf"),
    ("2-sinf", "2_sinf"),
    ("3-sinf", "3_sinf"),
    ("4-sinf", "4_sinf"),
    ("5-sinf", "5_sinf"),
    ("6-sinf", "6_sinf"),
    ("7-sinf", "7_sinf"),
    ("8-sinf", "8_sinf"),
    ("9-sinf", "9_sinf"),
]



class School(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveBigIntegerField(default=7)
    student_class = models.CharField(max_length=255, choices=STATUS)
    monday_pay = models.PositiveBigIntegerField(default=1)
    tuesday_pay = models.PositiveBigIntegerField(default=1)
    wednesday_pay = models.PositiveBigIntegerField(default=1)
    thursday_pay = models.PositiveBigIntegerField(default=1)
    friday_pay = models.PositiveBigIntegerField(default=1)
    saturday_pay = models.PositiveBigIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    


    class Meta:
        ordering = ["id"]
        verbose_name = "School"
        verbose_name_plural = "School"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def week_payment(self):
        week = self.monday_pay+self.tuesday_pay+self.wednesday_pay+self.thursday_pay+self.friday_pay+self.saturday_pay
        return week
    
    def month_payment(self):
        week = self.monday_pay+self.tuesday_pay+self.wednesday_pay+self.thursday_pay+self.friday_pay+self.saturday_pay
        month = week*4
        return month
    
    def year_payment(self):
        week = self.monday_pay+self.tuesday_pay+self.wednesday_pay+self.thursday_pay+self.friday_pay+self.saturday_pay
        year = week*48
        return year
