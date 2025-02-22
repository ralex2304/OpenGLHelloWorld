# Build

## Dependencies

- `conan`
- `cmake`
- `make`
- `g++` or `clang`

### Managed by conan

- `GLFW`
- `GLAD`
- `OpenGL`

## Preparation

Specify env var `CONAN_WAYLAND=1` for GLFW Wayland build (GLFW works fine with XWayland too).

```
conan install . --build=missing
cmake --preset conan-release
```

## Build

```
cmake --build --preset conan-release
```

