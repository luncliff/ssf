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
    default_options = {"shared": True}

    generators = "cmake_find_package"
    # requires = [
    #     "catch2/2.13.0"
    # ]

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
        if self.settings.os == "Windows":
            tc.variables["INSTALL_FOR_DEPLOY"] = "OFF"
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
        if self.settings.build_type == "RelWithDebInfo":  # -s build_type=RelWithDebInfo
            self.copy("ssf.pdb", dst="bin", keep_path=False)

    # https://docs.conan.io/en/latest/reference/conanfile/methods.html#package-info
    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.bindirs = ["bin"]
        self.cpp_info.defines = []
        self.cpp_info.cxxflags = []
        if self.options.shared == True:
            self.cpp_info.sharedlinkflags = []
        self.cpp_info.libs = ["ssf"]
