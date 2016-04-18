Name: hunspell-uk
Summary: Ukrainian hunspell dictionaries
Version: 1.8.0
Release: 1%{?dist}
Source: http://downloads.sourceforge.net/project/ispell-uk/spell-uk/%{version}/myspell-uk_UA-%{version}.zip
URL: http://ispell-uk.sourceforge.net/
License: BSD
BuildArch: noarch

Requires: hunspell
%if ! %{defined rhel} && 0%{?fedora} >= 23
Supplements: (hunspell and langpacks-uk)
%endif

%description
Ukrainian hunspell dictionaries.

%prep
%setup -q -c -n myspell-uk

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p uk_UA.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/uk_UA.dic
cp -p uk_UA.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/uk_UA.aff
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
uk_UA_aliases="uk-UA"
for lang in $uk_UA_aliases; do
        ln -s uk_UA.aff $lang.aff
        ln -s uk_UA.dic $lang.dic
done
popd


%files
%doc README_uk_UA.txt
%{_datadir}/myspell/*

%changelog
* Mon Apr 18 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 1.8.0-1.R
- initial build. Spec file merged from hunspell-ru
