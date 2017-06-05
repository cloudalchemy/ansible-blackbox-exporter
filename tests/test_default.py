from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(File):
    present = [
        "/opt/blackbox_exporter",
        "/opt/blackbox_exporter/dist",
        "/opt/blackbox_exporter/current",
        "/var/log/blackbox_exporter"
    ]
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists


def test_files(File):
    present = [
        "/etc/blackbox_exporter.yml"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file


def test_service(Service):
    present = [
        "blackbox_exporter"
    ]
    if present:
        for service in present:
            s = Service(service)
            assert s.is_enabled


def test_socket(Socket):
    present = [
        "tcp://0.0.0.0:9115"
    ]
    for socket in present:
        s = Socket(socket)
        assert s.is_listening
