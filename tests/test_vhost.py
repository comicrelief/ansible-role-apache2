import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_original_vhost_no_longer_exists(File):
    original_vhost = File("/etc/apache2/sites-enabled/000-default.conf")
    assert not original_vhost.exists
    assert not original_vhost.is_symlink
    assert not original_vhost.linked_to == \
        "/etc/apache2/sites-available/000-default.conf"


def test_default_vhost_exists(File):
    default_vhost = File("/etc/apache2/sites-enabled/001-default.conf")
    assert default_vhost.exists
    assert default_vhost.is_symlink
    assert default_vhost.linked_to == \
        "/etc/apache2/sites-available/001-default.conf"


def test_vhost_exists(File):
    test_vhost = File("/etc/apache2/sites-enabled/test.conf")
    assert test_vhost.exists
    assert test_vhost.is_symlink
    assert test_vhost.linked_to == \
        "/etc/apache2/sites-available/test.conf"
    content = test_vhost.content
    assert "<VirtualHost *:80>" in content
    assert "ErrorLog /var/log/apache2/test-error.log" in content
    assert "CustomLog /var/log/apache2/test-access.log combined-elb" in content


def test_default_vhost_returns_403_without_basic_auth(Command):
    test_vhost = Command(
        "curl -s -o /dev/null -w '%{http_code}' 'http://localhost/'"
    )
    assert test_vhost.stdout == \
        "403"
