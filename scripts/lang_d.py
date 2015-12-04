import os
import sys
from scripts.command import CommandSession

def check_compiler_availability(compiler_executable):
    if not os.path.exists(compiler_executable):
        print('missing compiler executable specified in the config: ' + compiler_executable)
        sys.exit(1)

def build_d_sources_with_dmd(source_dir, output_dir, builder_config):
    compiler_executable = os.path.join(builder_config['path'], 'rdmd.exe')
    check_compiler_availability(compiler_executable)

    build_command = [
        compiler_executable,
        '--build-only',
        '-O',
        '-inline',
        '-release',
        '-m64',
        '-boundscheck=off',
        '-od"' + output_dir + '"',
        '-of"' + os.path.join(output_dir, 'benchmark.exe"'),
        '-I' + 'scripts/common/lang_d',
        os.path.join(source_dir, 'main.d')
    ]
    session = CommandSession()
    session.add_command(*build_command)
    session.run()

def build_d_sources_with_gdc(source_dir, output_dir, builder_config):
    compiler_executable = os.path.join(builder_config['path'], 'gdc.exe')
    check_compiler_availability(compiler_executable)

    d_source_files = [os.path.join(source_dir, f) for f in os.listdir(source_dir) if f.endswith('.d')]
    d_source_files.append('scripts/common/lang_d/common.d')

    build_command = [
        compiler_executable,
        '-O3',
        '-m64',
        '-fno-bounds-check',
        '-frelease',
        '-o"' + os.path.join(output_dir, 'benchmark.exe"'),
        '-I' + 'scripts/common/lang_d',
    ]
    build_command.extend(d_source_files)
    session = CommandSession()
    session.add_command(*build_command)
    session.run()

def build_d_sources_with_ldc(source_dir, output_dir, builder_config):
    compiler_executable = os.path.join(builder_config['path'], 'ldc2.exe')
    check_compiler_availability(compiler_executable)

    d_source_files = [os.path.join(source_dir, f) for f in os.listdir(source_dir) if f.endswith('.d')]
    d_source_files.append('scripts/common/lang_d/common.d')

    build_command = [
        compiler_executable,
        '-O3',
        '-m64',
        '-release',
        '-od"' + output_dir + '"',
        '-of"' + os.path.join(output_dir, 'benchmark.exe"'),
        '-I' + 'scripts/common/lang_d'
    ]
    build_command.extend(d_source_files)
    session = CommandSession()
    session.add_command(*build_command)
    session.run()
