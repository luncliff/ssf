cmake_minimum_required(VERSION 3.10)

project(ssf VERSION 1.0 LANGUAGES CXX)

add_library(ssf
    socket.hpp
    socket.cpp
)

set_target_properties(ssf
PROPERTIES
    CXX_STANDARD 14
    # PUBLIC_HEADER socket.hpp
)

# target_include_directories(ssf
# PUBLIC
#     $<INSTALL_INTERFACE:${CMAKE_INSTALL_PREFIX}/include>
# )

if(${CMAKE_CXX_COMPILER_ID} MATCHES GNU)
    target_compile_options(ssf
    PUBLIC
        -std=gnu++14
    )
elseif(${CMAKE_CXX_COMPILER_ID} MATCHES Clang)
    if(WIN32)
        # clang-cl is not considered for now ...
    else()
        target_compile_options(ssf
        PUBLIC
            -stdlib=libc++
        )
    endif()
elseif(${CMAKE_CXX_COMPILER_ID} MATCHES MSVC)
    target_compile_options(ssf
    PUBLIC
        /W4
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
endif()


install(FILES   socket.hpp
        DESTINATION ${CMAKE_INSTALL_PREFIX}/include/${PROJECT_NAME}
)

install(TARGETS         ssf
        EXPORT          ${PROJECT_NAME}-config
        RUNTIME  DESTINATION ${CMAKE_INSTALL_PREFIX}/bin
        LIBRARY  DESTINATION ${CMAKE_INSTALL_PREFIX}/lib
        ARCHIVE  DESTINATION ${CMAKE_INSTALL_PREFIX}/lib
        INCLUDES DESTINATION ${CMAKE_INSTALL_PREFIX}/include
)

install(EXPORT      ${PROJECT_NAME}-config
        DESTINATION ${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME}
)

include(CMakePackageConfigHelpers)
set(VERSION_FILE_PATH   ${CMAKE_BINARY_DIR}/cmake/${PROJECT_NAME}-config-version.cmake)
write_basic_package_version_file(${VERSION_FILE_PATH}
    VERSION             ${PROJECT_VERSION}
    COMPATIBILITY       SameMajorVersion
)

install(FILES           ${VERSION_FILE_PATH} 
        DESTINATION     ${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME}
)
