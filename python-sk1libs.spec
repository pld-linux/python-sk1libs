# NOTE:
# sk1libs/imaging is contains (modified?) parts of python-PIL
# sk1libs/libpdf is a part of python-ReportLab
Summary:	Set of Python non-GUI extensions for sK1 Project
Summary(pl.UTF-8):	Zbiór pythonowych rozszerzeń bez GUI dla projektu sK1
Name:		python-sk1libs
Version:	0.9.1
Release:	1
License:	LGPL v2+
Group:		Libraries/Python
#Source0Download: http://code.google.com/p/uniconvertor/downloads/list
Source0:	http://uniconvertor.googlecode.com/files/sk1libs-%{version}.tar.gz
# Source0-md5:	e18088bbc8a105e7535a96f40b80f284
URL:		http://sk1project.org/
BuildRequires:	freetype-devel >= 2
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	zlib-devel
%pyrequires_eq	python-libs
Suggests:	fonts-TTF-bitstream-vera
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of Python non-GUI extensions for sK1 Project.

%description -l pl.UTF-8
Zbiór pythonowych rozszerzeń bez GUI dla projektu sK1.

%prep
%setup -q -n sk1libs-%{version}

%build
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

# filters/{export,import,parsing,preview}/*.py must stay (they contain plugins info as comments)
find $RPM_BUILD_ROOT%{py_sitedir} -name '*.py' | grep -Ev 'filters/(export|import|parsing|preview)/.*\.py$' | xargs rm -f

# use just system fonts
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/sk1libs/ft2engine/fallback_fonts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHTS
%dir %{py_sitedir}/sk1libs
%{py_sitedir}/sk1libs/__init__.py[co]
%dir %{py_sitedir}/sk1libs/filters
%{py_sitedir}/sk1libs/filters/__init__.py[co]
# NOTE: export/import/parsing/preview plugins NEED *.py because of additional data in comments
%dir %{py_sitedir}/sk1libs/filters/export
%{py_sitedir}/sk1libs/filters/export/*.py
%{py_sitedir}/sk1libs/filters/export/*.py[co]
%dir %{py_sitedir}/sk1libs/filters/formats
%{py_sitedir}/sk1libs/filters/formats/*.py[co]
%dir %{py_sitedir}/sk1libs/filters/import
%{py_sitedir}/sk1libs/filters/import/*.py
%{py_sitedir}/sk1libs/filters/import/*.py[co]
%dir %{py_sitedir}/sk1libs/filters/parsing
%{py_sitedir}/sk1libs/filters/parsing/*.py
%{py_sitedir}/sk1libs/filters/parsing/*.py[co]
%dir %{py_sitedir}/sk1libs/filters/preview
%{py_sitedir}/sk1libs/filters/preview/*.py
%{py_sitedir}/sk1libs/filters/preview/*.py[co]
%dir %{py_sitedir}/sk1libs/ft2engine
%{py_sitedir}/sk1libs/ft2engine/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/sk1libs/ft2engine/ft2.so
%dir %{py_sitedir}/sk1libs/imaging
%{py_sitedir}/sk1libs/imaging/*.py[co]
%attr(755,root,root) %{py_sitedir}/sk1libs/imaging/_imaging*.so
%dir %{py_sitedir}/sk1libs/libpdf
%{py_sitedir}/sk1libs/libpdf/*.py[co]
%dir %{py_sitedir}/sk1libs/libpdf/lib
%{py_sitedir}/sk1libs/libpdf/lib/*.py[co]
%dir %{py_sitedir}/sk1libs/libpdf/pdfbase
%{py_sitedir}/sk1libs/libpdf/pdfbase/*.py[co]
%dir %{py_sitedir}/sk1libs/libpdf/pdfgen
%{py_sitedir}/sk1libs/libpdf/pdfgen/*.py[co]
%dir %{py_sitedir}/sk1libs/pycms
%{py_sitedir}/sk1libs/pycms/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/sk1libs/pycms/_pycms.so
%{py_sitedir}/sk1libs/pycms/profiles
%dir %{py_sitedir}/sk1libs/utils
%{py_sitedir}/sk1libs/utils/*.py[co]
%{py_sitedir}/sk1libs-*.egg-info
