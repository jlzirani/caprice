import pwd


def _user_exists(name):
    try:
        pwd.getpwnam(name)
        return True
    except KeyError:
        return False


def _create_user(name):
    pass


def user(name):
    if not _user_exists(name):
        _create_user(name)
