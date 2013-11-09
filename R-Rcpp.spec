%global packname  Rcpp
%global rlibdir  %{_libdir}/R/library

%define __noautoreq '/usr/bin/R'

Name:             R-%{packname}
Version:          0.10.6
Release:          1
Summary:          Seamless R and C++ Integration
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/Rcpp_0.10.6.tar.gz
Requires:         R-methods 
Requires:         R-RUnit
Requires:         R-inline
Requires:         R-rbenchmark 
BuildRequires:    R-devel
BuildRequires:    Rmath-devel
BuildRequires:    texlive-collection-latex
BuildRequires:    R-methods
BuildRequires:    R-RUnit
BuildRequires:    R-inline
BuildRequires:    R-rbenchmark 

%description
The Rcpp package provides R functions as well as a C++ library which
facilitate the integration of R and C++. . R data types (SEXP) are matched
to C++ objects in a class hierarchy. All R types are supported (vectors,
functions, environment, etc ...)  and each type is mapped to a dedicated
class. For example, numeric vectors are represented as instances of the
Rcpp::NumericVector class, environments are represented as instances of
Rcpp::Environment, functions are represented as Rcpp::Function, etc ...
The "Rcpp-introduction" vignette provides a good entry point to Rcpp. .
Conversion from C++ to R and back is driven by the templates Rcpp::wrap
and Rcpp::as which are highly flexible and extensible, as documented in
the "Rcpp-extending" vignette. . Rcpp also provides Rcpp modules, a
framework that allows exposing C++ functions and classes to the R level.
The "Rcpp-modules" vignette details the current set of features of
Rcpp-modules. . Rcpp includes a concept called Rcpp sugar that brings many
R functions into C++. Sugar takes advantage of lazy evaluation and
expression templates to achieve great performance while exposing a syntax
that is much nicer to use than the equivalent low-level loop code. The
"Rcpp-sugar" vignette gives an overview of the feature. . Several examples
are included, and more than 750 unit tests in over 330 unit test functions
provide additional usage examples. . An earlier version of Rcpp,
containing what we now call the 'classic Rcpp API' was written during 2005
and 2006 by Dominick Samperi. This code has been factored out of Rcpp into
the package RcppClassic, and it is still available for code relying on the
older interface. New development should use alwayse use this Rcpp package

%prep
%setup -q -c -n %{packname}
perl -pi -e 's|%{_bindir}/r|%{_bindir}/R|;' `find . -name \*.R` `find . -name \*.r`

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#%check
#%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/announce
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/README
%doc %{rlibdir}/%{packname}/THANKS
%doc %{rlibdir}/%{packname}/NEWS*
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/discovery
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/lib
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/prompt
%{rlibdir}/%{packname}/skeleton
%{rlibdir}/%{packname}/unitTests


%changelog
* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.9.10-1
+ Revision: 776581
- Import R-Rcpp
- Import R-Rcpp





