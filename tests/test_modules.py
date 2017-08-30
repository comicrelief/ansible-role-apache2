import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_remoteip_symlink_exists(File):
    remoteip = File("/etc/apache2/mods-enabled/remoteip.load")
    assert remoteip.exists
    assert remoteip.is_symlink
    assert remoteip.linked_to == \
        "/etc/apache2/mods-available/remoteip.load"
    assert remoteip.content_string == \
        "LoadModule remoteip_module /usr/lib/apache2/modules/mod_remoteip.so\n"


def test_remoteip_is_enabled(Command):
    remoteip = Command("a2enmod remoteip")
    assert remoteip.stdout == \
        "Module remoteip already enabled\n"


def test_rewrite_symlink_exists(File):
    rewrite = File("/etc/apache2/mods-enabled/rewrite.load")
    assert rewrite.exists
    assert rewrite.is_symlink
    assert rewrite.linked_to == \
        "/etc/apache2/mods-available/rewrite.load"
    assert rewrite.content_string == \
        "LoadModule rewrite_module /usr/lib/apache2/modules/mod_rewrite.so\n"


def test_rewrite_is_enabled(Command):
    rewrite = Command("a2enmod rewrite")
    assert rewrite.stdout == \
        "Module rewrite already enabled\n"
