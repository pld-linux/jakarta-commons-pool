Summary:	Jakarta Commons Pool - object pooling interfaces
Summary(pl):	Jakarta Commons Pool - interfejsy gospodaruj±ce obiektami
Name:		jakarta-commons-pool
Version:	1.2
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/pool/source/commons-pool-%{version}-src.tar.gz
# Source0-md5:	e7dc9f479c6a4260f84f6751b434295a
Patch0:		jakarta-commons-pool-java15.patch   
URL:		http://jakarta.apache.org/commons/pool/
BuildRequires:	ant
BuildRequires:	jdk >= 1.2
BuildRequires:	jakarta-commons-collections >= 1.0
Requires:	jakarta-commons-collections >= 1.0
Requires:	jre >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q -n commons-pool-%{version}
%patch0

%build
JAVA_HOME=%{_libdir}/java
export JAVA_HOME
CLASSPATH=$CLASSPATH:%{_datadir}/java/commons-collections.jar
export CLASSPATH
ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install dist/*.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dist/LICENSE.txt
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc dist/docs
