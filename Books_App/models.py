from django.db import models

# Create your models here.
class Books_Data(models.Model):
    ISLAMIC = 'Islamic'
    NOVEL = 'Novel'
    NINETH_CLASS = 'Nineth_Class'
    TENTH_CLASS = 'Tenth_Class'
    ELEVEN_CLASS = 'Eleven_Class'
    TWELTH_CLASS = 'Twelth_Class'
    COMMON = 'Common'
    TYPES = [(ISLAMIC,'Islamic'),(NOVEL,'Novel'),(NINETH_CLASS,'Nineth_Class'),(TENTH_CLASS,'Tenth_Class'),(ELEVEN_CLASS,'Eleven_Class'),(TWELTH_CLASS,'Twelth_Class'),(COMMON , 'Common')]
    img = models.ImageField(upload_to='media',max_length=100)
    cat_type = models.CharField(max_length=20,choices=TYPES,default=COMMON)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    rate = models.PositiveIntegerField(default=0)
    owner = models.CharField(max_length=50)
    Contact = models.CharField(max_length=15)

def get_absolute_url(self):
    return reverse('contact_person' , args=[str(self.id)])
