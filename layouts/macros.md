<!-- Macro for including every element of the section -->
{%- macro section_elements(section) -%}
    {%- if "items" in section %}
        {%- if section.type == "education" %}
            {{ education(section) }}
        {%- elif section.type == "awards" %}
            {{ awards(section) }}
        {%- elif section.type == "teaching" %}
            {{ teaching(section) }}
        {%- elif section.type == "publication" %}
            {{ publication(section) }}
        {%- endif -%}
    {%- endif -%}
{%- endmacro -%}


<!-- Education -->
{%- macro education(section) -%}
{% for item in section["items"] %}
{{ item.date }}
:   **{{ item.title }}**
    _{{ item.institution }}_
    {%- if item.thesis %}

    _Thesis_: {{ item.thesis }}
    {%- endif %}
    {%- if item.advisor %}

    _Advisor_: {{ item.advisor }}
    {%- endif %}
    {%- if item.coadvisor %}
    _Co-advisor_: {{ item.coadvisor }}
    {%- endif %}
{% endfor %}
{%- endmacro -%}


<!-- Awards -->
{%- macro awards(section) -%}
{% for item in section["items"] %}
{{ item.date }}
:   {{ item.title }}
    {%- if item.extra %}

    {{ item.extra }}
    {%- endif %}
{% endfor %}
{%- endmacro -%}


<!-- Teaching -->
{%- macro teaching(section) -%}
{% for item in section["items"] %}
{{ item.date }}
:   **{{ item.course }}**
    _{{ item.institution }}_
    {%- if item.position %}

    {{ item.position }}
    {%- endif %}
    {%- if item.extra %}

    {{ item.extra }}
    {%- endif %}
{% endfor %}
{%- endmacro -%}


<!-- Publication -->
{%- macro publication(section) -%}
{% for item in section["items"] %}
{{ item.date }}
:   **{{ item.title }}**
    _{{ item.journal }}_
    {%- if item.authors %}

    {{ item.authors }}
    {%- endif %}
    {%- if item.extra %}

    {{ item.extra }}
    {%- endif %}
    {%- if item.doi %}

    doi: [{{ item.doi }}](https://doi.org/{{ item.doi }})
    {%- endif %}
{% endfor %}
{%- endmacro -%}
