### RPM external pythia8 183
%define mic %(case %cmsplatf in (*_mic_*) echo true;; (*) echo false;; esac)
%if "%mic" == "true"
Requires: icc
%endif

Requires: hepmc

Source: http://cern.ch/service-spi/external/MCGenerators/distribution/%{n}/%{n}-%{realversion}-src.tgz

%if "%{?cms_cxxflags:set}" != "set"
%define cms_cxxflags -std=c++0x
%endif

%prep
%setup -q -n %{n}/%{realversion}

export USRCXXFLAGS="%cms_cxxflags"
export HEPMCLOCATION=${HEPMC_ROOT} 
export HEPMCVERSION=${HEPMC_VERSION} 
%if "%mic" == "true"
CXX="icpc" CC="icc" USRLDFLAGSSHARED="-fPIC -mmic" USRCXXFLAGS="-fPIC -mmic $USRCXXFLAGS" \
%endif
./configure --prefix=%i --enable-shared --with-hepmc=${HEPMC_ROOT}

%build
%if "%mic" == "true"
CXX="icpc" CC="icc" USRLDFLAGSSHARED="-fPIC -mmic" USRCXXFLAGS="-fPIC -mmic $USRCXXFLAGS" \
%endif
make %makeprocesses

%install
make install
