from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow the owner of an object to perform any action.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the authenticated user is the owner of the object.
        return obj.user == request.user
