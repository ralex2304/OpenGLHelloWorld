from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout

class opengl_helloworldProject(ConanFile):
    name = "opengl_helloworld"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("glfw/3.3.8")
        self.requires("glad/0.1.36")

    def layout(self):
        cmake_layout(self)
