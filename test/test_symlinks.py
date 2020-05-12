#
# Copyright (C) 2020  Red Hat, Inc.
# Author(s):  David Cantrell <dcantrell@redhat.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import os
import unittest
import rpmfluff
from baseclass import TestRPMs, TestKoji, TestCompareRPMs, TestCompareKoji

script_source = '''#!/bin/sh
echo This is a script
'''

# Absolute symlink exists (OK)
class AbsoluteSymlinkExistsRPMs(TestRPMs):
    def setUp(self):
        TestRPMs.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        self.rpm.add_installed_symlink('usr/sbin/testscript', '/usr/bin/testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

class AbsoluteSymlinkExistsKoji(TestKoji):
    def setUp(self):
        TestKoji.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        self.rpm.add_installed_symlink('usr/sbin/testscript', '/usr/bin/testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

class AbsoluteSymlinkExistsCompareRPMs(TestCompareRPMs):
    def setUp(self):
        TestCompareRPMs.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        self.after_rpm.add_installed_symlink('usr/sbin/testscript', '/usr/bin/testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

class AbsoluteSymlinkExistsCompareKoji(TestCompareKoji):
    def setUp(self):
        TestCompareKoji.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        self.after_rpm.add_installed_symlink('usr/sbin/testscript', '/usr/bin/testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

# Relative symlink with ../ exists (OK)
class RelativeSymlinkExistsParentDirRPMs(TestRPMs):
    def setUp(self):
        TestRPMs.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        self.rpm.add_installed_symlink('usr/sbin/testscript', '../bin/testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

class RelativeSymlinkExistsParentDirKoji(TestKoji):
    def setUp(self):
        TestKoji.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        self.rpm.add_installed_symlink('usr/sbin/testscript', '../bin/testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

class RelativeSymlinkExistsParentDirCompareRPMs(TestCompareRPMs):
    def setUp(self):
        TestCompareRPMs.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        self.after_rpm.add_installed_symlink('usr/sbin/testscript', '../bin/testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

class RelativeSymlinkExistsParentDirCompareKoji(TestCompareKoji):
    def setUp(self):
        TestCompareKoji.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        self.after_rpm.add_installed_symlink('usr/sbin/testscript', '../bin/testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

# Relative symlink in current directory exists (OK)
class RelativeSymlinkExistsCurrentDirRPMs(TestRPMs):
    def setUp(self):
        TestRPMs.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        self.rpm.add_installed_symlink('usr/bin/anothertestscript', 'testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

class RelativeSymlinkExistsCurrentDirKoji(TestKoji):
    def setUp(self):
        TestKoji.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        self.rpm.add_installed_symlink('usr/bin/anothertestscript', 'testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

class RelativeSymlinkExistsCurrentDirCompareRPMs(TestCompareRPMs):
    def setUp(self):
        TestCompareRPMs.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        self.after_rpm.add_installed_symlink('usr/bin/anothertestscript', 'testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

class RelativeSymlinkExistsCurrentDirCompareKoji(TestCompareKoji):
    def setUp(self):
        TestCompareKoji.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        self.after_rpm.add_installed_symlink('usr/bin/anothertestscript', 'testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

# Symlink that exists spans subpackages (OK)
class SymlinkExistsMultiplePackagesRPMS(TestRPMs):
    def setUp(self):
        TestRPMs.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        subpackage = self.rpm.add_subpackage('symlinks')
        self.rpm.add_installed_symlink('usr/bin/anothertestscript', 'testscript', subpackageSuffix='symlinks')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

class SymlinkExistsMultiplePackagesKoji(TestKoji):
    def setUp(self):
        TestKoji.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        subpackage = self.rpm.add_subpackage('symlinks')
        self.rpm.add_installed_symlink('usr/bin/anothertestscript', 'testscript', subpackageSuffix='symlinks')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

class SymlinkExistsMultiplePackagesCompareRPMs(TestCompareRPMs):
    def setUp(self):
        TestCompareRPMs.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        subpackage = self.after_rpm.add_subpackage('symlinks')
        self.after_rpm.add_installed_symlink('usr/bin/anothertestscript', 'testscript', subpackageSuffix='symlinks')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

class SymlinkExistsMultiplePackagesCompareKoji(TestCompareKoji):
    def setUp(self):
        TestCompareKoji.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        subpackage = self.after_rpm.add_subpackage('symlinks')
        self.after_rpm.add_installed_symlink('usr/bin/anothertestscript', 'testscript', subpackageSuffix='symlinks')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'OK'
        self.waiver_auth = 'Not Waivable'

# Absolute symlink is dangling (VERIFY)
class AbsoluteSymlinkDangingRPMs(TestRPMs):
    def setUp(self):
        TestRPMs.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        self.rpm.add_installed_symlink('usr/sbin/testscript', '/usr/bin/anothertestscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'

class AbsoluteSymlinkDangingKoji(TestKoji):
    def setUp(self):
        TestRPMs.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        self.rpm.add_installed_symlink('usr/sbin/testscript', '/usr/bin/anothertestscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'

class AbsoluteSymlinkDangingCompareRPMs(TestCompareRPMs):
    def setUp(self):
        TestCompareRPMs.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        self.after_rpm.add_installed_symlink('usr/sbin/testscript', '/usr/bin/anothertestscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'

class AbsoluteSymlinkDangingCompareKoji(TestCompareKoji):
    def setUp(self):
        TestCompareKoji.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        self.after_rpm.add_installed_symlink('usr/sbin/testscript', '/usr/bin/anothertestscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'

# Relative symlink with ../ is dangling (VERIFY)
class RelativeSymlinkDanglingParentDirRPMs(TestRPMs):
    def setUp(self):
        TestRPMs.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        self.rpm.add_installed_symlink('usr/sbin/testscript', '../bin/anothertestscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'

class RelativeSymlinkDanglingParentDirKoji(TestKoji):
    def setUp(self):
        TestKoji.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        self.rpm.add_installed_symlink('usr/sbin/testscript', '../bin/anothertestscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'

class RelativeSymlinkDanglingParentDirRPMs(TestCompareRPMs):
    def setUp(self):
        TestCompareRPMs.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        self.after_rpm.add_installed_symlink('usr/sbin/testscript', '../bin/anothertestscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'

class RelativeSymlinkDanglingParentDirKoji(TestCompareKoji):
    def setUp(self):
        TestCompareKoji.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        self.after_rpm.add_installed_symlink('usr/sbin/testscript', '../bin/anothertestscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'

# Relative symlink in current directory is dangling (VERIFY)
class RelativeSymlinkDanglingCurrentDirRPMs(TestRPMs):
    def setUp(self):
        TestRPMs.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        self.rpm.add_installed_symlink('usr/bin/anothertestscript', 'originaltestscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'

class RelativeSymlinkDanglingCurrentDirKoji(TestKoji):
    def setUp(self):
        TestKoji.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        self.rpm.add_installed_symlink('usr/bin/anothertestscript', 'originaltestscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'

class RelativeSymlinkDanglingCurrentDirCompareRPMs(TestCompareRPMs):
    def setUp(self):
        TestCompareRPMs.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        self.after_rpm.add_installed_symlink('usr/bin/anothertestscript', 'originaltestscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'

class RelativeSymlinkDanglingCurrentDirCompareKoji(TestCompareKoji):
    def setUp(self):
        TestCompareKoji.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        self.after_rpm.add_installed_symlink('usr/bin/anothertestscript', 'originaltestscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'

# Too many symlink cycles (VERIFY)
# To trigger an ELOOP on symlink resolution, you need to have more
# than 40 levels of symlink redirection, per path_resolution(7).  I use 47
# levels here just to make sure.
class TooManySymlinkLevelsRPMs(TestRPMs):
    def setUp(self):
        TestRPMs.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        self.rpm.add_installed_symlink('usr/bin/bin', '.')
        self.rpm.add_installed_symlink('usr/bin/anothertestscript', 'bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'BAD'
        self.waiver_auth = 'Anyone'

class TooManySymlinkLevelsKoji(TestKoji):
    def setUp(self):
        TestKoji.setUp(self)

        # add file and symlink
        self.rpm.add_installed_file(installPath='usr/bin/testscript',
                                    sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                    mode="0755")
        self.rpm.add_installed_symlink('usr/bin/bin', '.')
        self.rpm.add_installed_symlink('usr/bin/anothertestscript', 'bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'BAD'
        self.waiver_auth = 'Anyone'

class TooManySymlinkLevelsCompareRPMs(TestCompareRPMs):
    def setUp(self):
        TestCompareRPMs.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        self.after_rpm.add_installed_symlink('usr/bin/bin', '.')
        self.after_rpm.add_installed_symlink('usr/bin/anothertestscript', 'bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'BAD'
        self.waiver_auth = 'Anyone'

class TooManySymlinkLevelsCompareKoji(TestCompareKoji):
    def setUp(self):
        TestCompareKoji.setUp(self)

        # add file and symlink
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                          sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                          mode="0755")
        self.after_rpm.add_installed_symlink('usr/bin/bin', '.')
        self.after_rpm.add_installed_symlink('usr/bin/anothertestscript', 'bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/bin/testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'BAD'
        self.waiver_auth = 'Anyone'

# Directory becomes a symlink (VERIFY)
class DirectoryBecomesSymlinkCompareRPMs(TestCompareRPMs):
    def setUp(self):
        TestCompareRPMs.setUp(self)

        # add directories and symlinks
        self.before_rpm.add_installed_directory('usr/share/testdirectory')
        self.before_rpm.add_installed_directory('usr/share/actualdirectory')
        self.after_rpm.add_installed_symlink('usr/share/testdirectory', 'actualdirectory')
        self.after_rpm.add_installed_directory('usr/share/actualdirectory')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'

class DirectoryBecomesSymlinkCompareKoji(TestCompareKoji):
    def setUp(self):
        TestCompareKoji.setUp(self)

        # add directories and symlinks
        self.before_rpm.add_installed_directory('usr/share/testdirectory')
        self.before_rpm.add_installed_directory('usr/share/actualdirectory')
        self.after_rpm.add_installed_symlink('usr/share/testdirectory', 'actualdirectory')
        self.after_rpm.add_installed_directory('usr/share/actualdirectory')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'

# Non-directory becomes a symlink (VERIFY)
class NonDirectoryBecomesSymlinkCompareRPMs(TestCompareRPMs):
    def setUp(self):
        TestCompareRPMs.setUp(self)

        # add files and symlinks
        self.before_rpm.add_installed_file(installPath='usr/bin/testscript',
                                           sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                           mode="0755")
        self.before_rpm.add_installed_file(installPath='usr/bin/anothertestscript',
                                           sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                           mode="0755")
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                           sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                           mode="0755")
        self.after_rpm.add_installed_symlink('usr/bin/anothertestscript', 'testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'

class NonDirectoryBecomesSymlinkCompareKoji(TestCompareKoji):
    def setUp(self):
        TestCompareKoji.setUp(self)

        # add files and symlinks
        self.before_rpm.add_installed_file(installPath='usr/bin/testscript',
                                           sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                           mode="0755")
        self.before_rpm.add_installed_file(installPath='usr/bin/anothertestscript',
                                           sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                           mode="0755")
        self.after_rpm.add_installed_file(installPath='usr/bin/testscript',
                                           sourceFile=rpmfluff.SourceFile('testscript.sh', script_source),
                                           mode="0755")
        self.after_rpm.add_installed_symlink('usr/bin/anothertestscript', 'testscript')

        self.inspection = 'symlinks'
        self.label = 'symlinks'
        self.result = 'VERIFY'
        self.waiver_auth = 'Anyone'