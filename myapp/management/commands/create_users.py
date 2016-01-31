from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User, Permission, Group

class Command(BaseCommand):
    help = 'Create users & group, and Set permission'

    def handle(self, *args, **options):
        # すでにユーザが存在している場合は実行しない
        try:
            User.objects.get(username='no-perm')
            self.stdout.write(self.style.SUCCESS('Needless re-run'))
            return
        except User.DoesNotExist:
            # ユーザーが存在しない場合も正常系なので、処理続行
            pass

        # パーミッションなしのユーザ
        User.objects.create_user('no-perm', 'no-perm@example.com', 'no-permpassword')
        # この時点で、"no-perm"ユーザが"auth_user"テーブルに保存されている

        # パーミッションありのユーザ
        perm = User.objects.create_user('perm', 'perm@example.com', 'permpassword')
        permission = Permission.objects.get(codename='can_view')
        perm.user_permissions.add(permission)
        # この時点で、パーミッションが"auth_user_user_permissions"テーブルに保存されている

        # グループに対してパーミッションがあるユーザ
        # まずグループを作る
        group = Group.objects.create(name='viewable_users')
        # グループにパーミッションを割当
        group.permissions.add(permission)
        # この時点で、"auth_group_permissions"テーブルに保存されている
        # 続いてユーザを作る
        group_user = User.objects.create_user('group', 'group@example.com', 'grouppassword')
        # ユーザをグループに割り当て
        group_user.groups.add(group)
        # この時点で、"auth_user_groups"テーブルに保存されている
        
        self.stdout.write(self.style.SUCCESS('Complete'))