Summary: Open-horizon edge agent
Name: horizon
Version: %{getenv:VERSION}
Release: %{getenv:RELEASE}
Epoch: 1
License: Apache License Version 2.0
Source: horizon-%{version}.tar.gz
Packager: Open-horizon
BuildArch: x86_64
Provides: horizon = %{version}
Requires: horizon-cli docker

#Prefix: /usr/horizon
#Vendor: ?
#Distribution: ?
#BuildRoot: ?

%description
Open-horizon edge node agent

%prep
%setup -q

%build
#todo: the rpm should really build the executables itself, but we have a ways to go before getting there...
# This phase is done in ~/rpmbuild/BUILD/horizon-<version> . All of the tarball source has been unpacked there and
# is in the same file structure as it is in the git repo. $RPM_BUILD_DIR has a value like ~/rpmbuild/BUILD
#env | grep -i build
# Need to play some games to get our src dir under a GOPATH
#rm -f ../src; ln -s . ../src
#mkdir -p ../github.com/open-horizon
#rm -f ../github.com/open-horizon/anax; ln -s ../../anax-%{version} ../github.com/open-horizon/anax
#GOPATH=$RPM_BUILD_DIR make anax

%install
# The install phase puts all of the files in the paths they should be in when the rpm is installed on a system.
# The $RPM_BUILD_ROOT is a simulated root file system and usually has a value like: ~/rpmbuild/BUILDROOT/horizon-1.0.0-1.x86_64
# Following the LSB Filesystem Hierarchy Standard: https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdf
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/horizon/{bin,sbin} $RPM_BUILD_ROOT/etc/default $RPM_BUILD_ROOT/etc/horizon/{policy.d,trust/}
cp -a fs/* $RPM_BUILD_ROOT/

%files
#%defattr(-, root, root)
#%doc LICENSE COPYRIGHT
/usr/horizon
/lib/systemd/system/horizon.service
/etc/default/horizon
/etc/horizon

%clean
# This step happens *after* the %files packaging
rm -rf $RPM_BUILD_ROOT
