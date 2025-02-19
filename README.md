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

```
conan install . --build=missing
cmake --preset conan-release
```

## Build

```
cmake --build --preset conan-release
```

