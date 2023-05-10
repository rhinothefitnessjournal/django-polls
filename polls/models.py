from django.db import models

class Hashtag(models.Model):
    idHashtag = models.IntegerField(primary_key=True)
    tag = models.CharField(max_length=45, unique=True)

class Usuário(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=True)
    nickname = models.CharField(max_length=100, unique=True)
    avatar = models.CharField(max_length=255, null=True)

class Quiz(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45, null=True)
    data_criacao = models.CharField(max_length=45)
    capa = models.CharField(max_length=45, null=True)
    Usuário = models.ForeignKey(Usuário, on_delete=models.CASCADE)

class Hashtag_has_Quiz(models.Model):
    Hashtag_idHashtag = models.IntegerField()
    Quiz_id = models.IntegerField()
    Hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    Quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('Hashtag_idHashtag', 'Quiz_id')
