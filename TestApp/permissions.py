from rest_framework.permissions import BasePermission

# UNSAFE_METHODS = ('POST', 'HEAD', 'OPTIONS')


class IsAuthenticatedExaminer(BasePermission):
    message = 'You need to be an Examiner to perform this action.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_examiner)


class IsAuthenticatedExaminee(BasePermission):
    message = 'You need to be an Examinee to perform this action.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_examinee)

        # return bool(
        #     request.method in UNSAFE_METHODS and user_perms or
        #     user_perms and request.user.has_profile()
        # )
