# Django Permissions & Groups Setup

This document provides an overview of how permissions and groups are configured and utilized in this Django project.

## Permissions in Django

Django’s permission system allows you to control access to specific actions on models or views. Each model automatically gets the following permissions:

- `add_<modelname>`
- `change_<modelname>`
- `delete_<modelname>`
- `view_<modelname>`

### Custom Permissions

To add custom permissions to a model:

```python
class MyModel(models.Model):
    ...

    class Meta:
        permissions = [
            ("can_approve", "Can approve item"),
        ]
```

After defining custom permissions, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Assigning Permissions to Users

You can assign permissions to individual users in the Django admin or via code:

```python
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model

user = get_user_model().objects.get(username='john')
permission = Permission.objects.get(codename='can_approve')
user.user_permissions.add(permission)
```

### Checking Permissions

```python
if request.user.has_perm('app_label.can_approve'):
    # allow access
```

## Groups in Django

Groups are a way to assign permissions to multiple users at once.

### Creating a Group

You can create a group in the Django admin or with code:

```python
from django.contrib.auth.models import Group, Permission

group, created = Group.objects.get_or_create(name='Editors')
permission = Permission.objects.get(codename='change_article')
group.permissions.add(permission)
```

### Assigning Users to a Group

```python
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

user = get_user_model().objects.get(username='john')
group = Group.objects.get(name='Editors')
user.groups.add(group)
```

### Checking Group Permissions

Users inherit the permissions of the groups they belong to.

```python
if request.user.has_perm('app_label.change_article'):
    # allowed because of group membership
```

## Testing Permissions

You can test user permissions in the Django shell:

```bash
python manage.py shell
```

```python
user = User.objects.get(username='john')
user.get_all_permissions()
user.has_perm('app_label.change_article')
```

## Best Practices

- Use groups to manage roles (e.g., Admins, Editors, Viewers).
- Define meaningful custom permissions for complex workflows.
- Always use `has_perm()` for checking permissions before accessing protected views or actions.
- Use Django's `@permission_required` decorator to protect views.

```python
from django.contrib.auth.decorators import permission_required

@permission_required('app_label.can_approve', raise_exception=True)
def approve_view(request):
    ...
```

## Summary

| Feature     | Purpose                                       |
| ----------- | --------------------------------------------- |
| Permissions | Fine-grained access control                   |
| Groups      | Role-based permission management              |
| Admin UI    | Manage permissions and groups easily          |
| Code APIs   | Assign and check permissions programmatically |

## Resources

- [https://docs.djangoproject.com/en/stable/topics/auth/default/#permissions-and-authorization](https://docs.djangoproject.com/en/stable/topics/auth/default/#permissions-and-authorization)
- [https://docs.djangoproject.com/en/stable/topics/auth/default/#groups](https://docs.djangoproject.com/en/stable/topics/auth/default/#groups)
