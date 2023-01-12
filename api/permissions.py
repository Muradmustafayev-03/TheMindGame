from rest_framework import permissions


def is_owner(request, obj):
    # Instance must have an attribute named `user`.
    return obj.user == request.user


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to access it.
    Assumes the model instance has a `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        return is_owner(request, obj)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has a `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return is_owner(request, obj)


class DefaultPermissions(permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly):
    """
    Allows everyone to see the content.
    Allows authenticated users to create objects.
    Allows owners of an object to edit or delete it.
    """
