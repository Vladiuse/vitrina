from django import template
from django.template import loader
from django.utils.safestring import mark_safe

register = template.Library()


@register.tag
def comment_block(parser,token):
    return CommentBlock()

class CommentBlock(template.Node):
    TEMPLATE_PATH = 'product/tags/comment_block.html'

    def render(self, context):
        template = loader.get_template(self.TEMPLATE_PATH)
        content = {}
        output = template.render(content)
        return output