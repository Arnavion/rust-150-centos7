Name: foo
Version: 1.0.0
Release: 1
Summary: .
License: MIT
URL: https://github.com/Arnavion/foo
Source: foo-%{version}-%{release}.tar.gz


%description
.


%prep

%setup -q


%build

# Nothing to do here.


%install

# https://docs.fedoraproject.org/en-US/packaging-guidelines/RPMMacros/#_macros_for_paths_set_and_used_by_build_systems
#
# Yes, docdir is different in that it includes the name of the package, whereas others like includedir and libexecdir do not
# and the invocation of `install` is expected to append the package name manually.

make -j \
    DESTDIR=%{buildroot} \
    bindir=%{_bindir}


%pre


%post


%preun


%postun


%files

# Binaries
%{_bindir}/%{name}


%changelog
