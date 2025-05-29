;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "mypackagesV3"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("graphicx" "") ("amsmath" "") ("amsfonts" "") ("amsthm" "") ("amssymb" "") ("setspace" "") ("framed" "") ("mathtools" "") ("tikz" "") ("mlmodern" "") ("esdiff" "thinc") ("nicefrac" "") ("float" "") ("caption" "") ("xcolor" "") ("environ" "") ("tcolorbox" "")))
   (TeX-run-style-hooks
    "graphicx"
    "amsmath"
    "amsfonts"
    "amsthm"
    "amssymb"
    "setspace"
    "framed"
    "mathtools"
    "tikz"
    "mlmodern"
    "esdiff"
    "nicefrac"
    "float"
    "caption"
    "xcolor"
    "environ"
    "tcolorbox")
   (TeX-add-symbols
    '("rmkb" "Text")
    '("rmk" "Text")
    '("ex" "Text")
    '("pf" "Text")
    '("fact" "Text")
    '("clmp" "Text" "Text" "Text")
    '("clm" "Text" "Text")
    '("propp" "Text" "Text")
    '("prop" "Text")
    '("corp" "Text" "Text" "Text")
    '("cor" "Text")
    '("lemp" "Text" "Text" "Text")
    '("lem" "Text" "Text")
    '("thmr" "Text" "Text" "Text")
    '("thm" "Text" "Text")
    '("defnr" "Text" "Text" "Text")
    '("defn" "Text" "Text")
    '("circled" 1)
    "mybar")
   (LaTeX-add-environments
    "lempf"
    "corpf"
    "proppf"
    "clmpf"
    "example"
    "remark")
   (LaTeX-add-xcolor-definecolors
    "lightpink"
    "pinkishpurple"
    "lightpurple"
    "superblue"
    "lightblue")
   (LaTeX-add-tcolorbox-tcbuselibraries
    "theorems,skins,breakable"))
 :latex)

