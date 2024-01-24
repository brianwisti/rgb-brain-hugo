#!/usr/bin/env python

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "../lib"))

from note_processor import main  # pylint: disable=C0413

if __name__ == "__main__":
    main()
