from django.db import models


class Question(models.Model):
    
    question = models.CharField(max_length=120)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question

class Choice(models.Model): 
    question_txt = models.ForeignKey(Question, on_delete=models.CASCADE)  
    choice = models.CharField(max_length=120)

    def __str__(self):
        return self.choice

