%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Do not edit this header!!!
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesClass{uebung}[2008/11/12 v0.00001455745]
\PassOptionsToClass{a4paper,11pt}{article}
\LoadClass{article}

\RequirePackage{ngerman}
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage[margin=23mm,top=40mm,bottom=30mm]{geometry}
\RequirePackage{graphicx}
\RequirePackage{fancyhdr,lastpage}
\RequirePackage{amsmath,amsfonts,amssymb,amsthm}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% These commands are used to generate the header
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\lecture}[1]{%
  \def\uebcslecture{#1}%
}

\newcommand{\semester}[1]{%
  \def\uebcssemester{#1}%
}

\newcommand{\student}[3]{%
  \def\uebcsstdname{#1}%
  \def\uebcsstdid{#2}%
  \def\uebcsstdgroup{#3}%
}

\newcommand{\assignment}[1]{%
  \def\uebcsnr{#1}%
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% The different texts are defined for English and German
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\DeclareOption{german}
{
% i18n: deutsch
\def\uebcsassignment{\"Ubung}
\def\uebcsexercise{Aufgabe}
\def\uebcsgroup{Gruppe}
\def\uebcsmatnr{Mat.-Nr.}
}

\DeclareOption{english}
{
% i18n: english
\def\uebcsassignment{Assignment}
\def\uebcsexercise{Exercise}
\def\uebcsgroup{Group}
\def\uebcsmatnr{Student ID number}
}

\ProcessOptions

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This environment sets the spaces around the exercises
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newenvironment{exercise}[1]{{%
\vspace{3ex}%
\large%
\noindent\textbf{\uebcsexercise\ \uebcsnr.#1}\\[1ex]%
}}{}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% define header
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\pagestyle{fancy}

\lhead{\uebcslecture\ (\uebcssemester)\\\uebcsgroup\ \uebcsstdgroup}
\rhead{\uebcsstdname\\\uebcsstdid}
\cfoot{\thepage~/~\pageref{LastPage}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% predefined commands
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\renewcommand{\O}{\mathcal{O}}
\newcommand{\sort}{\mathrm{sort}}
\newcommand{\scan}{\mathrm{scan}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%