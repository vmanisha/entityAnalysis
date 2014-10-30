\ProvidesClass{a0poster}[2004/01/31 v1.22b a0poster class (GK, MW)]
\NeedsTeXFormat{LaTeX2e}[1995/06/01]
\LoadClass{article}

\newif\ifportrait
\newif\ifanullb
\newif\ifanull
\newif\ifposterdraft

\newcount\xkoord
\newcount\ykoord
\newcount\xscale
\newcount\yscale

\DeclareOption{a0}{
	\anulltrue
	\anullbfalse
	\xkoord=2380 % big points (1 bp=1/72 inch)
	\ykoord=3368 % big points (1 bp=1/72 inch)
	\xscale=2
	\yscale=2
}
\DeclareOption{landscape}{
	\portraitfalse
}
\DeclareOption{portrait}{
	\portraittrue
}
\DeclareOption{draft}{   %% Just for downward compatibility
	\posterdrafttrue
}
\DeclareOption{final}{
	\posterdraftfalse
}
\DeclareOption*{
	\PackageWarning{a0poster}{Unknown Option \CurrentOption}
}
\ExecuteOptions{landscape,a0,final}
\ProcessOptions\relax

\setlength{\paperwidth}{46.8in}
\setlength{\paperheight}{33.1in}
\setlength{\textwidth}{44.8in}
\setlength{\textheight}{31.1in}
\setlength{\topmargin}{0in}
\setlength{\headheight}{0in}
\setlength{\headsep}{0in}
\setlength{\oddsidemargin}{0in}
\setlength{\evensidemargin}{0in}
\setlength{\parskip}{0.0in}

%% Setting proper dimensions for a DIN A0 printer

\catcode`\%=11
\newwrite\Ausgabe
\immediate\openout\Ausgabe=a0header.ps
\write\Ausgabe{%%BeginFeature *PageSize ISOA0/ISO A0}
\ifposterdraft\write\Ausgabe{2 dict dup /PageSize [595 842] put dup /ImagingBBox null put}
\else\write\Ausgabe{2 dict dup /PageSize [\number\xkoord\space \number\ykoord] put dup /ImagingBBox null put}\fi
\write\Ausgabe{setpagedevice}
\ifposterdraft\write\Ausgabe{38 84 translate}
\write\Ausgabe{0.\number\xscale\space 0.\number\yscale\space scale}\else\relax\fi
\write\Ausgabe{%%EndFeature}
\closeout\Ausgabe
\catcode`\%=14

\special{header=./a0header.ps}

\input{a0size.sty}

\renewcommand{\tiny}{\fontsize{12}{14}\selectfont}
\renewcommand{\scriptsize}{\fontsize{14.4}{18}\selectfont}   
\renewcommand{\footnotesize}{\fontsize{17.28}{22}\selectfont}
\renewcommand{\small}{\fontsize{20.74}{25}\selectfont}
\renewcommand{\normalsize}{\fontsize{24.88}{30}\selectfont}
\renewcommand{\large}{\fontsize{29.86}{37}\selectfont}
\renewcommand{\Large}{\fontsize{35.83}{45}\selectfont}
\renewcommand{\LARGE}{\fontsize{43}{54}\selectfont}
\renewcommand{\huge}{\fontsize{51.6}{64}\selectfont}
\renewcommand{\Huge}{\fontsize{61.92}{77}\selectfont}
\newcommand{\veryHuge}{\fontsize{74.3}{93}\selectfont}
\newcommand{\VeryHuge}{\fontsize{89.16}{112}\selectfont}
\newcommand{\VERYHuge}{\fontsize{107}{134}\selectfont}

\setlength\smallskipamount{6pt plus 2pt minus 2pt}
\setlength\medskipamount{12pt plus 4pt minus 4pt}
\setlength\bigskipamount{24pt plus 8pt minus 8pt}

\setlength\abovecaptionskip{25pt}
\setlength\belowcaptionskip{0pt}
\setlength\abovedisplayskip{25pt plus 6pt minus 15 pt}
\setlength\abovedisplayshortskip{0pt plus 6pt}
\setlength\belowdisplayshortskip{13pt plus 7pt minus 6pt}
\setlength\belowdisplayskip\abovedisplayskip

\normalsize

\AtBeginDocument{
	\ifportrait
		\special{papersize=33.1in,46.8in}
	\else
		\special{papersize=46.8in,33.1in}
	\fi
	\pagestyle{empty}
}

\ifportrait
   \newdimen\temp
   \setlength{\temp}{\paperwidth}
   \setlength{\paperwidth}{\paperheight}
   \setlength{\paperheight}{\temp}
   \setlength{\temp}{\textwidth}
   \setlength{\textwidth}{\textheight}
   \setlength{\textheight}{\temp}
\else\relax
\fi

\endinput
%% 
%% End of file `a0poster.cls'.
