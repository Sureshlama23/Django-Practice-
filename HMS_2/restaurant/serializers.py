from rest_framework import serializers
from restaurant.models import Menu,Food

class Menuserializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

    def validate(self,menu):

        if menu['name']:
            for n in menu['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'status': 403, 'error':'Name must not be digit!'})
        return menu
        
class Foodserializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

    def validate(self,food):

        if food['name']:
            for n in food['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'status': 403, 'error':'Name must not be digit!'})
        return food
        
