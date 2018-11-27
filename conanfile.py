from conans import ConanFile, CMake, tools


class Secp256k1Conan(ConanFile):
    name = "secp256k1"
    version = "1.0"
    license = "BSD"
    channel = "stable"
    author = "Erik Aronesty <erik@getvida.io>"
    url = "https://github.com/earonesty/conan-secp256k1.git"
    description = "Optimized C library for EC operations on curve secp256k1"
    topics = ("bitcoin", "cryptography", "elliptic curve")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake_paths", "cmake"
    build_policy = "missing"
    requires = ( )

    def source(self):
        self.run("git clone git@github.com:vidaid/conan-secp256k1.git")

    def test(self):
        cmake = CMake(self)
        cmake.test()

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="secp256k1")
        cmake.build()
        cmake.test()

        # Explicit way:
        # self.run('cmake %s/src %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="secp256k1")
        self.copy("*secp256k1.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["secp256k1"]
