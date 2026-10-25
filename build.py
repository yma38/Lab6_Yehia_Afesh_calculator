from pybuilder.core import init, use_plugin


use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")


name = "calculator_Yehia_Afesh"
version = "1.0"
default_task = "publish"


@init
def initialize(project):
    project.set_property(
        "dir_source_main_python",
        "src/main/python",
    )

    project.set_property(
        "dir_source_unittest_python",
        "tests/unittest/calculator_Yehia_Afesh",
    )

    project.set_property(
        "unittest_module_glob",
        "test_*",
    )

    project.set_property(
        "dir_target",
        "target",
    )