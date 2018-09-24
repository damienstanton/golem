from os import path

from golem.core.common import get_golem_path
from golem.docker.environment import DockerEnvironment


class ShellTaskEnvironment(DockerEnvironment):
    DOCKER_IMAGE = "golemfactory/base"
    DOCKER_TAG = "1.2"
    ENV_ID = "Shell"
    APP_DIR = path.join(get_golem_path(), 'apps', 'shell')
    SCRIPT_NAME = "docker_shelltask.py"
    SHORT_DESCRIPTION = "Shell task"
