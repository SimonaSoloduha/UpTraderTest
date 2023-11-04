from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    def build_nested_dict_to_parent(self):
        result = {}
        children = self.children.all()
        if children:
            childs = {}
            for child in children:
                childs[child.title] = {'id': child.id,
                                       'menu': None}
            result = childs
        elem = self

        while elem.parent:
            children = elem.parent.children.all()
            childs = {}
            for child in children:
                if child == elem:
                    childs[elem.title] = {'id': child.id,
                                          'menu': result}
                else:
                    childs[child.title] = {'id': child.id,
                                           'menu': None}
            result = childs
            elem = elem.parent

        result = {elem.title: {'id': elem.id,
                               'menu': result}}
        return result
