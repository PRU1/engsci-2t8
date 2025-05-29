;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("tufte-handout" "")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("mypackagesv3" "") ("tikz" "") ("pgfplots" "") ("listings" "") ("qtree" "") ("forest" "") ("listofitems" "") ("contour" "outline") ("xcolor" "" "dvipsnames")))
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (TeX-run-style-hooks
    "latex2e"
    "tufte-handout"
    "tufte-handout10"
    "mypackagesv3"
    "tikz"
    "pgfplots"
    "listings"
    "qtree"
    "forest"
    "listofitems"
    "contour"
    "xcolor")
   (TeX-add-symbols
    '("code" 1)
    "nstyle"
    "NI"
    "NO"
    "yshift"
    "agr")
   (LaTeX-add-labels
    "fig:bigoh")
   (LaTeX-add-xcolor-definecolors
    "myred"
    "myblue"
    "mygreen"
    "myorange"
    "mydarkred"
    "mydarkblue"
    "mydarkgreen"
    "light-gray"
    "codegreen"
    "codegray"
    "backcolour")
   (LaTeX-add-listings-lstdefinestyles
    "mystyle"))
 :latex)

