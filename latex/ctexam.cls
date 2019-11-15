% exam.cls
%
% A LaTeX2e document class for preparing exams.

%%% Copyright (c) 2000 Philip S. Hirschhorn
%
% This program may be distributed and/or modified under the
% conditions of the LaTeX Project Public License, either version 1.2
% of this license or (at your option) any later version.
% The latest version of this license is in
%   http://www.latex-project.org/lppl.txt
% and version 1.2 or later is part of all distributions of LaTeX 
% version 1999/12/01 or later.
%
% This program consists of the files exam.cls and examdoc.tex

% The user documentation for exam.cls is in the file examdoc.tex.


%%% Philip Hirschhorn
%%% Department of Mathematics
%%% Wellesley College
%%% Wellesley, MA 02481
%%% psh@poincare.wellesley.edu
%%% psh@math.mit.edu

% The newest version of this documentclass should always be available
% from my web page: http://www-math.mit.edu/~psh/


\def\fileversion{2.01}
\def\filedate{2000/10/10}

%--------------------------------------------------------------------
%--------------------------------------------------------------------
%
% The only change from version 2.0 to version 2.01 is that this
% documentclass (and its accompanying documentation) is now
% explicitly distributed under the LaTeX Project Public License.
%
%---------------------------------------------------------------------
%---------------------------------------------------------------------
% PLEASE DO NOT MAKE ANY CHANGES TO THIS FILE!
% 
% If you wish to make changes to this file, rename this file
% to something other than exam.cls BEFORE YOU MAKE THE CHANGES!
% 
% If there's some feature that you'd like that this file doesn't
% provide, tell me about it.
% 
%
%
%
%
% Thanks to:
%
% Piet van Oostrum, from whose excellent ``fancyheadings.sty'' we
% shamelessly stole most of the code for setting the headers and
% footers.
%
% Mate Wierdl <mw@wierdlmpc.msci.memphis.edu>, who contributed the
% code so that if the number of points is ``1'', then the default
% value of \pointname will print ``1 point'' instead of ``1 points''.
%
% Tom Brikowski <brikowi@utdallas.edu>, who contributed the code for
% making the number of points and number of questions available as
% macros (as well as the idea of putting the number of points in a 
% box, instead of in parentheses).  (I changed his code to make this
% all optional, so if there are errors there, it's my fault and not
% his.)
%
%--------------------------------------------------------------------
%--------------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}

\ProvidesClass{ctexam}[\filedate\space Version \fileversion\space by
  Philip Hirschhorn]

\RequirePackage{ifthen}

\DeclareOption*{%
  \PassOptionsToClass{\CurrentOption}{article}%
}
\ProcessOptions
\LoadClass{article}




%                         *****************
%                         ** PAGE LAYOUT **
%                         *****************


%\setlength{\textwidth}{6.5in}
%\setlength{\oddsidemargin}{0pt}
%\setlength{\evensidemargin}{0pt}


%\setlength{\headheight}{15pt}
%\setlength{\headsep}{15pt}
%\setlength{\topmargin}{0in}
%\addtolength{\topmargin}{-\headheight}
%\addtolength{\topmargin}{-\headsep}
%\setlength{\textheight}{8.8in}
%\setlength{\footskip}{29pt}
%\setlength{\marginparwidth}{.5in}
%\setlength{\marginparsep}{5pt}

%--------------------------------------------------------------------

%                          ****************
%                          ** EXTRAWIDTH **
%                          ****************

\newlength\@extrawidth

% We put the argument of \extrawidth into a length so that it will
% work correctly even if it's negative:

\def\extrawidth#1{%
  \@extrawidth=#1
  \advance \textwidth by \@extrawidth
  \divide\@extrawidth by 2
  \advance\oddsidemargin by -\@extrawidth
  \advance\evensidemargin by -\@extrawidth
}





%--------------------------------------------------------------------
%--------------------------------------------------------------------

%                \numpages, \iflastpage, and \oddeven
%     Also: \numpoints, \numquestions, \numparts, and \numsubparts

% Make the number of pages available as the macro \numpages,
% the number of points as \numpoints,
% the number of questions as \numquestions,
% the number of parts as \numparts, and
% the number of subparts as \numsubparts
\def\numpages{\pageref{@lastpage}}
\def\numpoints{\pageref{@numpoints}}
\def\numquestions{\pageref{@numquestions}}
\def\numparts{\pageref{@numparts}}
\def\numsubparts{\pageref{@numsubparts}}

%%%\let\@realenddocument=\enddocument
%%%\def\enddocument{\clearpage
%%%   \if@filesw 
%%%     {\advance\c@page-1 \immediate\write\@mainaux
%%%       {\string\newlabel{@lastpage}{{}{\arabic{page}}}}%
%%%     }
%%%   \fi
%%%   \@realenddocument
%%%}

\AtEndDocument{\clearpage
   \if@filesw 
     {\advance\c@page-1 \immediate\write\@mainaux
       {\string\newlabel{@lastpage}{{}{\arabic{page}}}}%
       \advance\c@page+1 % In case some other package looks at \c@page
       \immediate\write\@mainaux
       {\string\newlabel{@numpoints}{{}{\thenumpoints}}}%
       \immediate\write\@mainaux
       {\string\newlabel{@numquestions}{{}{\thenumquestions}}}%
       \immediate\write\@mainaux
       {\string\newlabel{@numparts}{{}{\thenumparts}}}%
       \immediate\write\@mainaux
       {\string\newlabel{@numsubparts}{{}{\thenumsubparts}}}%
     }
   \fi
   % Echo numbers of questions, parts, and subparts:
   \typeout{This exam contains \thenumquestions\space questions
     with \thenumparts\space parts and
     \thenumsubparts\space subparts.}
   % If counting points, echo total points:
   \if@printtotalpoints
     \typeout{This exam has a total of \thenumpoints\space points.}
   \fi
}


% We define \iflastpage so that it can safely be used
% in headers and footers:
\def\iflastpage#1#2{%
      \@ifundefined{r@@lastpage}{\def\@@lastpage{-1}}%
              {\edef\@@lastpage{\expandafter\@cdr\r@@lastpage\@nil}}%
      \ifnum\value{page}=\@@lastpage
        #1%
      \else
        #2%
      \fi
}


% The macro \oddeven takes two arguments.  If the page number is odd,
% then you get the first argument; otherwise, you get the second
% argument.
\def\oddeven#1#2{%
  \ifodd\value{page}%
    #1
  \else
    #2
  \fi
}







%---------------------------------------------------------------------
%
%                    ***************************
%                    ** QUESTION ENVIRONMENTS **
%                    ***************************
%
%
%
% We define the command \part only inside of a parts environment,
% so that we don't interfere with the meaning of the standard
% article documentclass command \part if that is used inside of a
% questions environment.  The commands \question and \subpart are
% defined everywhere inside of a questions environment.  (If the 
% user accidentally gives a \subpart command outside of a subparts
% environment, then a warning will be printed, and the \subpart
% command will be treated as either a \question command or a
% \part command (depending on the current environment).




% We use the counter name `partno' for the parts environment so that
% we will not interfere with the counter `part' used by the article
% document class.

%%%\@definecounter{question}
%%%\@definecounter{partno}
%%%\@definecounter{subpart}
\newcounter{question}
\newcounter{partno}
\newcounter{subpart}
\newcounter{numpoints}
\newcounter{numquestions}
\newcounter{numparts}
\newcounter{numsubparts}


\newenvironment{questions}%
  {\def\@queslevel{question}%
    \def\question{%
      \@checkqueslevel{question}%
      \addtocounter{numquestions}{1}%
      \@doitem
    }%
    \def\subpart{%
      \@checkqueslevel{subpart}%
      \addtocounter{numsubparts}{1}%
      \@doitem
    }%
    \list{\thequestion.}%
    {\usecounter{question}\def\makelabel##1{\hss\llap{##1}}%
      \def\thequestion{\arabic{question}}%
      \settowidth{\leftmargin}{10.\hskip\labelsep}
      \labelwidth\leftmargin\advance\labelwidth-\labelsep
      \partopsep=0pt
    }%
  }%
  {\endlist}

\newenvironment{parts}%
  {\def\@queslevel{part}%
     \def\part{%
       \@checkqueslevel{part}%
       \addtocounter{numparts}{1}%
       \@doitem
     }%
     \list{(\thepartno)}%
     {\usecounter{partno}\def\makelabel##1{\hss\llap{##1}}%
       \def\thepartno{\alph{partno}}%
       \settowidth{\leftmargin}{(m)\hskip\labelsep}
       \labelwidth\leftmargin\advance\labelwidth-\labelsep
       \topsep=0pt
       \partopsep=0pt
     }%
  }%
  {\endlist}

\newenvironment{subparts}%
  {\def\@queslevel{subpart}%
     \list{\thesubpart.}%
     {\usecounter{subpart}\def\makelabel##1{\hss\llap{##1}}%
       \def\thesubpart{\roman{subpart}}%
       \settowidth{\leftmargin}{vii.\hskip\labelsep}
       \labelwidth\leftmargin\advance\labelwidth-\labelsep
       \topsep=0pt
       \partopsep=0pt
     }%
  }%
  {\endlist}


\def\@checkqueslevel#1{%
   \begingroup
     \def\@temp{#1}%
     \ifx\@temp\@queslevel
       % Everything's fine; do nothing.
     \else
       \@warning{I found a #1 where I expected to find a \@queslevel}
     \fi
   \endgroup
}


\def\@doitem{\@ifnextchar[{\@readpoints}{\item\@setpoints}}

\def\@readpoints[#1]{%
  \edef\@points{#1}%
  \@placepointstrue
  \if@addpoints
    \addtocounter{numpoints}{\@points}
  \fi
  \item
  \@setpoints
}

\def\@setpoints{%
  % The \item command sets \everypar so that the first time we enter
  % horizontal mode (which will cause \everypar to be added to the
  % paragraph), the label (or labels, if, e.g., a \question begins
  % with a parts environment) will be placed on the page, a couple
  % of other bookkeeping chores are done, and then \everypar is
  % set to the empty token string (so that none of this will be
  % repeated for the following paragraphs).
  % 
  % We check to see if there are points to be placed for this item.
  % if so, we append either
  %   \llap{(\@points)\hskip\@totalleftmargin\hskip\marginpointssep}%
  %         \@placepointsfalse
  % or
  %   (\@points\@pointname)\enspace\@placepointsfalse
  % to \everypar, so that the number of points will be set whenever
  % we first enter horizontal mode, and the flag to set points will
  % be turned off.  (Actually, that's what we do if \if@boxedpoints is
  % false; if it's true, we do the analgoous thing with commands that
  % use \fbox instead of parentheses.)  (Resetting the flag is put
  % into \everypar so that if another \item is encounteres before we
  % actually enter horizontal mode, we'll put this back into the new
  % version of \everypar that will be created by that \item.)
  \if@placepoints
    \if@pointsinmargin
      \if@boxedpoints
        \everypar=\expandafter{\the\everypar
            \llap{\fbox{\@points\@marginpointname}\hskip\@totalleftmargin
                  \hskip\marginpointssep}%
            \@placepointsfalse}%
      \else
        \everypar=\expandafter{\the\everypar
            \llap{(\@points\@marginpointname)\hskip\@totalleftmargin
                  \hskip\marginpointssep}%
            \@placepointsfalse}%
      \fi
    \else
      \if@boxedpoints
        \everypar=\expandafter{\the\everypar
            \fbox{\@points\@pointname}\enspace\@placepointsfalse}%
      \else
        \everypar=\expandafter{\the\everypar
            (\@points\@pointname)\enspace\@placepointsfalse}%
      \fi
    \fi
  \fi
}% @setpoints

\newif\if@placepoints
\@placepointsfalse



% If the user says \pointsinmargin, then the distance from
% the right parentheses enclosing the points to the left margin
% will be \marginpointssep:
\newskip\marginpointssep
\setlength{\marginpointssep}{5pt}

\newif\if@pointsinmargin
\def\pointsinmargin{\global\@pointsinmargintrue}
\def\nopointsinmargin{\global\@pointsinmarginfalse}
\@pointsinmarginfalse

\newif\if@boxedpoints
\def\boxedpoints{\global\@boxedpointstrue}
\def\noboxedpoints{\global\@boxedpointsfalse}
\@boxedpointsfalse



\def\pointname#1{\gdef\@pointname{#1}}
% Initialize to leave a space, and then the word `points':
%%\pointname{ points}
% The following improvement was contributed by 
% Mate Wierdl <mw@wierdlmpc.msci.memphis.edu> 
% If the number of points is ``1'', then the default value of
% \pointname will print `` point'' instead of `` points'' (and this
% version of the command doesn't generate an error message if the
% points entry is something other than a number):
\pointname{ \ifthenelse{\equal{\@points}{1}}{point}{points}}

% If we used the following line instead, then you'd get an error
% message if the point value contained something other than a valid
% integer:
%\pointname{ \ifthenelse{\@points = 1}{point}{points}}

% \@marginpointname is used in place of \@pointname if
% \@pointsinmargin is true:
\def\marginpointname#1{\gdef\@marginpointname{#1}}
\marginpointname{}


% The following keeps track of whether the user has requested that we
% add up the points on the exam.  We make the default false so that
% users who put other than numbers into the points argument of a
% question (or part, or subpart) won't get error messages.
% We use \if@printtotalpoints as a flag to signal that we are counting
% points, so that we will know to print the total on the screen (and
% in the log file).  We use this separate flag so that the user can
% use both \addpoints and \noaddpoints to count some points and not
% others, but still have the total printed when we finish the file no
% matter what the state of \if@addpoints.
\newif\if@addpoints
\newif\if@printtotalpoints
\def\addpoints{\global\@addpointstrue\global\@printtotalpointstrue}
\def\noaddpoints{\global\@addpointsfalse}
\@addpointsfalse
\@printtotalpointsfalse

%--------------------------------------------------------------------
%--------------------------------------------------------------------

%                      \uplevel and \fullwidth:

% \uplevel is used to print text at the indentation level of the 
% enclosing environment.  For example, to precede a question with
% directions about how that question should be answered, you would
% say \uplevel{Answer this question correctly.}
% 
% \fullwidth is similar, but uses the full page of text on the page.

\long\def\uplevel#1{%
  \par\bigskip
  \vbox{%
 {}   \advance\leftskip\@totalleftmargin
    \advance\leftskip-\leftmargin
    #1\par
  }% vbox
  \nobreak
}

\long\def\fullwidth#1{%
  \par\bigskip
  \vbox{%
    \leftskip=0pt \rightskip=0pt
    #1\par
  }% vbox
  \nobreak
}

%---------------------------------------------------------------------


\endinput




%---------------------------------------------------------------------
%---------------------------------------------------------------------
%---------------------------------------------------------------------
%---------------------------------------------------------------------

