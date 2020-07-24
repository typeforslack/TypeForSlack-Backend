from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import PractiseLog,Paragraph,DashboardData
from django.utils import timezone

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paragraph
        fields=['id','taken_from','para']        

    def create(self,validated_data):
        taken_from=validated_data['taken_from'].lower()
        savedpara=Paragraph.objects.create(taken_from=taken_from,para=validated_data['para'])
        return savedpara


class PractiseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=PractiseLog
        fields=["para","wpm","taken_at","correct_words","wrong_words","total_words","accuracy","mode"]
        extra_kwargs = {'para': {'write_only': True}}

    def create(self,validated_data):
        user=self.context['request'].user
        result=user.practiselog_set.create(para=validated_data['para'],wpm=validated_data['wpm'],correct_words=validated_data['correct_words'],wrong_words=validated_data['wrong_words'],total_words=validated_data['total_words'],accuracy=validated_data['accuracy'],taken_at=validated_data['taken_at'],mode=validated_data['mode'])
        return result

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']
    
    def create(self,validated_data):
        user=User.objects.create_user(username=validated_data['username'],password=validated_data['password'],email=validated_data['email'])
        token=Token.objects.create(user=user)
        return token,user

class StreakSerializer(serializers.ModelSerializer):
    class Meta:
        model=DashboardData
        fields='__all__'
        extra_kwargs={'user':{'write_only':True}}

    