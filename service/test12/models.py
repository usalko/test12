from django.db import models

# Create your models here.


class Order(models.Model):
    '''
        # Order
            - created_at
            - email
    '''

    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    email = models.EmailField()

    @property
    def all_ataches(self):
        return list(self.attached_files.all())

    class Meta:
        app_label  = 'test12'


class AttachedFile(models.Model):
    '''
        # Atached file
            - order
            - attached_file
    '''

    order = models.ForeignKey(
        Order, related_name='attached_files', on_delete=models.CASCADE)
    attached_file = models.FileField(upload_to='order/')
    
    def __str__(self) -> str:
        return f'id:{self.id}\tname:{self.attached_file.name}'

    class Meta:
        app_label  = 'test12'

