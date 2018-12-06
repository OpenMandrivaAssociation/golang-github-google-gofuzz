# http://github.com/google/gofuzz

%global goipath         github.com/google/gofuzz
%global commit          44d81051d367757e1c7c6a5a86423ece9afcf63c


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.22%{?dist}
Summary:        Library for populating go objects with random values
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%ifnarch ppc64le %{arm} %{s390x}
%gochecks
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.21.git44d8105
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.20.20161122git44d8105
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.git44d8105
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.18.git44d8105
- Bump to upstream 44d81051d367757e1c7c6a5a86423ece9afcf63c
  related: #1249075

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.gitfd52762
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.gitfd52762
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.gitfd52762
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.gitfd52762
- Bump to upstream fd52762d25a41827db7ef64c43756fd4b9f7e382
  related: #1249075

* Fri Jan 20 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.gitbbcb9da
- Polish the spec file
  related: #1249075

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.12.gitbbcb9da
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.gitbbcb9da
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitbbcb9da
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.9.gitbbcb9da
- Update to spec-2.1
  related: #1249075

* Fri Jul 31 2015 jchaloup <jchaloup@redhat.com> - 0-0.8.gitbbcb9da
- Update spec file spec-2.0
  resolves: #1249075

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gitbbcb9da
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.gitbbcb9da
- Choose the correct architecture
  related: #1141817

* Sun Mar 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.gitbbcb9da
- Bump to upstream bbcb9da2d746f8bdbd6a936686a0a6067ada0ec5
  related: #1141817

* Fri Sep 19 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.4.gitaef70da
- don't redefine gopath
- don't own dirs owned by golang
- preserve timestamps of copied files
- use golang 1.2.1-3 or higher
- quiet setup
- add check

* Tue Aug 12 2014 Eric Paris <eparis@redhat.com> - 0.3.gitaef70da
- Move location and make a bit more generic

* Tue Aug 12 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.2.gitaef70da
- Fix License

* Mon Aug 11 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.1.gitaef70da
- First package for Fedora.

