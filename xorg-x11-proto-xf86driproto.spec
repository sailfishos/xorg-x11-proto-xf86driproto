# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       xorg-x11-proto-xf86driproto
Summary:    X.Org X11 Protocol xf86driproto
Version:    2.1.1
Release:    0
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/xf86driproto-%{version}.tar.bz2
Source100:  xorg-x11-proto-xf86driproto.yaml
Provides:   xf86driproto


%description
This extension defines a protocol to allow user applications to access
the video hardware without requiring data to be passed through the X server.




%prep
%setup -q -n xf86driproto-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post






%files
%defattr(-,root,root,-)
# >> files
%{_datadir}/pkgconfig/xf86driproto.pc
%{_includedir}/X11/dri/xf86dristr.h
%{_includedir}/X11/dri/xf86dri.h
%{_includedir}/X11/dri/xf86driproto.h
# << files


