from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes,permission_classes


from .models import CustomeUser

class UserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        password= validated_data.pop('')
       

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance


    class Meta:
        model = CustomeUser
        extra_kwargs={'passwprd':{'write_only':True}} 
        fields =('name','email','password','phone','gender','is_active','is_staff','is_superuser')

