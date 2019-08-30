#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-pgjdbc
Version  : el9.4.1207
Release  : 2
URL      : https://github.com/pgjdbc/pgjdbc/archive/REL9.4.1207.tar.gz
Source0  : https://github.com/pgjdbc/pgjdbc/archive/REL9.4.1207.tar.gz
Source1  : https://repo1.maven.org/maven2/org/postgresql/postgresql/9.4.1207.jre7/postgresql-9.4.1207.jre7.jar
Source2  : https://repo1.maven.org/maven2/org/postgresql/postgresql/9.4.1207.jre7/postgresql-9.4.1207.jre7.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-pgjdbc-data = %{version}-%{release}

%description
To run the SSL tests, the following properties are used:
certdir: directory where the certificates and keys are store

%package data
Summary: data components for the mvn-pgjdbc package.
Group: Data

%description data
data components for the mvn-pgjdbc package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/postgresql/postgresql/9.4.1207.jre7
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/postgresql/postgresql/9.4.1207.jre7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/postgresql/postgresql/9.4.1207.jre7
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/postgresql/postgresql/9.4.1207.jre7


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/postgresql/postgresql/9.4.1207.jre7/postgresql-9.4.1207.jre7.jar
/usr/share/java/.m2/repository/org/postgresql/postgresql/9.4.1207.jre7/postgresql-9.4.1207.jre7.pom
