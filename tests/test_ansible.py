import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/group01.yml")["ansible_facts"]


def test_prometheus_user(User, Group, AnsibleDefaults):
    assert User(AnsibleDefaults["prometheus_user"]).exists
    assert Group(AnsibleDefaults["prometheus_group"]).exists
    assert User(AnsibleDefaults["prometheus_user"]).group == AnsibleDefaults["prometheus_group"]


def test_prometheus_conf(File, User, Group, AnsibleDefaults):
    conf_path = File(AnsibleDefaults["prometheus_conf_path"])
    assert conf_path.exists
    assert conf_path.is_directory
    assert conf_path.user == AnsibleDefaults["prometheus_user"]
    assert conf_path.group == AnsibleDefaults["prometheus_group"]


def test_prometheus_data(File, User, Group, AnsibleDefaults):
    conf_path = File(AnsibleDefaults["prometheus_data_path"])
    assert conf_path.exists
    assert conf_path.is_directory
    assert conf_path.user == AnsibleDefaults["prometheus_user"]
    assert conf_path.group == AnsibleDefaults["prometheus_group"]


def test_prometheus_log(File, User, Group, AnsibleDefaults):
    conf_path = File(AnsibleDefaults["prometheus_log_path"])
    assert conf_path.exists
    assert conf_path.is_directory
    assert conf_path.user == AnsibleDefaults["prometheus_user"]
    assert conf_path.group == AnsibleDefaults["prometheus_group"]


def test_prometheus_bin(File, Command, AnsibleDefaults):
    am = File(AnsibleDefaults["prometheus_bin_path"] + "/prometheus")
    am_link = File("/usr/bin/prometheus")
    assert am.exists
    assert am.is_file
    assert am.user == AnsibleDefaults["prometheus_user"]
    assert am.group == AnsibleDefaults["prometheus_group"]
    assert am_link.exists
    assert am_link.is_file
    assert am_link.user == "root"
    assert am_link.group == "root"
    am_version = Command("prometheus --version")
    assert am_version.rc is 0
    assert "prometheus, version " + AnsibleDefaults["prometheus_version"] in am_version.stdout


def test_prometheus_service(File, Service, Socket, AnsibleVars):
    port = AnsibleVars["prometheus_port"]
    assert File("/lib/systemd/system/prometheus.service").exists
    assert Service("prometheus").is_enabled
    assert Service("prometheus").is_running
    assert Socket("tcp://:::" + str(port)).is_listening
