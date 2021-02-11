{% from "macros.md" import section_elements %}
---
title: {{ info.first_name }} {{ info.last_name }}
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
{%- if section.subsection %}
### {{ section.name }}
{%- else %}
## {{ section.name }}
{%- endif %}
{{ section_elements(section) }}
{%- endfor %}
