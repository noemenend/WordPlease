from rest_framework.permissions import BasePermission


class BlogPermission(BasePermission):

    def has_permission(self, request, view):
        return view.action in ['list', 'retrieve'] or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return view.action == 'retrieve' or obj.author == request.user or request.user.is_superuser
