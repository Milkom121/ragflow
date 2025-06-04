"""
Root-level conftest to adjust sys.path for test package imports.
"""
import os
import sys

# Make SDK Python test directory part of system path for package-relative imports
ROOT_DIR = os.path.dirname(__file__)
TEST_ROOT = os.path.join(ROOT_DIR, 'sdk', 'python', 'test')
sys.path.insert(0, os.path.abspath(TEST_ROOT))

# Monkey-patch default SourceFileLoader to strip null bytes from source to avoid null byte syntax errors
try:
    import importlib._bootstrap_external as _bootstrap_ext
    _bootstrap_ext.SourceFileLoader.get_source = (
        lambda self, path: open(path, 'rb').read().replace(b"\x00", b"").decode('utf-8', errors='replace')
    )
except ImportError:
    pass

# Monkey-patch pytest assertion rewriting to avoid null bytes issues in rewritten modules
try:
    import _pytest.assertion.rewrite as _rewrite_mod

    def _rewrite_test_noop(path, config):
        # Read source without rewriting asserts and remove null bytes
        data = path.read_bytes().replace(b'\x00', b'')
        source = data.decode('utf-8', 'replace')
        code_obj = compile(source, str(path), 'exec')
        return None, code_obj

    _rewrite_mod._rewrite_test = _rewrite_test_noop
    # Disable writing of pyc files in pytest assertion rewrite to avoid caching errors
    _rewrite_mod._write_pyc = lambda *args, **kwargs: None
    _rewrite_mod._write_pyc_fp = lambda *args, **kwargs: None
    # Also remove AssertionRewritingHook from sys.meta_path to disable assertion rewriting loader
    try:
        from _pytest.assertion.rewrite import AssertionRewritingHook
        sys.meta_path[:] = [h for h in sys.meta_path if not isinstance(h, AssertionRewritingHook)]
    except ImportError:
        pass
except ImportError:
    pass

def pytest_configure(config):
    # Unregister pytest assertion rewriting plugin to avoid null byte issues
    try:
        from _pytest.assertion.rewrite import AssertionRewritingHook
        pm = config.pluginmanager
        for plugin in list(pm.get_plugins()):
            if isinstance(plugin, AssertionRewritingHook):
                pm.unregister(plugin)
    except ImportError:
        pass