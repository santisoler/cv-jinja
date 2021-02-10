---
title: {{ info.name }}
margin-left: 25mm
margin-right: 25mm
margin-top: 30mm
margin-bottom: 30mm
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
    {% if item.coadvisor %}_Advisor_: {{ item.advisor }}{% endif %}
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
