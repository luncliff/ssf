# $env:CXX=clang-cl
# $env:CC=clang-cl
# meson setup   "build-x86-windows" --prefix "$(pwd)/install" --default-library shared --buildtype debug --warnlevel 3
# meson install -C "build-x86-windows"
# meson test    -C "build-x86-windows"

project('ssf', 'cpp', version: '0.1.3', meson_version: '>=0.55.0')
project_description = 'Simple Socket Functions'

public_headers = [
  'src/socket.hpp'
]
source_files = [
  'src/socket.cpp'
]
test_files = [
  'src/socket_test.cpp',
]

# https://mesonbuild.com/Reference-manual.html
compiler =  meson.get_compiler('cpp')

dep1 = compiler.find_library('kernel32', required: true)
dep2 = compiler.find_library('ws2_32', required: true)
dep3 = compiler.find_library('mswsock', required: true)

lib1 = library('ssf', 
    sources: [ source_files ],
    include_directories: join_paths('.', 'src'),
    dependencies: [ dep1, dep2, dep3 ],
    install: true,
    install_dir: get_option('libdir')
)

exe1 = executable('ssf_test', 
    sources: [ test_files ],
    include_directories: join_paths('.', 'src'),
    link_with: [ lib1 ],
    install: true,
    install_dir: get_option('bindir')
)

test('test 1', exe1)

# see https://mesonbuild.com/Installing.html
install_headers(public_headers, subdir : 'ssf')
install_data(
  sources: [ 'readme.md', 'LICENSE' ],
  install_dir: join_paths(get_option('infodir'), meson.project_name())
)
