# mkdir build
# cd build
# conan install ..
# conan build ..

from conans import ConanFile, CMake, tools

class DLibConan(ConanFile):
    name = "dlib"
    version = "19.21"
    license = "Boost Software License"
    url = "https://github.com/davisking/dlib/"
    description = "A toolkit for making real world machine learning and data analysis applications in C++"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "iso_cpp_only" : [True, False], 
        "enable_gif" : [True, False], 
        "enable_png" : [True, False], 
        "enable_jpeg" : [True, False], 
        "no_gui_support" : [True, False], 
        "enable_stack_trace" : [True, False], 
        "link_with_sqlite" : [True, False], 
        "enable_asserts" : [True, False], 
        "enable_cuda" : [True, False], 
        "enable_blas" : [True, False], 
        "enable_lapack" : [True, False], 
        "enable_sse2" : [True, False], 
        "enable_sse4" : [True, False], 
        "enable_avx" : [True, False], 
        "enable_mkl_fft": [True, False], 
        "shared": [True, False], 
        "fPIC": [True, False]
    }
    default_options = {
        "iso_cpp_only": False,
        "enable_gif": False,
        "enable_png": False,
        "enable_jpeg": False,
        "no_gui_support": True,
        "enable_stack_trace": False,
        "link_with_sqlite": False,
        "enable_asserts": False,
        "enable_cuda": False,
        "enable_blas": False,
        "enable_lapack": False,
        "enable_avx": False,
        "enable_sse4": False,
        "enable_sse2": True,
        "enable_mkl_fft": False,
        "shared": False,
        "fPIC": True
    }
    generators = "cmake"        

    def build(self):
        cmake = CMake(self)
        defs = {
            "CMAKE_INSTALL_PREFIX": "../bin",
            "DLIB_ISO_CPP_ONLY": self.options.iso_cpp_only,
            "DLIB_GIF_SUPPORT": self.options.enable_gif,
            "DLIB_PNG_SUPPORT": self.options.enable_png,
            "DLIB_JPEG_SUPPORT": self.options.enable_jpeg,
            "DLIB_NO_GUI_SUPPORT": self.options.no_gui_support,
            "DLIB_ENABLE_STACK_TRACE": self.options.enable_stack_trace,
            "DLIB_LINK_WITH_SQLITE3": self.options.link_with_sqlite,
            "DLIB_ENABLE_ASSERTS": self.options.enable_asserts,
            "DLIB_USE_CUDA": self.options.enable_cuda,
            "DLIB_USE_BLAS": self.options.enable_blas,
            "DLIB_USE_LAPACK": self.options.enable_lapack,
            "USE_AVX_INSTRUCTIONS": self.options.enable_avx,
            "USE_SSE4_INSTRUCTIONS": self.options.enable_sse4,
            "USE_SSE2_INSTRUCTIONS": self.options.enable_sse2,
            "DLIB_USE_MKL_FFT": self.options.enable_mkl_fft,            
            "BUILD_SHARED_LIBS": self.options.shared
        }
        cmake.configure(source_folder="dlib", defs=defs)
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*", dst="include/", src="bin/include")
        self.copy("*", dst="lib/", src="bin/lib")

    def package_info(self):
        if self.settings.os == "Windows":
            self.cpp_info.libs = ["dlib19.21.99_release_64bit_msvc1926.lib"]
        elif self.settings.os == "Linux":
            self.cpp_info.libs = ["libdlib.a"]
        elif self.settings.os == "Macos":
            self.cpp_info.libs = ["libdlib.a"]
