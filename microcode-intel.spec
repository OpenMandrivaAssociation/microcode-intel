Name: microcode-intel
Version: 20180108
Release: 1
Source0: https://downloadmirror.intel.com/27431/eng/microcode-%{version}.tgz
Summary: Latest microcode (firmware) for Intel processors
URL: https://downloadcenter.intel.com/download/27431/Linux-Processor-Microcode-Data-File
License: distributable
Group: System/Kernel and hardware
BuildArch: noarch
BuildRequires: iucode-tool

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
