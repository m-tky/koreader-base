cmake_minimum_required(VERSION 3.17.5)
project(luasec LANGUAGES C)

find_package(PkgConfig REQUIRED)
pkg_check_modules(LuaJIT luajit REQUIRED IMPORTED_TARGET)

# LuaSec is compiled with the bundled LibreSSL headers in the staging prefix.
# Link it to the matching bundled library rather than a host OpenSSL selected
# by pkg-config: their legacy stack APIs are not ABI-compatible.
if(BUILD_SHARED_LIBS)
    set(LIBRESSL_LIBRARY_SUFFIX ${CMAKE_SHARED_LIBRARY_SUFFIX})
else()
    set(LIBRESSL_LIBRARY_SUFFIX ${CMAKE_STATIC_LIBRARY_SUFFIX})
endif()

if(BUILD_SHARED_LIBS)
    add_library(ssl MODULE)
else()
    add_library(ssl STATIC)
endif()
set_target_properties(ssl PROPERTIES C_VISIBILITY_PRESET hidden PREFIX "")
target_compile_definitions(ssl PRIVATE -DWITH_LUASOCKET)
target_include_directories(ssl PRIVATE ${CMAKE_INSTALL_PREFIX}/include)
target_link_libraries(ssl PRIVATE
    ${CMAKE_INSTALL_PREFIX}/lib/libluasocket.a
    ${CMAKE_INSTALL_PREFIX}/lib/libssl${LIBRESSL_LIBRARY_SUFFIX}
    ${CMAKE_INSTALL_PREFIX}/lib/libcrypto${LIBRESSL_LIBRARY_SUFFIX}
    PkgConfig::LuaJIT
)
target_sources(ssl PRIVATE
    src/options.c
    src/x509.c
    src/context.c
    src/ssl.c
    src/config.c
    src/ec.c
)
