# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from src.shared._menu import Resource, to_menu, to_menu_item


@pytest.fixture
def resource():
    return Resource(name="Panel", url="https://panel.holoviz.org")


def test_to_menu_item(resource):
    # When
    item = to_menu_item(resource)
    # Then
    assert item == '<li><a href="https://panel.holoviz.org">Panel</a></li>'


def test_to_menu(resource):
    resources = [resource]
    # When
    item = to_menu(resources).replace("\n", "")
    # Then
    assert '<li><a href="https://panel.holoviz.org">Panel</a></li' in item
