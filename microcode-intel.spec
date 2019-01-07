Name: microcode-intel
Version: 20180807a
Release: 0.1
Source0: https://downloadmirror.intel.com/28087/eng/microcode-%{version}.tgz
Summary: Latest microcode (firmware) for Intel processors
URL: https://downloadcenter.intel.com/download/27945/Linux-Processor-Microcode-Data-File
License: distributable
Group: System/Kernel and hardware
BuildArch: noarch
ExcludeArch: %{armx}
BuildRequires: iucode-tool >= 2.3

%description
Latest microcode (firmware) for Intel processors

%prep
%setup -qc %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/lib/firmware/intel-ucode %{buildroot}/boot
cd intel-ucode
%{_sbindir}/iucode_tool --write-firmware=%{buildroot}/lib/firmware/intel-ucode .
%{_sbindir}/iucode_tool --write-earlyfw=%{buildroot}/boot/microcode.img .

%files
/lib/firmware/intel-ucode
/boot/microcode.img
