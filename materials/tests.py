from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.ru'
        )
        self.course = Course.objects.create(
            name="test_course",
            owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name='test_lesson',
            course=self.course,
            owner=self.user
        )
        self.client.force_authenticate(
            user=self.user
        )

    def test_create_lesson(self):
        """ Тестирование создания урока """

        data = {
            'name': 'test lesson',
            'description': 'test lesson',
            'course': self.course.id,
            'owner': self.user.id
        }
        response = self.client.post(
            reverse('materials:lesson_create'),
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(Lesson.objects.all().exists())


    def test_list_lessons(self):
        """ Тестирование вывода списка уроков """

        response = self.client.get(
            reverse('materials:lesson_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        # print(response.json())

        self.assertEquals(
            response.json(),
            # {'count': 1, 'next': None, 'previous': None, 'results': [
            #     {'id': 2, 'name': 'test_lesson', 'image': None, 'description': '', 'video_url': None, 'course': 2,
            #      'owner': 2}]}
        {
            'count': 1, 'next': None, 'previous': None, 'results':
            [{
                'id': self.lesson.id,
                'name': self.lesson.name,
                'image': self.lesson.image,
                'description': self.lesson.description,
                'video_url': self.lesson.video_url,
                'course': self.lesson.course.id,
                'owner': self.lesson.owner.id}]
            }
        )

    def test_update_lesson(self):
        """ Тестирование редактирования урока """
        update_data = {
            'name': 'update lesson',
            'description': 'update lesson',
            # "image": "https://www.youtube.com/watch?v=fYNMZWxwxQE&ab_channel=%D0%9C%D0%A3%D0%97",
            'course': self.course.id,
            'owner': self.lesson.owner.id
        }

        response = self.client.put(
            reverse('materials:lesson_update', kwargs={'pk': self.lesson.id}),
            data=update_data
        )
        # self.client.force_authenticate(user=self.user)

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """ Тестирование удаления урока """

        response = self.client.delete(
            reverse('materials:lesson_delete', kwargs={'pk': self.lesson.id}),
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@test.ru'
        )
        self.course = Course.objects.create(
            name='course 1',
            description='course 1',
            owner=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):
        """ Тестирование подписки на курс """

        data = {
            'course': self.course.id,
        }

        response = self.client.post(
            reverse('materials:subscription'),
            data=data
        )
        # print(response.json())
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            {'message': 'подписка добавлена'}
        )
