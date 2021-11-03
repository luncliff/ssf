cmake_minimum_required(VERSION 3.10)
project(ssf VERSION 1.0.1 LANGUAGES CXX)
message(STATUS "Using system: ${CMAKE_SYSTEM_VERSION}")

include(GNUInstallDirs)
if(WIN32)
    # see "C:/Program Files (x86)/Windows Kits/10/Redist/..."
    # 10.0.18362.0, 10.0.19041.0, 10.0.20348.0 ...
    set(CMAKE_INSTALL_DEBUG_LIBRARIES true)
    set(CMAKE_INSTALL_UCRT_LIBRARIES true)
    include(InstallRequiredSystemLibraries)
    message(VERBOSE " Target: ${CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION}")
endif()
find_package(Threads REQUIRED)


list(APPEND hdrs socket.hpp)

add_library(ssf
    ${hdrs}
    socket.cpp
)

set_target_properties(ssf
PROPERTIES
    CXX_STANDARD 14
    PUBLIC_HEADER "${hdrs}"
)

target_include_directories(ssf
PUBLIC
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

message(STATUS "compiler: ${CMAKE_CXX_COMPILER_ID}")
if(CMAKE_CXX_COMPILER_ID MATCHES GNU)
    target_compile_options(ssf
    PUBLIC
        -std=gnu++14
    )
    target_link_libraries(ssf
    PUBLIC
        stdc++
    )
elseif(CMAKE_CXX_COMPILER_ID MATCHES Clang)
    if(WIN32)
        # clang-cl is not considered for now ...
    else()
        target_compile_options(ssf
        PUBLIC
            -stdlib=libc++
        )
    endif()
elseif(CMAKE_CXX_COMPILER_ID MATCHES MSVC)
    target_compile_options(ssf
    PRIVATE
        /W4 /Zc:__cplusplus
    )
endif()

if(WIN32)
    set_target_properties(ssf
    PROPERTIES
        WINDOWS_EXPORT_ALL_SYMBOLS True
    )
    target_link_libraries(ssf
    PUBLIC
        ws2_32
    )
elseif(APPLE)
    target_link_libraries(ssf
    PUBLIC
        c++
    )
endif()

install(TARGETS ssf
        EXPORT  ${PROJECT_NAME}-config
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/${PROJECT_NAME}
)
install(EXPORT  ${PROJECT_NAME}-config
        DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/${PROJECT_NAME} # share/ssf
)

include(CMakePackageConfigHelpers)
set(VERSION_FILE_PATH   ${CMAKE_BINARY_DIR}/cmake/${PROJECT_NAME}-config-version.cmake)
write_basic_package_version_file(${VERSION_FILE_PATH}
    VERSION         ${PROJECT_VERSION}
    COMPATIBILITY   SameMajorVersion
)
install(FILES       ${VERSION_FILE_PATH} 
        DESTINATION ${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME}
)

set(CPACK_PACKAGE_NAME ${PROJECT_NAME})
set(CPACK_PACKAGE_VERSION ${PROJECT_VERSION})
set(CPACK_PACKAGE_VENDOR "luncliff@gmail.com")
set(CPACK_PACKAGE_DESCRIPTION "https://github.com/luncliff/ssf")
set(CPACK_RESOURCE_FILE_README ${PROJECT_SOURCE_DIR}/readme.md)
set(CPACK_GENERATOR "ZIP")
include(CPack)
