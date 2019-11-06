from django.db import models

class Recruitment(models.Model):
    # 募集に必要な情報。
    game = models.CharField(
        verbose_name='プレイしたいボードゲームやジャンル',
        max_length=100,
        default=''
        blank=False
    )
    area = models.ManyToManyField(
        Prefecture,
        verbose_name='遊びたい地域（県）'
        blank=False
    )
    place = models.CharField(
        verbose_name='遊びたいカフェや場所',
        max_length=100,
    )
    date = models.DateField(
        verbose_name='遊びたい日時',
    )
    comment = models.TextField(
        verbose_name='その他コメントなど',
        max_length='400',
    )

class Prefecture(models.Model):
    """
    遊びたいエリア指定のための県クラス
    """
    prefecture = models.CharField(
        verbose_name='遊びたい地域',
    )
    
    def __str__(self):
        return self.prefecture