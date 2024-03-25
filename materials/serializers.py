from rest_framework import serializers
from materials.models import Course, Lesson, Subscription
from materials.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='video_url')]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    subscribe = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()

    def get_subscribe(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(owner=user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
