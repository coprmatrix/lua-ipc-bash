%define luarocks_pkg_name ipc-bash
%define luarocks_pkg_version 0.0.1-1
%define luarocks_pkg_prefix ipc-bash-0.0.1-1
%define luarocks_pkg_major 0.0.1
%define luarocks_pkg_minor 1
%global __luarocks_requires %{_bindir}/true
%global __luarocks_provides %{_bindir}/true

Name: lua-ipc-bash
BuildRequires: lua-rpm-macros
Version: %{luarocks_pkg_major}
Release: %{luarocks_pkg_minor}
Summary: Inter process communications between shell session and lua script
Url: https://github.com/huakim/lua-ipc-bash
License: LGPL
Provides: %{luadist %{luarocks_pkg_name} = %{luarocks_pkg_version}}
Requires: %{luadist lua >= 5.1}
Requires: %{luadist posix}
Requires: %{luadist subprocess}
Requires: %{luadist file-util-tempdir}
Requires: %{luadist lua-path}
Requires: %{luadist luafilesystem}

Source0: ipc-bash-0.0.1-1.tar.gz
Source1: ipc-bash-0.0.1-1.rockspec
%{?luarocks_subpackages:%luarocks_subpackages -f}

%description
  

%prep
%autosetup -p1 -n %luarocks_pkg_prefix
%luarocks_prep

%generate_buildrequires

%build
%{?luarocks_subpackages_build}
%{!?luarocks_subpackages_build:%luarocks_build}

%install
%{?luarocks_subpackages_install}
%{!?luarocks_subpackages_install:%luarocks_install %{luarocks_pkg_prefix}.*.rock}
%{?lua_generate_file_list}
%check
%if %{with check}
%{?luarocks_check}
%endif

%files %{?lua_files}%{!?lua_files:-f lua_files.list}
