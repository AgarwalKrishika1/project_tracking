from rest_framework.permissions import IsAuthenticated, BasePermission


class AdminPermission(IsAuthenticated):

    def has_permission(self, request, view):
        print(request.user)
        if request.user.is_superuser:
            print('has_permission true')
            return True

        print('has_permission false')
        return False


class ProjectManagerPermission(AdminPermission):

    def has_permission(self, request, view):
        default_permission = super().has_permission(request=request, view=view)
        if default_permission or request.user.userprofile.role == 'project_manager':
            return True
        return False


class SrDeveloperPermission(AdminPermission):

    def has_permission(self, request, view):
        default_permission = super().has_permission(request=request, view=view)
        if default_permission or request.user.userprofile.role == 'sr_developer':
            return True
        return False


class JrDeveloperPermission(AdminPermission):

    def has_permission(self, request, view):
        default_permission = super().has_permission(request=request, view=view)
        if default_permission or request.user.userprofile.role == 'jr_developer':
            return True
        return False


class IsAuthenticatedOrPostOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow unauthenticated access for POST requests
        if request.method == 'POST':
            return True
        # Authenticate other requests using IsAuthenticated
        return IsAuthenticated().has_permission(request, view)

