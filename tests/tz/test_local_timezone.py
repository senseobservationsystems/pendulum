import os
import sys

import pytest

from pendulum.tz.local_timezone import _get_unix_timezone
from pendulum.tz.local_timezone import _get_windows_timezone


@pytest.mark.skipif(sys.platform == 'win32',
                    reason='Test only available for UNIX systems')
def test_unix_symlink():
    # A ZONE setting in the target path of a symbolic linked localtime,
    # f ex systemd distributions
    local_path = os.path.join(os.path.split(__file__)[0], '..')
    tz = _get_unix_timezone(
        _root=os.path.join(local_path, 'fixtures', 'tz', 'symlink')
    )

    assert tz.name == 'Europe/Paris'


@pytest.mark.skipif(sys.platform != 'win32',
                    reason='Test only available for Windows')
def test_unix_symlink():
    timezone = _get_windows_timezone()

    assert timezone is not None