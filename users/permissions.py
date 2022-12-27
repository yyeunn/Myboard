from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
    # GET : anyone / PUT,PATCH : user who has the profile
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # SAFE_METHOD is like GET not affecting on the data
            return True
        return obj.user == request.user