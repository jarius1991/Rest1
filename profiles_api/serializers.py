from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        #chcemy tylko aby password byl przesyłany ale nie dało się go pobrać
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},  # widoczne gwiazdki jak wpisujesz
            },
        }

    # serializer pozwala uzyc domyslej funkcji managera modelu, my chcemy to nadpisać
    # aby użyć gwiazdek zmiast czystego tekstu
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user


class ProfileFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user', 'status_text', 'created_on')
        extra_kwargs = {
            'user': {
                'read_only': True,
            }
        }