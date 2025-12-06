from conan import ConanFile
from conan.tools.cmake import CMakeDeps, CMakeToolchain


class MyProjectConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def configure(self):
        # Use header-only mode for fmt
        self.options["fmt"].header_only = True

    def generate(self):
        # Generate CMake files - handles everything automatically
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def requirements(self):
        self.requires("fmt/12.0.0")
        self.requires("magic_enum/0.9.7")
        self.requires("spdlog/1.16.0")
        self.requires("gtest/1.17.0")
        self.requires("protobuf/6.32.1")
