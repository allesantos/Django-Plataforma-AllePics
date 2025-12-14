from django import template

register = template.Library()

@register.filter
def add_label_class(label_html, css_class):
    """Adiciona uma classe CSS a uma string de label_tag HTML (tag <label>)."""
    # Verifica se a classe já existe e adiciona
    if 'class="' in label_html:
        return label_html.replace('class="', f'class="{css_class} ', 1)
    
    # Se não houver atributo class, insere ele na tag <label>
    return label_html.replace('<label', f'<label class="{css_class}"', 1)