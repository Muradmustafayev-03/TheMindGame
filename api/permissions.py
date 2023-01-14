from rest_framework import permissions


def is_owner(request, obj):
    # Instance must have an attribute named `user`.
    return obj.user == request.user


def is_same_user(request, user):
    print(user, request.user)
    return user == request.user


def is_admin(request):
    return bool(request.user and request.user.is_staff)


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
    Safe methods are allowed for any requests.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return is_owner(request, obj)


class ProfilesPermissions(permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly):
    """
    Allows everyone to see the content.
    Allows authenticated users to create objects.
    Allows owners of an object to edit or delete it.
    """


class UsersPermissions(permissions.BasePermission):
    """
    Allows admin users to see the content.
    Allows everyone to create new objects.
    Allows owners of an object to retrieve,
    update and destroy this object.
    """

    def has_permission(self, request, view):
        return request.method != 'GET' or is_admin(request)

    def has_object_permission(self, request, view, obj):
        if is_same_user(request, obj):
            return True
        return request.method in permissions.SAFE_METHODS and is_admin(request)
