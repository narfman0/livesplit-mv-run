import os
import unittest

from livesplit_mv_run.splits_parser import parse


class TestSplitsParser(unittest.TestCase):
    def test_parse(self):
        src_path = os.path.join("tests", "fixtures", "splits1.lss")
        src_file = parse(src_path)
        breakpoint()
        self.assertEqual("Game Name 1", src_file.game_name)
