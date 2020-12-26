"""Provides the MENU html string appended to all templates"""
from typing import List

from src.shared import config

from .models import Resource

COLLAPSED_SVG_ICON = f"""
<svg style="stroke: {config.color_primary}" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" slot="collapsed-icon">
            <path d="M15.2222 1H2.77778C1.79594 1 1 1.79594 1 2.77778V15.2222C1 16.2041 1.79594 17 2.77778 17H15.2222C16.2041 17 17 16.2041 17 15.2222V2.77778C17 1.79594 16.2041 1 15.2222 1Z" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M9 5.44446V12.5556" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M5.44446 9H12.5556" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
""".replace(
    "\n", ""
)

EXPANDED_SVG_ICON = f"""
<svg style="stroke: {config.color_primary}" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" slot="expanded-icon">
    <path d="M15.2222 1H2.77778C1.79594 1 1 1.79594 1 2.77778V15.2222C1 16.2041 1.79594 17 2.77778 17H15.2222C16.2041 17 17 16.2041 17 15.2222V2.77778C17 1.79594 16.2041 1 15.2222 1Z" stroke-linecap="round" stroke-linejoin="round"></path>
    <path d="M5.44446 9H12.5556" stroke-linecap="round" stroke-linejoin="round"></path>
</svg>
""".replace(
    "\n", ""
)

MENU_PRE = f"""
<fast-accordion id="menu">
    <fast-accordion-item slot="item" expanded>
        <h3 slot="heading">Main</h3>{ COLLAPSED_SVG_ICON }{ EXPANDED_SVG_ICON }
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="gallery">Gallery</a></li>
        </ul>
    </fast-accordion-item>
    <fast-accordion-item slot="item" expanded>
        <h3 slot="heading" >Apps</h3>{COLLAPSED_SVG_ICON}{EXPANDED_SVG_ICON}
        <ul>
"""

MENU_POST = """
        </ul>
    </fast-accordion-item>
</fast-accordion>
"""


def to_menu_item(resource: Resource) -> str:
    """Converts a Resource to a Menuitem"""
    return f'<li><a href="{resource.url}">{resource.name}</a></li>'


def to_menu(resources: List[Resource], menu_prefix=MENU_PRE, menu_postfix=MENU_POST) -> str:
    """Converts a list of Resources to a Menu

    Args:
        resources (List[Resource]): The list of Resources
        menu_prefix ([type], optional): A string prepended to the list of MenuItems.
            Defaults to MENU_PRE.
        menu_postfix ([type], optional): A string appended to the list of MenuItems.
            Defaults to MENU_POST.

    Returns:
        [str]: The Menu as a HTML string
    """
    skip = ["Gallery", "Home"]
    resources = [resource for resource in resources if not resource.name in skip]
    resources = sorted(resources, key=lambda x: x.name)
    menu_items = [to_menu_item(resource) for resource in resources]
    menu = menu_prefix + "\n".join(menu_items) + menu_postfix
    return menu


MENU = to_menu(config.applications.values()).replace("\n", "")
