Name: microcode-intel
Version:	20230214
Release:	2
Source0: https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/archive/Intel-Linux-Processor-Microcode-Data-Files-microcode-%{version}.tar.gz
Summary: Latest microcode (firmware) for Intel processors
URL: https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files
# Used to be https://downloadcenter.intel.com/download/28087/Linux-Processor-Microcode-Data-File and might return there
License: distributable
Group: System/Kernel and hardware
BuildArch: noarch
ExclusiveArch: %{ix86} %{x86_64}
BuildRequires: iucode-tool >= 2.3

%description
Latest microcode (firmware) for Intel processors

%prep
%setup -n Intel-Linux-Processor-Microcode-Data-Files-microcode-%{version}

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/firmware/intel-ucode %{buildroot}/boot
cd intel-ucode
%{_sbindir}/iucode_tool --write-firmware=%{buildroot}%{_prefix}/lib/firmware/intel-ucode .
%{_sbindir}/iucode_tool --write-earlyfw=%{buildroot}/boot/microcode.img .

%files
%{_prefix}/lib/firmware/intel-ucode
/boot/microcode.img
