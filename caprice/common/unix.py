import pwd, grp
from caprice.core.logging import log


def _user_exists(name):
    try:
        pwd.getpwnam(name)
        return True
    except KeyError:
        return False


def _create_user(name):
    pass

def user(name):
    log.question("check if user '%s' exists" % name)
    if not _user_exists(name):
        log.action("user doesn't exists, create it")
        _create_user(name)
    else:
        log.ok("user exists, continue")

def _group_exists(name):
    try:
        grp.getgrnam(name)
        return True
    except KeyError:
        return False

def _create_group(name):
    pass

def group(name):
    log.question("check if group '%s' exists" % name)
    if not _group_exists(name):
        log.action("group doesn't exists, create it")
        _create_group(name)
    else:
        log.ok("group exists, continue")
