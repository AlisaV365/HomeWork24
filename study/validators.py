from rest_framework import serializers

SCAN_URL = ['youtube.com', 'https://youtube.com', 'http://youtube.com', 'https://youtu.be']


def validator_urlvideo(value):
    if not value.lower() in SCAN_URL:
        raise serializers.ValidationError("Возможно добавление видео только опубликованные на youtube.com.")
