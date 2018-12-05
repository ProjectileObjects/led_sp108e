import pytest
import commands


def test_frame():
    with pytest.raises(ValueError):
        # data too long
        commands.frame(4, b'\x01\x02\x03\x04')

    assert b'\x38\x00\x00\x00\x7f\x83' == commands.frame(0x7f, None)
    assert b'\x38\x80\x00\x00\x0f\x83' == commands.frame(0xf, b'\x80')
    assert b'\x38\x01\x20\x44\x01\x83' == commands.frame(1, b'\x01\x20\x44')


def test_speed():
    assert b'\x38\x64\x00\x00\x03\x83' == commands.speed(100)


def test_get_device_name():
    assert b'\x38\x00\x00\x00\x77\x83' == commands.get_device_name()


def test_check_device():
    with pytest.raises(AttributeError):
        commands.check_device(None)

    assert b'\x38\x30\x20\x10\xd5\x83' == commands.check_device(0x102030)