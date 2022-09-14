# tests.py
import pytest
import os

from app.data_capture import DataCapture
from app.utils.exceptions import OutOfRangeException



LONG_VALUE_LIST = [336, 903, 111, 420, 677, 759, 195, 208, 729, 999, 15, 20, 195, 488, 784, 488, 381, 694, 972, 943]


@pytest.fixture
def capture_scenario_1():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    return capture

@pytest.fixture
def capture_scenario_2():
    capture = DataCapture()
    for num in LONG_VALUE_LIST:
        capture.add(num)
    return capture


class TestDataCapture:
    def test_greater_scenario_1(self,capture_scenario_1):
        # Act
        stats = capture_scenario_1.build_stats() 

        # Assert
        assert stats.greater(4) == 2

    def test_less_scenario_1(self,capture_scenario_1):
        # Act
        stats = capture_scenario_1.build_stats() 

        # Assert
        assert stats.less(4) == 2

    def test_between_scenario_1(self, capture_scenario_1):
        # Act
        stats = capture_scenario_1.build_stats() 

        # Assert
        assert stats.between(3,6) == 4


    def test_greater_scenario_2(self,capture_scenario_2):
        # Act
        stats = capture_scenario_2.build_stats() 

        # Assert
        assert stats.greater(420) == 11

    def test_less_scenario_2(self,capture_scenario_2):
        # Act
        stats = capture_scenario_2.build_stats() 

        # Assert
        assert stats.less(208) == 5

    def test_between_scenario_2(self, capture_scenario_2):
        # Act
        stats = capture_scenario_2.build_stats() 

        # Assert
        assert stats.between(111,694) == 11

    def test_greater_scenario_negative_number(self,capture_scenario_1):
        # Act
        stats = capture_scenario_1.build_stats() 

        # Assert
        try:
            stats.greater(-20)
            assert False
        except OutOfRangeException:
            assert True

    def test_greater_scenario_big_number(self,capture_scenario_1):
        # Act
        stats = capture_scenario_1.build_stats() 

        # Assert
        try:
            stats.less(921821)
            assert False
        except OutOfRangeException:
            assert True


    def test_between_scenario_same_boundaries(self,capture_scenario_2):
        # Act
        stats = capture_scenario_2.build_stats() 

        # Assert
        assert stats.between(488,488) == 2

    def test_between_scenario_boundaries_inverted(self,capture_scenario_2):
        # Act
        stats = capture_scenario_2.build_stats() 

        # Assert
        assert stats.between(694,111) == 11

    def test_less_scenario_string_value(self,capture_scenario_1):
        # Act
        stats = capture_scenario_1.build_stats() 

        # Assert
        try:
            stats.less('921821')
            assert False
        except Exception:
            assert True