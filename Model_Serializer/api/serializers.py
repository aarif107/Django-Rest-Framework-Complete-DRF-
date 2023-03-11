from rest_framework import serializers
from .models import Student




class StudentSerializer(serializers.ModelSerializer):

        #Validators
    def start_with_c(value):
        if value[0].lower() != 'c':
            raise serializers.ValidationError('Name should be start with c')

    name=serializers.CharField(validators=[start_with_c])

    class Meta:
        model=Student
        fields=['id','name','roll','city'] 
        # read_only_fields=['name'] 

        #Field Level Validation
    def validate_roll(self,value):
        if value >= 100:
            raise serializers.ValidationError('Seat Full')
        return value


        #Object Level Validation
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower() == 'zara' and ct.lower() != 'istanbul':
            raise serializers.ValidationError('City must be istanbul')
        return data

