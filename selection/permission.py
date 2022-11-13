from rest_framework.permissions import BasePermission

from users.models import User


class SelectionPermission(BasePermission):
    message = 'not access for its owner'

    def has_object_permission(self, request, view, obj):
        if obj.owner != request.user:
            return False
        return True


class AdPermission(BasePermission):
    message = 'This user not allowed editing'

    def has_object_permission(self, request, view, obj):
        if obj.author.id == request.user.id:
            return True
        elif request.user.role not in (User.ROLE[1][0], User.ROLE[2][0]):  # пользователь не является модератором или администратором
            return True
        return False
