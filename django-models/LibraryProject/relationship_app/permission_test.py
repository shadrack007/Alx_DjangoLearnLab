from django.contrib.auth import get_user_model

User = get_user_model()

def is_admin(user):
    user = User.objects.get(username=user)

    if user.profile.role == 'Admin':
        return True
    return False

def is_member(user):
    user = User.objects.get(username=user)
    if user.profile.role == 'Member':
        return True
    return False


def is_librarian(user):
    user = User.objects.get(username=user)
    if user.profile.role == 'Librarian':
        return True
    return False