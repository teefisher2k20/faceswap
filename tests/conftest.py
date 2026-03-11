""" Pytest configuration and environment setup to ensure CPU
and Torch defaults. """
import os

# Configure environment for tests
if "FACESWAP_BACKEND" not in os.environ:
    # Default to CPU for tests to avoid hardware dependency issues
    os.environ["FACESWAP_BACKEND"] = "cpu"

if "KERAS_BACKEND" not in os.environ:
    import importlib.util
    # Auto-detect backend for Keras
    if (importlib.util.find_spec("torch") and
            not importlib.util.find_spec("tensorflow")):
        os.environ["KERAS_BACKEND"] = "torch"
