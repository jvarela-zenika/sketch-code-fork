from __future__ import print_function
from __future__ import absolute_import

from .SamplerUtils import *

TEXT_PLACE_HOLDER = "[]"

class Node:

    def __init__(self, key, parent_node, content_holder):
        self.key = key
        self.parent = parent_node
        self.children = []
        self.content_holder = content_holder

    def add_child(self, child):
        self.children.append(child)

    def show(self):
        for child in self.children:
            child.show()

    def rendering_function(self, key, value):
        if key.find("button") != -1:
            value = value.replace(TEXT_PLACE_HOLDER, SamplerUtils.get_random_text())
        elif key.find("title") != -1:
            value = value.replace(TEXT_PLACE_HOLDER, SamplerUtils.get_random_text(length_text=5, space_number=0))
        elif key.find("text") != -1:
            value = value.replace(TEXT_PLACE_HOLDER,
                                  SamplerUtils.get_random_text(length_text=56, space_number=7, with_upper_case=False))
        return value

    def render(self, mapping, rendering_function=None):

        value = self.get_node_value(mapping)
        if value is None:
            self = None
            return None

        content = ""
        for child in self.children:
            placeholder = child.render(mapping, self.rendering_function)
            if placeholder is None:
                self = None
                return
            else:
                content += placeholder
            value = value.replace(self.get_content_holder(child.key), content)

        if rendering_function is not None:
            value = self.rendering_function(self.key, value)

        return value

    def get_node_value(self, mapping):
        value = None
        if self.parent.key == "header":
            if self.key == "image":
                value = mapping.get("logo", None)

            if self.key == "link":
                value = mapping.get("header-link", None)
        if value is None:
            value = mapping.get(self.key, None)
        return value

    def get_content_holder(self, node):

        specializer = ''
        if node.key == "header":
            specializer = 'h'
        if node.key == "footer":
            specializer = 'f'

        content_length = len(self.content_holder)
        return self.content_holder[0:content_length/2] + specializer + self.content_holder[content_length:]
