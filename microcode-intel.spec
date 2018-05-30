Name: microcode-intel
Version: 20180425
Release: 1
Source0: https://downloadmirror.intel.com/27776/eng/microcode-%{version}.tgz
Summary: Latest microcode (firmware) for Intel processors
URL: https://downloadcenter.intel.com/download/27776/Linux-Processor-Microcode-Data-File
License: distributable
Group: System/Kernel and hardware
BuildArch: noarch
BuildRequires: iucode-tool >= 2.3

%description
Latest microcode (firmware) for Intel processors

%prep
%setup -qc %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/lib/firmware/intel-ucode %{buildroot}/boot
cd intel-ucode
mv list ..
%{_sbindir}/iucode_tool --write-firmware=%{buildroot}/lib/firmware/intel-ucode .
%{_sbindir}/iucode_tool --write-earlyfw=%{buildroot}/boot/microcode.img .

%files
/lib/firmware/intel-ucode
/boot/microcode.img
