# https://docs.conan.io/en/latest/creating_packages/getting_started.html
from conans import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake
from conan.tools.layout import cmake_layout


class SsfConan(ConanFile):
    name = "ssf"
    version = "1.0.3"
    description = "Simple Socket Functions"
    url = "https://github.com/luncliff/ssf"
    license = "CC-BY-4.0"  # https://spdx.org/licenses/

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}

    generators = "cmake_find_package"
    # requires = [
    #     "catch2/2.13.0"
    # ]
    default_options = {"shared": True}

    exports_sources = [
        "readme.md", "LICENSE",  # for CPack
        "CMakeLists.txt",
        "src/socket.hpp", "src/socket.cpp", "src/socket_test.cpp",
    ]

    # https://docs.conan.io/en/latest/developing_packages/package_layout.html
    def layout(self):
        cmake_layout(self)

    # https://docs.conan.io/en/latest/reference/conanfile/tools/cmake/cmaketoolchain.html
    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["BUILD_TESTING"] = "ON"
        tc.generate()

    # https://docs.conan.io/en/latest/reference/build_helpers/cmake.html
    def build(self):
        cmake = CMake(self)
        if self.settings.os == "Windows":
            cmake.append_vcvars = True
        cmake.configure()
        cmake.build()

    def test(self):
        cmake = CMake(self)
        if self.settings.os == "Windows":
            cmake.append_vcvars = True
        cmake.test()

    def package(self):
        cmake = CMake(self)
        if self.settings.os == "Windows":
            cmake.append_vcvars = True
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["ssf"]
        self.cpp_info
