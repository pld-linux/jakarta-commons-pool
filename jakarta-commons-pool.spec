Summary:	Jakarta Commons Pool
Name:		jakarta-commons-pool
Version:	1.0.1
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/jakarta-commons/release/commons-pool/v%{version}/commons-pool-%{version}-src.tar.gz
URL:		http://jakarta.apache.org/
Requires:	jre
BuildRequires:	jakarta-ant
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Jakarta Commons Modeller.

%package doc
Summary:	Jakarta Commons Modeller
Group:		Development/Languages/Java

%description doc
Jakarta Commons Modeller.

%prep
%setup -q -n commons-pool-%{version}-src

%build
ant dist

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install dist/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dist/LICENSE.txt
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc dist/docs
