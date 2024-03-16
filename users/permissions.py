from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderator').exists()


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return request.method in ('GET', 'PUT', 'PATCH', 'DELETE')
        return False
