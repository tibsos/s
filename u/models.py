from django.db import models as m

from django.contrib.auth.models import User

class Profile(m.Model):

    CATEGORIES = (

        ('Бизнес', 'Бизнес'),
        ('Образование', 'Бизнес'),

    )
    PLANS = (

        ('Бизнес', 'Бизнес'),
        ('Образование', 'Бизнес'),

    )

    user = m.ForeignKey(User, on_delete = m.CASCADE, related_name = 'profile')

    name = m.TextField()
    email = m.EmailField()
    category = m.CharField(max_length = 20, choices = CATEGORIES)
    plan = m.CharField(max_length = 20, choices = PLANS)

    class Meta:

        ordering = ['name']
    
    def __str__(self):

        return self.user.username