import pytest

from transform.dedupe import dedupe
from transform.normalize import normalize


@pytest.mark.parametrize("fn", [dedupe, normalize])
def test_stubs_not_implemented_yet(fn):
    with pytest.raises(NotImplementedError):
        fn([])
