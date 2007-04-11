Summary:	Jakarta Commons Pool - object pooling interfaces
Summary(pl.UTF-8):	Jakarta Commons Pool - interfejsy gospodarujące obiektami
Name:		jakarta-commons-pool
Version:	1.3
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/pool/source/commons-pool-%{version}-src.tar.gz
# Source0-md5:	a2dcdff75de2af76f5f2169494ed3499
URL:		http://jakarta.apache.org/commons/pool/
BuildRequires:	ant
BuildRequires:	jakarta-commons-collections >= 1.0
BuildRequires:	jdk >= 1.2
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jakarta-commons-collections >= 1.0
Requires:	jre >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Pool package defines a generalized object pooling interfaces, and
provides several general-purpose implementations.

%description -l pl.UTF-8
Pakiet Pool definiuje uogólnione interfejsy gospodarowania obiektami
oraz dostarcza kilku implementacji ogólnego przeznaczenia.

%package javadoc
Summary:	Jakarta Commons Pool documentation
Summary(pl.UTF-8):	Dokumentacja do Jakarta Commons Pool
Group:		Documentation
Obsoletes:	jakarta-commons-pool-doc

%description javadoc
Jakarta Commons Pool documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do Jakarta Commons Pool.

%prep
%setup -q -n commons-pool-%{version}-src

%build
required_jars="commons-collections"
export CLASSPATH=$(/usr/bin/build-classpath $required_jars)
%ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install dist/commons-pool-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-pool-%{version}.jar
ln -s commons-pool-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-pool.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
	rm -f %{_javadocdir}/%{name}
fi

%files
%defattr(644,root,root,755)
%doc dist/LICENSE.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
