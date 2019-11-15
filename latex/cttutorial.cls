% LaTeX2e class file `cttutorial.cls' for providing consistent
% typesetting of tutorials and their solutions.
%
% Created by Colin Turner, 6 October 2003
%
% Put something like the following into your LaTeX file:
%
% \documentclass{cttutorial}
% \begin{document}
% \modulenumber{EEE001}
% \moduletitle{Engineering Calculations}
% \modulelecturer{Dr. Turner}
% \tutorialnumber{2}
% \tutorialtitle{Please attempt these problems \emph{before} your tutorial in week 3}
% ...
% \end{document}

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cttutorial}[2003/09/06 Colin Turner tutorial solutions class]
\RequirePackage{fancyhdr}
%\RequirePackage{times}
\LoadClass[a4paper]{ctexam}


% Information about the module
\def\modulenumber#1{\def\themodulenumber{#1}}
\def\moduletitle#1{\def\themoduletitle{#1}}
\def\modulelecturer#1{\def\themodulelecturer{#1}}
\def\tutorialword#1{\def\thetutorialword{#1}}
\def\tutorialnumber#1{\def\thetutorialnumber{#1}}
\def\tutorialextra#1{\def\thetutorialextra{#1}}
\def\tutorialtitle#1{\def\thetutorialtitle{#1}}

% Defaults
\tutorialword{Tutorial}

% Set up the page formatting appropriately
\pagestyle{fancyplain}
\addtolength{\headwidth}{\marginparsep}
\addtolength{\headwidth}{\marginparwidth}
\lhead{\themodulenumber\ (\themoduletitle)}
\rhead{\themodulelecturer}
\lfoot{\thetutorialword\ \thetutorialnumber\ \thetutorialextra}
\rfoot{\thepage}
\cfoot{}
\def\headrulewidth{0.4 pt}
\def\footrulewidth{0.4 pt}

% Solutions
\newcommand\solutions{
\newpage
\chead{\sc{\thetutorialword\ \thetutorialnumber\ \thetutorialextra\ Solutions}}
\lhead{\sc{\themodulenumber}}
\rhead{\sc{\themodulelecturer}}
\lfoot{}
\rfoot{}
\cfoot{\thepage\ / \pageref{LastPage}}
%\setlength{\footrulewidth}{1 pt}
%\setlength{\headrulewidth}{1 pt}
\boxedpoints
\pointsinmargin
%\pointname{}
\renewcommand{\baselinestretch}{1.0}

\begin{center}
\begin{Large}
\sc{Sketch Solutions}
\end{Large}

Approach your tutor or lecturer if you do not understand any part of the 
solutions for further explanation. Marks are shown boxed in the left margin.
\end{center}
}



