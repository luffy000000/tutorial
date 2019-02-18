from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    自定义权限只允许对象的所有者编辑它
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # 只有该snippit的所有者才允许写权限
        return obj.owner == request.user
        