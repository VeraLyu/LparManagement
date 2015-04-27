from django.db import models

class LPAR(models.Model):
    name = models.CharField(max_length=15, null=True, blank=False)
    ip = models.IPAddressField(blank=False)
    available = models.BooleanField(default=1)
    reservation_time = models.DateTimeField(auto_now_add=True)
    rsv_person = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def get_status(self):
        return self.available

    def set_status(self, avail):
        self.available = avail
        self.save()

    def get_reservation_time(self):
        return self.reservation_time

    def set_reservaiton_time(self, time):
        self.reservation_time = time
        self.save()

class Server(models.Model):
    name = models.CharField(max_length=15, null=True, blank=False)
    ip = models.IPAddressField(blank=False)
    imm_ip = models.IPAddressField(blank=False)
    available = models.BooleanField(default=1)
    rsv_person = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def get_status(self):
        return self.available

    def set_status(self, avail):
        self.available = avail
        self.save()
