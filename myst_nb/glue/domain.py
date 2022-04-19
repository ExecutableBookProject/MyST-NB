"""A domain to register in sphinx.

This is required for any directive/role names using `:`.
"""
from typing import List

from sphinx.domains import Domain

from .directives import (
    PasteAnyDirective,
    PasteFigureDirective,
    PasteMarkdownDirective,
    PasteMathDirective,
)
from .roles import PasteMarkdownRole, PasteRoleAny, PasteTextRole


class NbGlueDomain(Domain):
    """A sphinx domain for defining glue roles and directives."""

    name = "glue"
    label = "NotebookGlue"

    # data version, bump this when the format of self.data changes
    data_version = 1

    directives = {
        "": PasteAnyDirective,
        "any": PasteAnyDirective,
        "figure": PasteFigureDirective,
        "math": PasteMathDirective,
        "md": PasteMarkdownDirective,
    }
    roles = {
        "": PasteRoleAny(),
        "any": PasteRoleAny(),
        "text": PasteTextRole(),
        "md": PasteMarkdownRole(),
    }

    def merge_domaindata(self, docnames: List[str], otherdata: dict) -> None:
        pass
