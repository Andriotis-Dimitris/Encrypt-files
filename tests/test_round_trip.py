import os
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ransomware import generate_key, encrypt_files
from decrypt import decrypt_files


def test_round_trip(tmp_path):
    """Encrypt and decrypt a file and verify its contents."""
    original_content = b"Hello, world!"
    test_file = tmp_path / "sample.txt"
    test_file.write_bytes(original_content)

    # Run encryption in the temporary directory
    cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        key = generate_key()
        encrypt_files([test_file.name], key)

        # Ensure content changed after encryption
        assert test_file.read_bytes() != original_content

        # Decrypt using the stored key
        decrypt_files([test_file.name], key)

        # Verify content matches original
        assert test_file.read_bytes() == original_content
    finally:
        os.chdir(cwd)
