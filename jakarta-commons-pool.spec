Summary:	Jakarta Commons Pool - object pooling interfaces
Summary(pl):	Jakarta Commons Pool - interfejsy gospodaruj±ce obiektami
Name:		jakarta-commons-pool
Version:	1.0.1
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/jakarta-commons/release/commons-pool/v%{version}/commons-pool-%{version}-src.tar.gz
# Source0-md5:	df9aaf5ee3e5d68abbee6eca0b8d037f
URL:		http://jakarta.apache.org/
BuildRequires:	jakarta-ant
BuildRequires:	jdk >= 1.2
BuildRequires:	jakarta-commons-collections >= 1.0
Requires:	jakarta-commons-collections >= 1.0
Requires:	jre >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
The Pool package defines a generalized object pooling interfaces, and
provides several general-purpose implementations.

%description -l pl
Pakiet Pool definiuje uogólnione interfejsy gospodarowania obiektami
oraz dostarcza kilku implementacji ogólnego przeznaczenia.

%package doc
Summary:	Jakarta Commons Pool documentation
Summary(pl):	Dokumentacja do Jakarta Commons Pool
Group:		Development/Languages/Java

%description doc
Jakarta Commons Pool documentation.

%description doc -l pl
Dokumentacja do Jakarta Commons Pool.

%prep
%setup -q -n commons-pool-%{version}-src

%build
JAVA_HOME=/usr/lib/java
export JAVA_HOME
CLASSPATH=$CLASSPATH:/usr/share/java/commons-collections.jar
export CLASSPATH
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
