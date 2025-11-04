# DVWA Setup Guide (for this project)

1. Provision a Linux VM (e.g., Debian/Kali).
2. Install Apache, PHP, MySQL/MariaDB:
   - `sudo apt update && sudo apt install apache2 php php-mysqli mariadb-server git -y`
3. Clone DVWA:
   - `cd /var/www/html && sudo git clone https://github.com/digininja/DVWA.git dvwa`
4. Create DB and configure `config/config.inc.php` as per DVWA instructions.
5. Set DVWA security level to 'low' via the DVWA security page.
6. Enable verbose Apache logging (custom log format to include Referer and User-Agent).
7. Snapshot the VM before testing.