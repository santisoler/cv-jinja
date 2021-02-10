---
title: {{ info.first_name }} {{ info.last_name }}
{%- if page_layout.margin_left %}
margin-left: {{ page_layout.margin_left }}
{%- endif %}
{%- if page_layout.margin_right %}
margin-right: {{ page_layout.margin_right }}
{%- endif %}
{%- if page_layout.margin_top %}
margin-top: {{ page_layout.margin_top }}
{%- endif %}
{%- if page_layout.margin_bottom %}
margin-bottom: {{ page_layout.margin_bottom }}
{%- endif %}
---

{% if "affiliation" in info %}

----
{% for affil in info.affiliation %}
>  {{ affil }}
>
{%- endfor %}

----
{% endif %}

{%- for section in sections -%}

{%+ if section.subsection %}
### {{ section.name }}
{%- else %}
## {{ section.name }}
{% endif %}

{%- if section.type == "education" %}
{%- if "items" in section %}
{% for item in section["items"] %}
{{ item.date }}
:   **{{ item.title }}**
    _{{ item.institution }}_

    {% if item.thesis %}_Thesis_: {{ item.thesis }}{% endif %}

    {% if item.advisor %}_Advisor_: {{ item.advisor }}{% endif %}
    {% if item.coadvisor %}_Co-advisor_: {{ item.coadvisor }}{% endif %}
{% endfor %}
{%- endif %}
{%- endif %}

{%- if section.type == "awards" %}
{%- if "items" in section %}
{% for item in section["items"] %}
{{ item.date }}
:   {{ item.title }}

    {{ item.extra }}
{% endfor %}
{%- endif %}
{%- endif %}

{%- if section.type == "teaching" %}
{%- if "items" in section %}
{% for item in section["items"] %}
{{ item.date }}
:   **{{ item.course }}**
    _{{ item.institution }}_

    {{ item.position }}

    {{ item.extra }}
{% endfor %}
{%- endif %}
{%- endif %}

{%- if section.type == "publication" %}
{%- if "items" in section %}
{% for item in section["items"] %}
{{ item.date }}
:   **{{ item.title }}**
    _{{ item.journal }}_

    {% if item.authors %}
    {{ item.authors }}
    {% endif %}

    {% if item.extra %}
    {{ item.extra }}
    {%- endif %}

    {% if item.doi %}
    doi: [{{ item.doi }}](https://doi.org/{{ item.doi }})
    {%- endif %}
{% endfor %}
{%- endif %}
{%- endif %}

{%- endfor %}
