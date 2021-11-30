from django.db import models

class Documentation(models.Model):
    Doc_Type = models.CharField(max_length=32)
    Doc_URL = models.CharField(max_length=124)

    def __str__(self):
        return str(self.Doc_Type + " @ " + self.Doc_URL)
