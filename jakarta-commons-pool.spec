%include	/usr/lib/rpm/macros.java
Summary:	Jakarta Commons Pool - object pooling interfaces
Summary(pl.UTF-8):	Jakarta Commons Pool - interfejsy gospodarujące obiektami
Name:		jakarta-commons-pool
Version:	1.3
Release:	2
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/pool/source/commons-pool-%{version}-src.tar.gz
# Source0-md5:	a2dcdff75de2af76f5f2169494ed3499
Source1:	%{name}-tomcat5-build.xml
URL:		http://jakarta.apache.org/commons/pool/
BuildRequires:	ant
BuildRequires:	jakarta-commons-collections >= 1.0
BuildRequires:	jdk >= 1.2
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
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

%package tomcat5
Summary:	Pool dependency for Tomcat5
Group:		Development/Languages/Java
Obsoletes:	jakarta-commons-pool-source

%description tomcat5
Pool dependency for Tomcat5

%prep
%setup -q -n commons-pool-%{version}-src
cp %{SOURCE1} tomcat5-build.xml

%build
required_jars="commons-collections"
export CLASSPATH=$(build-classpath $required_jars)
%ant dist
%ant -f tomcat5-build.xml

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install dist/commons-pool-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-pool-%{version}.jar
ln -s commons-pool-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-pool.jar

install pool-tomcat5/commons-pool-tomcat5.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tomcat5-%{version}.jar
ln -sf %{name}-tomcat5-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tomcat5.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -sf %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc dist/LICENSE.txt
%{_javadir}/commons-pool.jar
%{_javadir}/commons-pool-%{version}.jar

%files tomcat5
%defattr(644,root,root,755)
%{_javadir}/%{name}-tomcat5.jar
%{_javadir}/%{name}-tomcat5-%{version}.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
