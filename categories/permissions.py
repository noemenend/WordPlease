from rest_framework.permissions import BasePermission


class CategoryPermission(BasePermission):

    def has_permission(self, request, view):
        return view.action in ['list', 'retrieve'] or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return view.action in ['retrieve'] or request.user.is_superuser
