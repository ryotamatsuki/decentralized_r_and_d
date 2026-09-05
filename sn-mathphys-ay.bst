%% This is file `sn-mathphys-ay.bst'
%% Compatible with bibtex version 0.99d.
%%
%% Sorting entries is done by name and year fields!
%%
%% You are free to use this style file as you see fit, provided 
%% that you do not make changes to the file. 
%%
%% It may be distributed under the terms of the LaTeX Project Public
%% License, as described in lppl.txt in the base LaTeX distribution.
%% Either version 1.0 or, at your option, any later version.
%%
%% LIMITATIONS:
%% If you are getting error like
%% "Sorry---you've exceeded BibTeX's number of string global-variables"
%% that means you are using to old bibtex version. You should download latest version 0.99d. 
%% (One of the binaries location is minimals.contextgarden.net/current/bin/common/)

FUNCTION {identify.mathphys.version}
{ % Put identifying string in the .blg file
  "sn-mathphys-ay.bst"
  " [2024/07/19 v1.1 bibliography style]"
  * top$
}

ENTRY
  { address
    author
    booktitle
    bnumber
    chapter
    doi
    edition
    editor
    howpublished
    institution
    isbn
    journal
    key
    keywords
    month
    note
    number
    organization
    pages
    publisher
    school
    series
    title
    type
    url
    volume
    year
  }
  { label }
  { sort.label sort.year sort.name }

INTEGERS { output.state before.all mid.sentence after.sentence after.block }
INTEGERS { nameptr namesleft numnames }
INTEGERS { multiresult }

STRINGS  { s t u v w }
STRINGS  { longest.label }
STRINGS  { label extra.label sort.key }
STRINGS  { sort.label sort.year sort.name }

MACRO {jan} {"January"}
MACRO {feb} {"February"}
MACRO {mar} {"March"}
MACRO {apr} {"April"}
MACRO {may} {"May"}
MACRO {jun} {"June"}
MACRO {jul} {"July"}
MACRO {aug} {"August"}
MACRO {sep} {"September"}
MACRO {oct} {"October"}
MACRO {nov} {"November"}
MACRO {dec} {"December"}
