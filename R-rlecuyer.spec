#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rlecuyer
Version  : 0.3.5
Release  : 4
URL      : https://cran.r-project.org/src/contrib/rlecuyer_0.3-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rlecuyer_0.3-5.tar.gz
Summary  : R Interface to RNG with Multiple Streams
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-rlecuyer-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
random number generator with multiple independent streams
        developed by L'Ecuyer et al (2002). The main purpose of this
        package is to enable the use of this random number generator in
        parallel R applications.

%package lib
Summary: lib components for the R-rlecuyer package.
Group: Libraries

%description lib
lib components for the R-rlecuyer package.


%prep
%setup -q -c -n rlecuyer
cd %{_builddir}/rlecuyer

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641097677

%install
export SOURCE_DATE_EPOCH=1641097677
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rlecuyer
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rlecuyer
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rlecuyer
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rlecuyer || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rlecuyer/DESCRIPTION
/usr/lib64/R/library/rlecuyer/INDEX
/usr/lib64/R/library/rlecuyer/Meta/Rd.rds
/usr/lib64/R/library/rlecuyer/Meta/features.rds
/usr/lib64/R/library/rlecuyer/Meta/hsearch.rds
/usr/lib64/R/library/rlecuyer/Meta/links.rds
/usr/lib64/R/library/rlecuyer/Meta/nsInfo.rds
/usr/lib64/R/library/rlecuyer/Meta/package.rds
/usr/lib64/R/library/rlecuyer/NAMESPACE
/usr/lib64/R/library/rlecuyer/R/rlecuyer
/usr/lib64/R/library/rlecuyer/R/rlecuyer.rdb
/usr/lib64/R/library/rlecuyer/R/rlecuyer.rdx
/usr/lib64/R/library/rlecuyer/help/AnIndex
/usr/lib64/R/library/rlecuyer/help/aliases.rds
/usr/lib64/R/library/rlecuyer/help/paths.rds
/usr/lib64/R/library/rlecuyer/help/rlecuyer.rdb
/usr/lib64/R/library/rlecuyer/help/rlecuyer.rdx
/usr/lib64/R/library/rlecuyer/html/00Index.html
/usr/lib64/R/library/rlecuyer/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rlecuyer/libs/rlecuyer.so
/usr/lib64/R/library/rlecuyer/libs/rlecuyer.so.avx2
/usr/lib64/R/library/rlecuyer/libs/rlecuyer.so.avx512
