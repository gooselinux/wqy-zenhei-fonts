%global fontname wqy-zenhei

%global fontconf  44-%{fontname}.conf
%global fontconf1 65-%{fontname}.conf
%global fontconf2 43-%{fontname}-sharp.conf

%define common_desc \
WenQuanYi Zen Hei is a Hei-Ti style (sans-serif type) Chinese \
outline font. It is designed for general purpose text formatting \
and on-screen display of Chinese characters and symbols from \
many other languages. The embolden strokes of the font glyphs \
produces enhanced screen contrast, making it easier to read \
recognize. The embedded bitmap glyphs further enhance on-screen \
performance, which can be enabled with the provided configuration \
files. WenQuanYi Zen Hei provides a rather complete coverage to \
Chinese Hanzi glyphs, including both simplified and traditional \
forms. The total glyph number in this font is over 35,000, including \
over 21,000 Chinese Hanzi. This font has full coverage to GBK(CP936) \
charset, CJK Unified Ideographs, as well as the code-points \
needed for zh_cn, zh_sg, zh_tw, zh_hk, zh_mo, ja (Japanese) \
and ko (Korean) locales for fontconfig. Starting from version \
0.8, this font package has contained two font families, i.e. \
the proportionally-spaced Zen Hei, and a mono-spaced face \
named "WenQuanYi Zen Hei Mono".

%define setscript zenheiset

Name:           %{fontname}-fonts
Version:        0.9.45
Release:        3%{?dist}
Summary:        WenQuanYi Zen Hei CJK Font

Group:          User Interface/X
License:        GPLv2 with exceptions
URL:            http://wenq.org/enindex.cgi
Source0:        http://downloads.sourceforge.net/wqy/%{fontname}-%{version}.tar.gz
Source1:        %{fontname}-fontconfig.conf
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Patch0:         wqy-zenhei-fonts-0.8.34-1-noprefer.patch
Patch1:         zenheiset-0.8.38-1-fontpackages.patch
Patch2:         wqy-zenhei-fonts-0.8.38-1-zenheiset.patch

%description
%common_desc

%package common
Summary:  Common files for WenQuanYi Zen Hei CJK Font
Requires: fontpackages-filesystem

%description common
%common_desc
This package consists of files used by other %{name} packages.

%prep
%setup -q -n %{fontname}
%patch0 -p1
%patch1 -p1
%patch2 -p1
chmod 644 %{setscript}

# Convert to utf-8
for file in AUTHORS README; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done


%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttc %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf1}
install -m 0644 -p %{fontconf2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf2}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf1} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf1}

%clean
rm -fr %{buildroot}


%_font_pkg -f ??-%{fontname}*.conf *.ttc

%files common
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%doc %{setscript} 


%changelog
* Fri Jun 11 2010  Peng Wu <pwu@redhat.com> - 0.9.45-3
- Resolves: rhbz#592843: Request to add wqy-zenhei-fonts to RHEL 6.0.
- Clean up the spec file.

* Mon Apr 19 2010  Peng Wu <pwu@redhat.com> - 0.9.45-2
- get rid of binding="same", fixes [rhbz#578051] New: lang-specific overrides rule doesn't work as expected.

* Mon Mar 15 2010  Peng Wu <pwu@redhat.com> - 0.9.45-1
- Update to the upstream version 0.9.45 (#573330)

* Mon Mar 01 2010 Peng Wu <pwu@redhat.com> - 0.8.38-5
- make this package adopt the Packaging:FontsPolicy (#568587)

* Mon Dec 21 2009 Jens Petersen <petersen@redhat.com> - 0.8.38-4
- add a fedora fontconfig file for zh (#476459)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

*Mon Mar 30 2009 Qianqian Fang <fangqq@gmail.com> 0.8.38-2
- rebuild to pickup font autodeps (# 491974)

*Sat Mar 07 2009 Qianqian Fang <fangqq@gmail.com> 0.8.38-1
- update to the final version of upstream v0.8 release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.34-3.20081027cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

*Wed Feb 11 2009 Qianqian Fang <fangqq@gmail.com> 0.8.34-2.20081027cvs
- remove fontconfig preference section (# 476459)

*Tue Feb 10 2009 Qianqian Fang <fangqq@gmail.com> 0.8.34-1.20081027cvs
- use fontpackages macros (# 478891)

*Mon Oct 27 2008 Qianqian Fang <fangqq@gmail.com> 0.8.34-0.cvs20081027
- upstream new version prelease

*Wed Jun 25 2008 Qianqian Fang <fangqq@gmail.com> 0.6.26-0
- new upstream release

*Sat Apr 5 2008 Qianqian Fang <fangqq@gmail.com> 0.5.23-0
- new upstream release

*Fri Feb 15 2008 Qianqian Fang <fangqq@gmail.com> 0.4.23-1
- new upstream release

*Fri Nov 2 2007 Qianqian Fang <fangqq@gmail.com> 0.2.16-0.2.20071031cvs
- spec file clean up

*Thu Nov 1 2007 Qianqian Fang <fangqq@gmail.com> 0.2.16-0.1.20071031cvs
- initial packaging for Fedora (# 361121)

