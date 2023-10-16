from rest_framework.permissions import BasePermission, SAFE_METHODS
    

class IsSuperuser(BasePermission):
    """
    The request is superuser, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_superuser
        )
    
    
class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author