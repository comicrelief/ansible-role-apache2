import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_apache2_is_installed(Package):
    apache = Package("apache2")
    assert apache.is_installed
    assert apache.version.startswith("2.4")


def test_apache2_running_and_enabled(Service):
    apache = Service("apache2")
    assert apache.is_running
    assert apache.is_enabled
