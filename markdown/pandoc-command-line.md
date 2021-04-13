---
title: pandoc command line
author: X_Mingest
authorLink: http://xm.tsohlac.online
date: 2020-08-24 16:57:50
---

# pandoc

```shell
pandoc -V mainfont="Microsoft YaHei" -V fontsize="16pt" -s --toc -M title=need example.md -o example.html # HTML use pandoc

pandoc -V mainfont="Microsoft YaHei" -V fontsize="16pt" -s --toc -c pandoc.css -M title=need -A footer.html example.md -o example.html # HTML with table of contents, CSS, and custom footer:

pandoc --pdf-engine=xelatex -V mainfont="Microsoft YaHei Mono" -V fontsize="16pt" example.md -o example.pdf # From markdown to PDF

pandoc -s example.tex -o example.text # From LaTeX to markdown

pandoc -s -t rst --toc example.md -o example.text # reStructuredText

pandoc -s example.md -o example.rtf # Rich text format (RTF)

pandoc -t beamer SLIDES -o example.pdf # Beamer slide show

pandoc -s -t docbook example.md -o example.db # DocBook XML

pandoc -s -t man pandoc.1.md -o example.1 # Man page

pandoc -s -t context example.md -o example.tex # ConTeXt

pandoc -s -r html http://www.gnu.org/software/make/ -o example.text # Converting a web page to markdown

pandoc -N --template=template.tex --variable mainfont="Palatino" --variable sansfont="Helvetica" --variable monofont="Menlo" --variable fontsize=12pt --variable version=2.0 example.md --pdf-engine=xelatex --toc -o example.pdf # PDF with numbered sections and a custom LaTeX header

pandoc example.md -o example.ipynb # ipynb (Jupyter notebook)

# HTML slide shows
pandoc -s --mathml -i -t dzslides SLIDES -o examplea.html
pandoc -s --webtex -i -t slidy SLIDES -o exampleb.html
pandoc -s --mathjax -i -t revealjs SLIDES -o exampled.html

# TeX math in HTML
pandoc math.text -s -o mathDefault.html
pandoc math.text -s --mathml  -o mathMathML.html
pandoc math.text -s --webtex  -o mathWebTeX.html
pandoc math.text -s --mathjax -o mathMathJax.html
pandoc math.text -s --katex   -o mathKaTeX.html

# Syntax highlighting of delimited code blocks
pandoc code.text -s --highlight-style pygments -o examplea.html
pandoc code.text -s --highlight-style kate -o exampleb.html
pandoc code.text -s --highlight-style monochrome -o examplec.html
pandoc code.text -s --highlight-style espresso -o exampled.html
pandoc code.text -s --highlight-style haddock -o examplee.html
pandoc code.text -s --highlight-style tango -o examplef.html
pandoc code.text -s --highlight-style zenburn -o exampleg.html

# GNU Texinfo, converted to info and HTML formats
pandoc example.md -s -o example.texi
makeinfo --no-validate --force example.texi -o example.info
makeinfo --no-validate --force example.texi --html -o example

# OpenDocument XML
pandoc example.md -s -t opendocument -o example.xml

# ODT (OpenDocument Text, readable by OpenOffice)
pandoc example.md -o example.odt

# MediaWiki markup
pandoc -s -t mediawiki --toc example.md -o example.wiki

# EPUB ebook
pandoc example.md -o MANUAL.epub

# Markdown citations
pandoc -s --bibliography biblio.bib --filter pandoc-citeproc CITATIONS -o examplea.html
pandoc -s --bibliography biblio.json --filter pandoc-citeproc --csl chicago-fullnote-bibliography.csl CITATIONS -o exampleb.html
pandoc -s --bibliography biblio.yaml --filter pandoc-citeproc --csl ieee.csl CITATIONS -t man -o examplec.1

# Textile writer
pandoc -s example.md -t textile -o example.textile

# Textile reader
pandoc -s example.textile -f textile -t html -o example.html

# Org-mode
pandoc -s example.md -o example.org

# AsciiDoc
pandoc -s example.md -t asciidoc -o example.txt

# Word docx
pandoc -s example.md -o example.docx

# LaTeX math to docx
pandoc -s math.tex -o example.docx

# DocBook to markdown
pandoc -f docbook -t markdown -s howto.xml -o example.text

# MediaWiki to html5
pandoc -f mediawiki -t html5 -s haskell.wiki -o example.html

# Custom writer
pandoc -t sample.lua example.text -o example.html

# Docx with a reference docx
pandoc --reference-doc twocolumns.docx -o UsersGuide.docx example.md

# Docx to markdown, including math
pandoc -s example.docx -t markdown -o example.md

# EPUB to plain text
pandoc MANUAL.epub -t plain -o example.text

# Using a template to produce a table from structured data
pandoc fishwatch.yaml -t rst --template fishtable.rst -o fish.rst
```
