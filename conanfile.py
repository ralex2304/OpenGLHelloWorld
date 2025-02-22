from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout

def detect_display_server():
    import os

    if "CONAN_WAYLAND" in os.environ:
        return "wayland"

    return "x11"


class opengl_helloworldProject(ConanFile):
    name = "opengl_helloworld"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def configure(self):
        display_server = detect_display_server()

        if display_server == "wayland":
            self.output.info("Detected Wayland display server. Building GLFW for Wayland.")
            self.options["glfw"].with_x11     = False
            self.options["glfw"].with_wayland = True
        else:
            self.options["glfw"].with_x11     = True
            self.options["glfw"].with_wayland = False
 
    def requirements(self):
        self.requires("glfw/3.3.8")
        self.requires("glad/0.1.36")

    def layout(self):
        cmake_layout(self)
