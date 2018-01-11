from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_files(File):
    dirs = [
        "/opt/blackbox_exporter",
        "/var/log/blackbox_exporter"
    ]
    files = [
        "/etc/blackbox_exporter.yml",
        "/opt/blackbox_exporter/blackbox_exporter"
    ]
    for directory in dirs:
        d = File(directory)
        assert d.is_directory
        assert d.exists
    for file in files:
        f = File(file)
        assert f.exists
        assert f.is_file


def test_service(Service):
    s = Service("blackbox_exporter")
    assert s.is_running
    assert s.is_enabled


def test_socket(Socket):
    s = Socket("tcp://127.0.0.1:9115")
    assert s.is_listening
