# File: room/models.py

from django.db import models

class RuangPercobaan(models.Model):
    id_room = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    gedung = models.CharField(max_length=100)
    lantai = models.IntegerField()
    ket = models.TextField()
    svg_text = models.TextField(null=True, blank=True)  # Ubah svg menjadi TextField

    def __str__(self):
        return self.nama

class Jadwal(models.Model):
    id_jadwal = models.AutoField(primary_key=True)
    room = models.ForeignKey(RuangPercobaan, on_delete=models.CASCADE)
    code_jadwal = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    penanggung_jawab = models.CharField(max_length=100)
    waktu_mulai = models.DateTimeField()
    waktu_selesai = models.DateTimeField()
    ket = models.TextField()
    pdf = models.FileField(upload_to='pdf_files/', null=True, blank=True)

    def hitung_rentang_waktu(self):
        rentang_waktu = self.waktu_selesai - self.waktu_mulai
        return rentang_waktu

class FeedbackRuangan(models.Model):
    id_feedback = models.AutoField(primary_key=True)
    room = models.ForeignKey(RuangPercobaan, on_delete=models.CASCADE)
    komentar = models.TextField()
    rating = models.IntegerField()
    waktu_submit = models.DateTimeField(auto_now_add=True)
    penulis = models.CharField(max_length=100)
    STATUS_CHOICES = (
        ('reply', 'Reply'),
        ('nonreply', 'Non-Reply'),
    )
    status_feedback = models.CharField(max_length=20, choices=STATUS_CHOICES)

class FeedbackAplikasi(models.Model):
    id_feedback = models.AutoField(primary_key=True)
    kategori = models.CharField(max_length=100)
    komentar = models.TextField()
    rating = models.IntegerField()
    waktu_submit = models.DateTimeField(auto_now_add=True)
    penulis = models.CharField(max_length=100)
    STATUS_CHOICES = (
        ('reply', 'Reply'),
        ('nonreply', 'Non-Reply'),
    )
    status_feedback = models.CharField(max_length=20, choices=STATUS_CHOICES)
