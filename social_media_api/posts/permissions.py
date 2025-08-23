from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only owners can edit/delete, others can only view.
    """

    def has_object_permission(self, request, view, obj):
        # Read only permiSsIons for safe methods GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
