Summary:	C++ Template Image Processing Library
Summary(pl.UTF-8):	Biblioteka szablonów C++ do przetwarzania obrazu
Name:		CImg
Version:	1.1.8
Release:	1
License:	CeCILL Free Software License
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/cimg/%{name}-1-18.zip
# Source0-md5:	444bc816e8a489cede7a69ade3261d9d
URL:		http://cimg.sourceforge.net/
BuildRequires:	unzip
Conflicts:	gcc-c++ < 4.0
Requires:	libstdc++-devel
Requires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CImg Library is an open-source C++ toolkit for image processing.
It consists in a single header file 'CImg.h' providing a set of C++
classes and functions that can be used in your own sources, to
load/save, process and display images. Very portable (Unix/X11,
Windows, MacOS X, FreeBSD, ...), efficient, easy to use, it's a
pleasant toolkit for coding image processing stuffs in C++.

%description -l pl.UTF-8
Biblioteka CImg to toolkit C++ o otwartych źródłach służący do
przetwarzania obrazu. Składa się z pojedynczego pliku nagłówkowego
CImg.h udostępniającego zbiór klas i funkcji C++, które można
wykorzystać we własnych źródłach do wczytywania, zapisywania,
przetwarzania i wyświetlania obrazów. Jest przenośny (Unix/X11,
Windows, MacOS X, FreeBSD...), wydajny, łatwy w użyciu i przyjemny do
kodowania przetwarzania obrazu w C++.

%prep
%setup -q -n %{name}-1-18

cp plugins/README.txt README-plugins.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/%{name}/plugins,%{_examplesdir}/%{name}-%{version}/img}

install CImg.h $RPM_BUILD_ROOT%{_includedir}/%{name}
install plugins/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/plugins
install examples/{*.cpp,*.m,Makefile} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/img/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/img

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt Licence* README*.txt documentation/*
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/plugins
%{_includedir}/%{name}/CImg.h
%{_includedir}/%{name}/plugins/*.h
%{_examplesdir}/%{name}-%{version}
