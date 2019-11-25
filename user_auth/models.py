from django.db import models


class Prefecture(models.Model):
    """
    遊びたいエリア指定のための県クラス
    """
    prefecture = models.CharField(
        verbose_name='遊びたい地域',
        max_length=20
    )
    
    def __str__(self):
        return self.prefecture


class Participants(models.Model):
    """
    参加者のリスト
    """
    participant = models.IntegerField(
        verbose_name='参加者のtwitterID'
    )

    def __str__(self):
        return self.participant


class Recruitment(models.Model):
    # 募集に必要な情報。
    username = models.CharField(
        verbose_name='あなたの名前',
        max_length=100,
    )
    # 隠しフィールド
    userid = models.IntegerField(
        verbose_name='ID',
    )
    game = models.CharField(
        verbose_name='プレイしたいボードゲームやジャンル',
        max_length=100,
        default='',
        blank=False,
    )
    number = models.IntegerField(
        verbose_name='募集人数'
    )
    participant = models.ManyToManyField(
        Participants
    )
    area = models.ManyToManyField(
        Prefecture,
        verbose_name='遊びたい地域（県）',
        blank=False,
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

    def __str__(self):
        return self.username
