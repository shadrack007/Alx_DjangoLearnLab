from rest_framework.permissions import BasePermission

class ReadOnly(BasePermission):
    """
    A permission class that allows read-only access to unauthenticated users.
    """
    def has_permission(self, request):
        if request.user and request.user.is_authenticated:
            return True
        # Allow read-only methods for unauthenticated users 
        return request.method in ['GET', 'HEAD', 'OPTIONS']
