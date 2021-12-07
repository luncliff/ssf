#
# https://docs.conan.io/en/latest/creating_packages/getting_started.html
# https://spdx.org/licenses/
#
from conans import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake
from conan.tools.layout import cmake_layout


class SsfConan(ConanFile):
    name = "ssf"
    version = "1.0.2"
    description = "Simple Socket Functions"
    url = "https://github.com/luncliff/ssf"
    license = "CC-BY-4.0"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}

    generators = ["cmake_find_package", "cmake_paths"]
    # requires = [
    #     "catch2/2.13.0"
    # ]
    default_options = {"shared": True}

    exports_sources = [
        "readme.md", "LICENSE",  # for CPack
        "CMakeLists.txt",
        "src/socket.hpp", "src/socket.cpp", "src/socket_test.cpp",
    ]

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.shared = True

    def layout(self):
        cmake_layout(self)

    def generate(self):
        toolchain = CMakeToolchain(self)
        toolchain.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["ssf"]
