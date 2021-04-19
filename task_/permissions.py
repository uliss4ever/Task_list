from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and obj.public == True:
            return True
        else:
            return obj.user == request.user
# для выполнения п.2 ТЗ

# class IsCommentPost(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method == "POST":
#             return True
#         return False
