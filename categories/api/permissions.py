from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    """ Permiso para que solo el staff pueda enviar datos o borrarlos"""
    def has_permission(self, request, view):
        if request.method == 'GET':   
            return True 
        else:
            return request.user.is_staff 