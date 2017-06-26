Name: microcode-intel
Version: 20170511
Release: 1
Source0: https://downloadmirror.intel.com/26400/eng/microcode-%{version}.tgz
Summary: Latest microcode (firmware) for Intel processors
URL: https://downloadcenter.intel.com/download/26400/Linux-Processor-Microcode-Data-File
License: distributable
Group: System/Kernel and hardware
BuildArch: noarch
BuildRequires: iucode-tool
ExclusiveArch: %{ix86} x86_64

%description
Latest microcode (firmware) for Intel processors

%prep
%setup -qc %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/lib/firmware/intel-ucode %{buildroot}/boot
%{_sbindir}/iucode_tool --write-firmware=%{buildroot}/lib/firmware/intel-ucode microcode.dat
%{_sbindir}/iucode_tool --write-earlyfw=%{buildroot}/boot/microcode.img microcode.dat

%files
/lib/firmware/intel-ucode
/boot/microcode.img
